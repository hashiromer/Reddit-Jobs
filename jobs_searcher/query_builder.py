
"""

Module to build Queries easily for reddit Client

"""

class QueryBuilder:
    """
    Class to build Queries easily for reddit Client

    """
    def __init__(self) -> None:
        self.flairs=[]

    def add_fliar(self,flair:str):
        """
        Add flair to query
        """
        self.flairs.append(flair)
        return self

    def construct_fliar_query(self)->str:
        """
        Creates a query from a list of flairs
        """
        flairs=[]
        for i  in self.flairs:
            flairs.append(f'flair:"{i}"')
        query_search_string=" OR ".join(flairs)
        return query_search_string
