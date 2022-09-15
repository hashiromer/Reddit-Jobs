
import re
from typing import List, Set



def get_intersection_words(post:Set[str],kwd:Set[str]):
    return post.intersection(kwd)

def split_post_in_words(post:str):
    return set(post.split(" "))


def get_submission_keywords(sub:dict):
    # print(sub)
    post_text:str=sub["text"]
    text=post_text.lower()
    text=text.replace("\n"," ").replace("\r"," ")
    text = re.sub("[^0-9a-zA-Z ]+", "", text)
    text=text.strip()
    text=text.split()
    text=set(text)

    keywords={
    "typescript",
    "java",
    "software",
    "github",
    "usd",
    "react",
    "quote",
    "data",
    "entry",
    "webflow",
    "lead"
    "generation",
    "generate",
    "web",
    "scrap",
    "data",
    "scrap",
    "scraping",
    "hiring",
    "pay",
    "budget",
    "looking for",
    "pm"
    "me",
    "html",
    "javascript",
    "paypal",
    "hire",
    "data",
    "excel",
    "python",
    "price",
    "scrap",
    "mailto",
    "website",
}

    return list(text.intersection(keywords))


def add_metadata(sub:List[dict])->dict:
    s=sub
    for index,submission in enumerate(s):
        keys=get_submission_keywords(submission)
        s[index]["keys"]=keys
        s[index]["_id"]=s[index]["url"]
        s[index]["Applied"]=False
        s[index]["stage"]="Fetched"
        s[index]["platform"]="reddit"
        s[index]["stream_type"]="gigs"
    return s




