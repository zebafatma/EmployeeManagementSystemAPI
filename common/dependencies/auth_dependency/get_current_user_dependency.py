import logging

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette_context import request_cycle_context

from common.auth.jwt_handler import decode_access_token
from common.context.request_context import RequestContext
from common.exception.unauthorized_exception import InvalidTokenException
from employee.infrastructure.repository.implementation.auth_repository import (
    AuthRepository,
)

security = HTTPBearer()

logger = logging.getLogger(__name__)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    with request_cycle_context():
        repository = AuthRepository()
        try:
            token = credentials.credentials
            logger.info("Authenticating User")
            payload = decode_access_token(token)
            email = payload.get("sub")
            if email is None:
                logger.error("Token doesnot contain email")
                raise InvalidTokenException()
            admin = repository.get_admin_by_email(email)

            if admin is None:
                logger.error(f"No admin found for email: {email}")
                raise InvalidTokenException()
            RequestContext.set_current_user(admin)
            logger.info(f"User authenticated successfully: {email}")
            yield admin
        except Exception:
            logger.exception("Authentication failed")
            raise
        finally:
            repository.close()
