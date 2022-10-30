from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from mongodb.crud import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user,
)

from mongodb.schemas import User, UpdateUser

router = APIRouter()


@router.post("/user", response_model=User)
async def create_user_route(user: User):
    user = jsonable_encoder(user)
    new_user = await create_user(user)
    return new_user


@router.get("/user")
async def get_users_route():
    users = await get_users()
    return users


@router.get("/user/{user_id}", response_model=User)
async def get_user_data_route(user_id: str):
    user = await get_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.put("/user/{user_id}")
async def update_user_data(user_id: str, req: UpdateUser):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_user(user_id, req)
    if updated_student:
        return updated_student
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.delete("/user/{user_id}")
async def delete_user_route(user_id: str):
    deleted_student = await delete_user(user_id)
    if deleted_student:
        return deleted_student
    raise HTTPException(status_code=404, detail="User not found")
