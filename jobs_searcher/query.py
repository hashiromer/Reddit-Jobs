from typing import Literal
from pydantic import BaseModel


class Query(BaseModel):
    query:str

    sort: Literal["top"] | Literal["relevance"] | Literal["hot"] |\
          Literal["new"] | Literal["comments"]

    syntax: Literal["cloudsearch"]| Literal["lucene"]| Literal["plain"]

    time_filter:Literal["all"]| Literal["day"]| Literal["hour"] |\
                Literal["month"] | Literal["week"]| Literal["year"]

    subreddit:str

    limit:int


