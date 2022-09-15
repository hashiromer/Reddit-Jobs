from typing import List
from pymongo.errors import BulkWriteError
from motor.motor_asyncio import AsyncIOMotorClient



class Database:
    def __init__(
                    self,
                    mongo_client:AsyncIOMotorClient
    ) -> None:
        self.client=mongo_client

    async def test(self):
        """
        Tests database connection
        """
        posts= [{
            "_id":"Mike",
            "text":"this is mongo testing"
        },
        {
            "_id":"Aehan",
            "text":"Arduinio"
        },
        {
            "_id":"Namaste",
            "text":"YOtoYp"
        }
        ]
        st_database = self.client.sreaming
        jobs_collection=st_database.jobs
        try:
            results=await jobs_collection.insert_many(posts, ordered=False)
            print(f"Number of new inserted documents {len(results.inserted_ids)}")

        except BulkWriteError:
            print(f"Number of new inserted documents {len(results.inserted_ids)}")
            



    async def persist_jobs(self,jobs:List[dict]):
        """
        Uploads list of dictionaries to mongo db database
        """
        st_database = self.client.sreaming
        jobs_collection=st_database.jobs
        try:
            results=await jobs_collection.insert_many(jobs, ordered=False)

            if hasattr(results, "inserted_ids"):
                return set(results.inserted_ids)
                      
            raise ValueError

        except BulkWriteError as bulk_error:
            write_errors=bulk_error.details['writeErrors']
            duplicate_urls=list(map( lambda x: x["op"]["_id"], write_errors))
            all_urls=list(map( lambda x: x["_id"], jobs))
            urls_added=set(all_urls)-set(duplicate_urls)
            return list(urls_added)
             
            # total_duplicates=len(duplicate_urls)
            # new= len(jobs)-total_duplicates
            # print(f"Number of new inserted documents {new}")



    

  
  