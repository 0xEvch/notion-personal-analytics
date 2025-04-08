from notion_client import Client
from config import token, autopilot
from core.utils.json_parser import JsonParser

client = Client(auth=token)
database_id = autopilot
response = client.databases.query(database_id)
JsonParser.parse_notion_data(response)
