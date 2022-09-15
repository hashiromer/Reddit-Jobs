
"""
Module for handling different kinds of streams
"""
from win10toast_click import  ToastNotifier
from typing import List
from .keywords import add_metadata
from .submission import JobSubmission
from .database import Database
import webbrowser
from dotenv import dotenv_values




def create_callback_function(url):
    def open_url():
        try:
            webbrowser.open_new(url)
        except Exception:
            print("Failed to open url")

    return open_url


class StreamHandler:
    """
    Class for handling notifications from various streams for processing
    """
    def __init__(self,database:Database) -> None:
        self.persistence=database
        config = dotenv_values(".env")
        self.url=config["FRONTEND_URL"]



    async def handle_reddit_hiring_posts(self,posts:List[JobSubmission])->None:
        """
        Saves the jobs found in database
        """
        jobs_with_metadata=add_metadata(posts)
        added_jobs_ids:set(str)=await self.persistence.persist_jobs(jobs_with_metadata)
        added_jobs=[ job for job in posts if job["url"] in added_jobs_ids]
        print("Handling Jobs")
        self.notify_me(added_jobs)

    def notify_me(self, added_jobs:List):
        """
        Shows the notification of newly posted Jobs as Toast on Windows
        """
        total_new_jobs=len(added_jobs)
        toast=ToastNotifier()
        if total_new_jobs >0 and total_new_jobs <3: 
            for job in added_jobs:
                url=job["url"]
                title=job["title"]
                # message=job.text
                func=create_callback_function(url)
                toast.show_toast(
                    title,
                    url,
                    duration=5,
                    callback_on_click=func
                    )
                
        elif total_new_jobs >=3:
            title=f"{total_new_jobs} added in database"
            func=create_callback_function(self.url)

            toast.show_toast(
            title,
            url,
            duration=5,
            callback_on_click=func
            )
        else:
            print("No new posts found")


