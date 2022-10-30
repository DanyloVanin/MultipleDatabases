import motor.motor_asyncio
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.hr_deparment
user_collection = database.get_collection("cv_collection")
