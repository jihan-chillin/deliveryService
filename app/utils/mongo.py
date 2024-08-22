import os
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

DATABASE_NAME = os.environ.get("MONGO_DATABASE", "yorigin")

client = AsyncIOMotorClient()
db = client[DATABASE_NAME]


# 접속 시 버전정보 가져오기
async def print_mongo_version():
    status = await client.test.command("serverStatus")
    print(status["version"])

asyncio.run(print_mongo_version()) 