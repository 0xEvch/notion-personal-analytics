from notion_client import Client
from config import token, autopilot
from core.utils.json_parser import JsonParser

class NotionLoader:
    def __init__(self, token, database_id):
        self.client = Client(auth=token)
        self.database = database_id

    def get_database(self):
        response = self._query_notion()
        return JsonParser.parse_notion_data(response)

    def sync_query(self):
        response = self.client.databases.query(self.database)
        return response["results"][0]["id"]

    def _query_notion(self):
        results = []
        has_more = True
        next_cursor = None

        while has_more:
            if next_cursor:
                response = self.client.databases.query(self.database, start_cursor=next_cursor)
            else: 
                response = self.client.databases.query(self.database)
                
            results.extend(response["results"])
            has_more = response["has_more"]

            if has_more:
                next_cursor = response["next_cursor"]
            else:
                next_cursor = None

        return results
    
if __name__ == "__main__":
    loader = NotionLoader(token, autopilot)
    print(loader.get_database())
    print(loader.sync_query())