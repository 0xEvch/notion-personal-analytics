from notion_client import Client

class NotionLoader:
    def __init__(self, token, database_id):
        self.client = Client(auth=token)
        self.database = database_id

    def sync_query(self):
        response = self.client.databases.query(self.database)
        return response["results"][0]["id"]

    def get_database(self):
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