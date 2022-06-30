from fastapi import APIRouter
from controllers import auth

router = APIRouter(
  prefix='/api',
  tags=['api'],
  responses={404: {"description": "Not found"}},
)

router.include_router(auth.router)