from contextlib import asynccontextmanager

from seed import seed_admin


@asynccontextmanager
async def lifespan(app):
    seed_admin()
    yield
