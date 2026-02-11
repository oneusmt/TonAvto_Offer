from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(..., description="Имя пользователя")
    password: str = Field(..., description="Пароль пользователя")


class LoginResponse(BaseModel):
    token: str = Field(..., description="Токен авторизации")


class LogoutResponse(BaseModel):
    detail: str = Field(..., description="Сообщение об успешном выходе")
