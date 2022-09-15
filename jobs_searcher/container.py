"""
IOC Container
"""

import imp
from typing import List
from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dotenv import dotenv_values
from motor.motor_asyncio import AsyncIOMotorClient
import asyncpraw
from .stream_handler import StreamHandler
from .search import RedditClient
from .database import Database
from .mocks import MAsyncIOMotorClient




class Container(DeclarativeContainer):
    """
    Global IOC Container class for services, singletons and common classes 
    """
    config = dotenv_values(".env")

    client_id = config["REDDIT_CLIENT_ID"]
    app_secret = config["REDDIT_APP_SECRET"]
    user_password = config["REDDIT_PASSWORD"]
    username=config["REDDIT_USERNAME"]
    atlas_uri=config["ATLAS_URI"]


    mongo_client=providers.Singleton(AsyncIOMotorClient,atlas_uri)
    
    # mongo_client=providers.Singleton(MAsyncIOMotorClient,atlas_uri)


    persistence=providers.Factory(Database,mongo_client=mongo_client)

    reddit_praw_client=providers.Singleton(
        asyncpraw.Reddit,
        client_id=client_id,
        password=user_password,
        client_secret=app_secret,
        user_agent="my user agent",
        username=username

    )
    
    reddit_client=providers.Factory(RedditClient,reddit_praw_client)

    stream_handler=providers.Factory(StreamHandler,persistence)


