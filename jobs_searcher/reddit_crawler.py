"""
Module for Searching jobs and Tasks posted on Reddit.com
"""
from typing import List
from dependency_injector.wiring import Provide
from asyncpraw.models import Submission
from .query import Query
from .container import Container
from .query_builder import QueryBuilder
from .search import RedditClient
from .submission import JobSubmission
from .utilities import parsez_datetime
from .stream_handler import StreamHandler



def extract_information_from_submission(submission:Submission)->Submission:
    """
    Takes asyncreddit submission as input and returns a Submission class
    """
    submission_date=parsez_datetime(submission.created_utc)
    title=submission.title
    subreddit_name=submission.subreddit.display_name
    url=submission.url
    fliar=submission.link_flair_text
    number_of_comments=int(submission.num_comments)
    upvotes=submission.score
    submission_text=submission.selftext
    is_over_18=submission.over_18
    submission= JobSubmission(
        upvotes=upvotes,
        date=submission_date,
        flair=fliar,
        number_of_comments=number_of_comments,
        url=url,
        subreddit_name=subreddit_name,
        text=submission_text,
        title=title,
        over_18=is_over_18
        )
    return submission



class RedditCrawler:
    """
    Contains utilities for finding jobs posted on Reddit.com
    """
    def __init__(
        self,
        reddit_client:RedditClient=Provide[Container.reddit_client],
        notification:StreamHandler=Provide[Container.stream_handler]
    ) -> None:
        self.reddit_client=reddit_client
        self.notification_system=notification

    #Move to processor class
    def extract_data_from_submissions(self,data:List):
        """
        Extracts relevant data from reddit posts for job listings and saves them as dictionary
        """
        list_data=map(extract_information_from_submission,data)
        list_data=filter(lambda y: y.over_18 is False, list_data)
        #Removing Duplicate urls
        list_data=set(list_data)
        list_data=map(lambda x: x.as_dict(),list_data)
        return list(list_data)
    async def run(self):
        """
        Entry point for this class, starts the process
        for finding and persisting new jobs in database

        """ 
        raw_data=await self.search_jobs()
        data=self.extract_data_from_submissions(raw_data)
        await self.notification_system.handle_reddit_hiring_posts(data)





    async def search_jobs(self):

        """
        Finds 100 Reddit posts posted last week with hiring or
        task flair, ordered by submitted time.
        """

        query_string=QueryBuilder().add_fliar("hiring").add_fliar("task").construct_fliar_query()

        query=Query(
        query=query_string,
        sort="new",
        subreddit="all",
        limit=100,
        time_filter="week",
        syntax="cloudsearch")


        data=await self.reddit_client.search_reddit(query=query)
        # await self.redditClient.Client.close()
        return data
