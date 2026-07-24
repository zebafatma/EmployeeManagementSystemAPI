import logging

from fastapi import APIRouter, Depends

from common.dependencies.service_dependency.auth_service_depencency import get_signin_service, get_signup_service
from employee.application.models.request.signin_model import SigninRequest
from employee.application.models.request.signup_model import SignupRequest
from employee.application.models.response.current_user_response_model import (
    CurrentUserResponse,
)
from common.dependencies.auth_dependency.get_current_user_dependency import get_current_user
from employee.application.models.response.token_response_model import TokenResponse
from employee.application.services.interface.signin_service_interface import SigninServiceInterface
from employee.application.services.interface.signup_service_interface import SignupServiceInterface

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", response_model=CurrentUserResponse)
def signup_admin(
    request: SignupRequest,
    service:SignupServiceInterface=Depends(get_signup_service)
):
    logger.info("POST /auth/signup called")
    return service.signup(request)


@router.post("/signin", response_model=TokenResponse)
def signin_admin(
    request: SigninRequest,
    service:SigninServiceInterface=Depends(get_signin_service)
):
    logger.info("POST /auth/signin called")
    return service.signin(request)


@router.get("/me", response_model=CurrentUserResponse)
def get_me(
    current_admin=Depends(get_current_user)
):
    logger.info("GET /auth/me called")
    return current_admin
