"""
Main Module
"""

import asyncio
import time
from .container import Container
from .reddit_crawler import RedditCrawler

async def setup_jobs():
    """
    The main method
    """
    container = Container()
    container.wire(modules=[__name__])
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


    reddit_client= RedditCrawler()

    while True:
        await reddit_client.run()
        time.sleep(100)


def fetch_jobs():
    """
    Entry Point
    """
    


    try:
        asyncio.run(setup_jobs())

    except KeyboardInterrupt:
        exit()
    except Exception as general_exception:
        print(general_exception)

