from bson.objectid import ObjectId
from mongodb.database import user_collection
from mongodb.schemas import User

async def get_users():
    users = []
    async for data in user_collection.find():
        users.append(User(**data))
    return users


async def create_user(user_data: dict) -> User:
    user = await user_collection.insert_one(user_data)
    data = await user_collection.find_one({"_id": user.inserted_id})
    new_user: User = User(**data)
    return new_user


async def get_user(user_id: str) -> User:
    data = await user_collection.find_one({"_id": ObjectId(user_id)})
    user: User = User(**data)
    if user:
        return user


async def update_user(user_id: str, data: dict):
    if len(data) < 1:
        return False
    user_data = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user_data:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


async def delete_user(user_id: str):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(user_id)})
        return True


async def get_all_user_cities():
    pass