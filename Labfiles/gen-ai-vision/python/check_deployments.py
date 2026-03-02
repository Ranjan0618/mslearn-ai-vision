import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()
project_endpoint = os.getenv("PROJECT_CONNECTION")

project_client = AIProjectClient(
    credential=DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True
    ),
    endpoint=project_endpoint,
)

try:
    connections = project_client.connections.list()
    print("Available connections:")
    for conn in connections:
        print(f"  - {conn.name} ({conn.connection_type})")
except Exception as ex:
    print(f"Error: {ex}")
