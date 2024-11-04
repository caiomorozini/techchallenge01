from app.api.routes import (
    authentication,
    users,
    )
from fastapi import APIRouter


router = APIRouter(prefix="/api/v1")

router.include_router(authentication.router, tags=["Auth"])
router.include_router(users.router, tags=["User"])
