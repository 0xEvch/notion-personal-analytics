from notion_client import Client
from config import token, autopilot
from core.utils.json_parser import JsonParser

class NotionLoader:
    def __init__(self, token):
        self.client = Client(auth=token)

    def get_database(self):
        response = self._query_notion(autopilot)
        JsonParser.parse_notion_data(response)

    def _query_notion(self, database_id):
        results = []
        has_more = True
        next_cursor = None

        while has_more:
            if next_cursor:
                response = self.client.databases.query(database_id, start_cursor=next_cursor)
            else: 
                response = self.client.databases.query(database_id)
                
            results.extend(response["results"])
            has_more = response["has_more"]

            if has_more:
                next_cursor = response["next_cursor"]
            else:
                next_cursor = None

        return results
    
if __name__ == "__main__":
    loader = NotionLoader(token)
    loader.get_database()