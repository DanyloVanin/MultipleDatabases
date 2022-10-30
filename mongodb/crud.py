from mongodb.database import user_collection
from mongodb.schemas import User, UserCities, UserLanguages, UserByOrganization, LanguagesFromCity


async def get_users(limit: int):
    users = []
    async for data in user_collection.find().limit(limit):
        users.append(User(**data))
    return users


async def create_user(user_data: dict) -> User:
    user = await user_collection.insert_one(user_data)
    data = await user_collection.find_one({"_id": user.inserted_id})
    new_user: User = User(**data)
    return new_user


async def get_user(user_id: str) -> User:
    data = await user_collection.find_one({"_id": user_id})
    print(data)
    user: User = User(**data)
    if user:
        return user


async def update_user(user_id: str, data: dict):
    if len(data) < 1:
        return False
    user_data = await user_collection.find_one({"_id": user_id})
    if user_data:
        updated_user = await user_collection.update_one(
            {"_id": user_id}, {"$set": data}
        )
        if updated_user:
            return True
        return False


async def delete_user(user_id: str):
    user = await user_collection.find_one({"_id": user_id})
    if user:
        await user_collection.delete_one({"_id": user_id})
        return True


async def get_all_user_cities():
    user_cities = []
    async for data in user_collection.find(projection={"city": True, "_id": False}):
        user_cities.append(UserCities(**data))
    user_cities = set(map(lambda x: x.city, user_cities))
    print(user_cities)
    total_users = await user_collection.count_documents(filter={})
    return {"cities": user_cities, "total": len(user_cities), "total_users": total_users}


async def get_user_languages(user_id: str):
    data = await user_collection.find_one({"_id": user_id}, projection={"languages": True, "_id": False})
    user: UserLanguages = UserLanguages(**data)
    if user:
        return user.languages


async def group_users_by_organization(limit: int):
    users_by_organization = []
    async for data in user_collection.aggregate([
        {
            '$sample': {
                'size': limit
            }
        },
        {
            '$unwind': {
                'path': '$work_experience',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$group': {
                '_id': '$work_experience.organization',
                'users': {
                    '$addToSet': {
                        'user_id': '$_id',
                        'first_name': '$first_name',
                        'last_name': '$last_name'
                    }
                }
            }
        }
    ]):
        users_by_organization.append(UserByOrganization(**data))
    return users_by_organization


async def get_languages_from_user_in_city(city: str):
    languages_from_city = []
    async for data in user_collection.aggregate([
        {
            '$match': {
                'city': city
            }
        }, {
            '$unwind': {
                'path': '$languages',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$group': {
                '_id': '$city',
                'languages': {
                    '$addToSet': '$languages'
                }
            }
        }
    ]):
        languages_from_city.append(LanguagesFromCity(**data))
    return languages_from_city
