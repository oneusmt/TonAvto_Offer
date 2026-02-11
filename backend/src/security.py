import secrets
from datetime import datetime, timedelta
from typing import Dict

from fastapi import Header, HTTPException, status

from .config import settings


_ACTIVE_TOKENS: Dict[str, datetime] = {}


def _cleanup_expired_tokens() -> None:
    """Remove expired tokens to avoid unbounded memory usage."""
    now = datetime.utcnow()
    expired = [token for token, expires in _ACTIVE_TOKENS.items() if expires < now]
    for token in expired:
        _ACTIVE_TOKENS.pop(token, None)


def authenticate_user(username: str, password: str) -> bool:
    return username == settings.auth_username and password == settings.auth_password


def create_token() -> str:
    _cleanup_expired_tokens()
    token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(hours=settings.auth_token_ttl_hours)
    _ACTIVE_TOKENS[token] = expires_at
    return token


def revoke_token(token: str) -> None:
    _ACTIVE_TOKENS.pop(token, None)


def require_token(authorization: str = Header(None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Необходима авторизация",
        )

    token = authorization.split(" ", 1)[1]
    expires_at = _ACTIVE_TOKENS.get(token)
    if not expires_at:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Недействительный токен",
        )

    if expires_at < datetime.utcnow():
        revoke_token(token)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Срок действия токена истёк",
        )

    return token
