from flask import Blueprint, render_template, request
import docker
import os
from google.cloud import storage
from google.cloud import container_v1
from google.oauth2 import service_account
import json

upload_container_bp = Blueprint('upload_container_bp', __name__)

# Add this class to create dummy container objects
class DummyContainer:
    def __init__(self, name, short_id, created):
        self.name = name
        self.short_id = short_id
        self.tags = [name]
        self.attrs = {'Created': created}

@upload_container_bp.route('/upload_container/', methods=['GET', 'POST'])
def upload_container():
    # Initialize Docker client
    # docker_client = docker.from_env()
    
    # Create dummy containers with the required attributes
    dummy_containers = [
        DummyContainer('nginx:latest', 'abc123', '2024-03-20T10:00:00'),
        DummyContainer('python:3.9', 'def456', '2024-03-19T15:30:00'),
        DummyContainer('redis:alpine', 'ghi789', '2024-03-18T09:45:00')
    ]

    if request.method == 'POST':
        try:
            container_id = request.form.get('container')
            project_id = request.form.get('project_id')
            registry_name = request.form.get('registry_name')

            # Get credentials from environment
            credentials_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON')
            if not credentials_json:
                raise Exception("GCP credentials not found in environment")

            # Parse credentials JSON
            credentials_info = json.loads(credentials_json)
            credentials = service_account.Credentials.from_service_account_info(
                credentials_info,
                scopes=['https://www.googleapis.com/auth/cloud-platform']
            )

            # Initialize GCP clients
            storage_client = storage.Client(credentials=credentials, project=project_id)
            container_client = container_v1.ClusterManagerClient(credentials=credentials)

            # Get the selected container
            # container = docker_client.containers.get(container_id)
            
            # Tag the container for GCR
            # gcr_tag = f"gcr.io/{project_id}/{registry_name}:{container.short_id}"
            # container.tag(gcr_tag)
            
            # Push to GCR
            # docker_client.images.push(gcr_tag)
            
            return render_template('upload_container.html',
                                # containers=docker_client.containers.list(all=True),
                                # success=f"Container successfully uploaded to {gcr_tag}")
            )
            
        except Exception as e:
            return render_template('upload_container.html')
            # return render_template('upload_container.html',
                                # containers=docker_client.containers.list(all=True),
                                # error=str(e))
    
    # GET request - show container list
    # return render_template('upload_container.html',
                        #  containers=docker_client.containers.list(all=True))
    return render_template('upload_container.html',
                         containers=dummy_containers)
