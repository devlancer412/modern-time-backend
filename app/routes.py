from fastapi import APIRouter
from app.controllers import auth

router = APIRouter()
router.include_router(auth.router)