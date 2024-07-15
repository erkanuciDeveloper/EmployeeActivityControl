from domain.etl_process import ETLProcess
from infrastructure.data_access.database_client import MongoDBClient
from config import Config

class PipelineManager:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.db_client = MongoDBClient()

    def run_pipeline(self):
        etl_process = ETLProcess(self.csv_path, self.db_client)
        etl_process.run()

    def close(self):
        self.db_client.close()
