from fastapi import APIRouter, HTTPException, status, Depends

from ..schemas.auth import LoginRequest, LoginResponse, LogoutResponse
from ..security import authenticate_user, create_token, require_token, revoke_token


router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login(payload: LoginRequest):
    if not authenticate_user(payload.username, payload.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль",
        )

    token = create_token()
    return LoginResponse(token=token)


@router.post("/logout", response_model=LogoutResponse, status_code=status.HTTP_200_OK)
def logout(token: str = Depends(require_token)):
    revoke_token(token)
    return LogoutResponse(detail="Вы вышли из системы")
