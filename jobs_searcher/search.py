from .query import Query
from asyncpraw import Reddit

class RedditClient():
    def __init__(self, praw_client) -> None:
        self.client:Reddit=praw_client

    async def search_reddit(self, query:Query,subreddits:str="all"):
        """
        Searches Reddit for a given query and returns the results as a list

        """
        subreddit = await self.client.subreddit(subreddits)

        search=  subreddit.search(
                                    query=query.query,
                                    time_filter=query.time_filter,
                                    sort=query.sort ,
                                    limit=query.limit
                                )
        sync_list = [gen async for gen in search]
        return sync_list

    
        



