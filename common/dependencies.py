import logging

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from common.auth.jwt_handler import decode_access_token
from common.exception.unauthorized_exception import InvalidTokenException
from data.database import get_db
from employee.infrastructure.repository.auth_repository import AuthRepository

security = HTTPBearer()

logger = logging.getLogger(__name__)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
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
        logger.info(f"User authenticated successfully: {email}")
        return admin
    except Exception:
        logger.exception("Authentication failed")
        raise
    finally:
        repository.close()
