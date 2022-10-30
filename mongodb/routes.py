from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from mongodb.crud import *

from mongodb.schemas import User, UpdateUser

router = APIRouter()


@router.post("/user", response_model=User)
async def create_user_route(user: User):
    user = jsonable_encoder(user)
    new_user = await create_user(user)
    return new_user


@router.get("/user")
async def get_users_route(limit: int):
    users = await get_users(limit)
    return users


@router.get("/user/{user_id}", response_model=User)
async def get_user_data(user_id: str):
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


# Custom queries

@router.get("/user_cities")
async def get_all_user_cities_route():
    user_cities = await get_all_user_cities()
    return user_cities


@router.get("/user/{user_id}/languages")
async def get_user_languages_route(user_id: str):
    user_languages = await get_user_languages(user_id)
    return user_languages


@router.get("/user/group/by_organization")
async def get_users_grouped_by_organization(limit: int):
    grouped_users = await group_users_by_organization(limit)
    return grouped_users


@router.get("/languages/group/by_city/{city}")
async def get_languages_grouped_by_user_city(city: str):
    languages_by_city = await get_languages_from_user_in_city(city)
    return languages_by_city
