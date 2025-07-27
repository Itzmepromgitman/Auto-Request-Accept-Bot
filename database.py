from datetime import datetime, time

from motor.motor_asyncio import AsyncIOMotorClient

from config import DB_NAME, DB_URI

# --- Internal Helpers ---




# --- Your Modified Functions ---


# Initialize Motor client
dbclient = AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]
user_data = database["users"]
config_data = database["config"]


async def add_user(user_id: int):
    try:
        await user_data.update_one(
            {"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True
        )
    except Exception as e:
        print(f"Error adding user {user_id}: {e}")


async def present_user(user_id: int):
    try:
        found = await user_data.find_one({"_id": user_id})
        return bool(found)
    except Exception as e:
        print(f"Error finding user {user_id}: {e}")
        return False


async def full_userbase():
    try:
        cursor = user_data.find({}, {"_id": 1})
        return [doc["_id"] async for doc in cursor]
    except Exception as e:
        print(f"Error retrieving user base: {e}")
        return []


async def del_user(user_id: int):
    try:
        result = user_data.delete_one({"_id": user_id})

    except Exception as e:
        print(f"Error deleting user {user_id}: {e}")

