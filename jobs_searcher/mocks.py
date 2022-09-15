from typing import List
import time
import asyncio
# from asyncpraw import Reddit
from motor.motor_asyncio import AsyncIOMotorClient

import asyncpraw
from unittest.mock import MagicMock, Mock,patch
import requests


class MongoInsertedResult():
    def __init__(self) -> None:
        self.inserted_ids:List[int]=[1,2,44,77,654]

    def parse_obj(self,data):
        self.inserted_ids=data
        return self.inserted_ids

class MongoCollection:
    def __init__(self) -> None:
        pass

    async def insert_many(self,json:dict, ordered:bool):
        time.sleep(1)
        result=MongoInsertedResult()
        print("From mock insert many")
        return result


class MockSubReddit:
    def __init__(self) -> None:
        pass

    def search(self,query:str, time_filter:str,sort:str, limit:int):
        pass


class AsyncMockReddit:
    def __init__(self,client_id,password,client_secret,user_agent,username) -> None:
        self.subreddit=''

class MongoCollections():
    def __init__(self) -> None:
        self.jobs:MongoCollection=MongoCollection()
        self.test:MongoCollection=MongoCollection()

    
        


class MAsyncIOMotorClient:
    def __init__(self, uri:str) -> None:
        self.uri=uri
        self.sreaming=MongoCollections()

    async def test_Client(self):
        data=await self.sreaming.jobs.insert_many(json={"id":1}, ordered=False)
        print(data.inserted_ids)

if __name__ =="__main__":
    # mocked_reddit_client:Reddit=Mock(spec=Reddit)
    # s=mocked_reddit_client
    patcher = patch( "__main__.AsyncIOMotorClient", autospec=True)
    mock_request = patcher.start()
    s:AsyncIOMotorClient=mock_request

    s=s.HOST

    
    
    print(dir(s))


    # s:asyncpraw.models.Redditor
    # s=asyncio.run(  s.username_available(name="shhshs"))
    # print(dir(s))

    

    # client=MAsyncIOMotorClient(uri="test")
    # data=asyncio.run(client.sreaming.jobs.insert_many(json={"id":1},ordered=False))
    # print(data.inserted_ids)

