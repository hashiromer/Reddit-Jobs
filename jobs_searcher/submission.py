"""
Data Classes related to Job Submissions
"""

from datetime import datetime
from pydantic import BaseModel

class JobSubmission(BaseModel):
    upvotes: int
    title:str
    date:datetime
    subreddit_name: str
    url:str
    flair:str
    number_of_comments: int
    text:str
    over_18:bool

    @staticmethod
    def get_str_date(date:datetime):
        return date.strftime('%Y-%m-%d %I:%M:%S')

    def as_list(self):
        f=[]
        for field in self.__dataclass_fields__:
            value=getattr(self, field)
            f.append(value)
        return f  

    def as_dict(self)->dict:
        return self.dict()

    def __hash__(self) -> int:
        return hash(self.text)

    def __eq__(self, __o: object) -> bool:
        return self.__hash__()==__o.__hash__()

        




 