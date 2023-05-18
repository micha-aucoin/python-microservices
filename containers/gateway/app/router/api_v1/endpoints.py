from fastapi import APIRouter

from app.auth.api import router as auth_router
from app.user.api import router as user_router
from app.videos.api import router as video_router

api_router = APIRouter()

include_api = api_router.include_router

routers = (
    (auth_router, "auth", "auth"),
    (user_router, "users", "users"),
    (video_router, "videos", "videos"),
)

for router_item in routers:
    router, prefix, tag = router_item

    if tag:
        include_api(router, prefix=f"/{prefix}", tags=[tag])
    else:
        include_api(router, prefix=f"/{prefix}")
