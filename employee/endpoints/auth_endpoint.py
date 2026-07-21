import logging

from fastapi import APIRouter, Depends

from common.dependencies import get_current_user
from employee.application.models.request.signin_model import SigninRequest
from employee.application.models.request.signup_model import SignupRequest
from employee.application.models.response.current_user_response_model import (
    CurrentUserResponse,
)
from employee.application.models.response.token_response_model import TokenResponse
from employee.application.services.signin_service import SigninService
from employee.application.services.signup_service import SignupService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Authentication"])

signup_service = SignupService()
signin_service = SigninService()


@router.post("/signup", response_model=CurrentUserResponse)
def signup_admin(request: SignupRequest):
    logger.info("POST /auth/signup called")
    return signup_service.signup(request)


@router.post("/signin", response_model=TokenResponse)
def signin_admin(request: SigninRequest):
    logger.info("POST /auth/signin called")
    return signin_service.signin(request)


@router.get("/me", response_model=CurrentUserResponse)
def get_me(current_admin=Depends(get_current_user)):
    logger.info("GET /auth/me called")
    return current_admin
