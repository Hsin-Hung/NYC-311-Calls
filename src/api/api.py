import os
import pandas as pd
from sodapy import Socrata


class API_Client:
    def __init__(self, timeout=30):
        APP_TOKEN = os.getenv("APP_TOKEN")
        self.client = Socrata("data.cityofnewyork.us", APP_TOKEN, timeout=timeout)

    def getRecords(self, select=["*"], limit=100, offset=0):
        """Get records

        Parameters
        ------------
            select: [String], defaults to [*]
                A List of columns to select

            limit: int, defaults to 100
                Number of records to fetch

            offset: int, defaults to 0
                Number of records to skip

        """

        select = ",".join(select)
        results = self.client.get(
            "erm2-nwe9", select=select, limit=limit, offset=offset
        )
        return pd.DataFrame.from_records(results)

    def getRecordsQuery(self, query):
        """Get records with a SoQL query string

        Parameters
        ------------
            query: string
                SoQL query string

            More info about SoQL query:
                https://dev.socrata.com/docs/queries/query.html
        """
        results = self.client.get("erm2-nwe9", query=query)
        return pd.DataFrame.from_records(results)
