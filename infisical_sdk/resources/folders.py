from typing import Optional
from datetime import datetime

from infisical_sdk.infisical_requests import InfisicalRequests
from infisical_sdk.api_types import ListFoldersResponse, SingleFolderResponse, SingleFolderResponseItem, CreateFolderResponse, CreateFolderResponseItem


class V2Folders:
    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests

    def create_folder(
            self,
            name: str,
            environment_slug: str,
            project_id: str,
            path: str = "/",
            description: str = None) -> CreateFolderResponseItem:

        request_body = {
            "projectId": project_id,
            "environment": environment_slug,
            "name": name,
            "path": path,
            "description": description,
        }

        result = self.requests.post(
            path="/api/v2/folders",
            json=request_body,
            model=CreateFolderResponse
        )

        return result.data.folder

    def list_folders(
            self,
            project_id: str,
            environment_slug: str,
            path: str,
            lastSecretModified: Optional[datetime] = None,
            recursive: bool = False) -> ListFoldersResponse:

        params = {
            "projectId": project_id,
            "environment": environment_slug,
            "path": path,
            "recursive": recursive,
        }

        if lastSecretModified is not None:
            # Format as RFC 3339 (ISO 8601 profile) - uses 'Z' for UTC
            # Workaround for the zod datetime() validation in the API
            iso_string = lastSecretModified.isoformat(timespec='seconds')
            if iso_string.endswith('+00:00'):
                iso_string = iso_string[:-6] + 'Z'
            params["lastSecretModified"] = iso_string

        result = self.requests.get(
            path="/api/v2/folders",
            params=params,
            model=ListFoldersResponse
        )

        return result.data

    def get_folder_by_id(
            self,
            id: str) -> SingleFolderResponseItem:

        params = {
            "id": id,
        }

        result = self.requests.get(
            path=f"/api/v2/folders/{id}",
            params=params,
            model=SingleFolderResponse
        )

        return result.data.folder

