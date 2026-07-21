from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from common.exception.unauthorized_exception import InvalidTokenException

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()  # so that original data doesn't get modified
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )  # when will the token expire
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM
    )  # creating the token
    return encode_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        raise InvalidTokenException()
