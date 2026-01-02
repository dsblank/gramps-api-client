import json
import requests
from urllib.parse import urlparse, parse_qs, urlencode
from typing import Optional, Dict, Any


class Client:
    """Client for Gramps Web API"""

    def __init__(self, api_host: str, user: str, password: str):
        """
        Initialize the client.

        Args:
            api_host: Base URL of the API (e.g., "http://localhost:5000")
        """
        self.api_host = api_host.rstrip("/")
        self.user = user
        self.password = password
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self._get_tokens()

    def _get_tokens(self):
        """Get the tokens."""
        data = self._post(
            "/api/token/",
            json={"username": self.user, "password": self.password},
        )
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]

    def _get_headers(self) -> Dict[str, str]:
        """Get headers with authentication."""
        headers = {"Accept": "application/json"}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        return headers

    def get(self, endpoint: str, **kwargs) -> Any:
        """Make a GET request."""
        if not self.access_token:
            raise ValueError("Not logged in.")
        # Convert kwargs to query parameters
        url = f"{self.api_host}{endpoint}"
        if kwargs:
            # JSON encode dict and list values before URL encoding
            encoded_kwargs = {}
            for key, value in kwargs.items():
                if isinstance(value, (dict, list)):
                    encoded_kwargs[key] = json.dumps(value, separators=(",", ":"))
                else:
                    encoded_kwargs[key] = value
            query_string = urlencode(encoded_kwargs)
            separator = "&" if "?" in endpoint else "?"
            url = f"{url}{separator}{query_string}"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, data: Any = None, json: Any = None, **kwargs) -> Any:
        headers = self._get_headers()
        if json is not None:
            headers["Content-Type"] = "application/json"
        response = requests.post(
            f"{self.api_host}{endpoint}",
            headers=headers,
            data=data,
            json=json,
            **kwargs,
        )
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: Any = None, json: Any = None, **kwargs) -> Any:
        """Make a POST request."""
        if not self.access_token:
            raise ValueError("Not logged in.")
        return self._post(endpoint, data, json, **kwargs)

    def put(self, endpoint: str, data: Any = None, json: Any = None, **kwargs) -> Any:
        """Make a PUT request."""
        if not self.access_token:
            raise ValueError("Not logged in.")
        headers = self._get_headers()
        if json is not None:
            headers["Content-Type"] = "application/json"
        response = requests.put(
            f"{self.api_host}{endpoint}",
            headers=headers,
            data=data,
            json=json,
            **kwargs,
        )
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str, **kwargs) -> Any:
        """Make a DELETE request."""
        if not self.access_token:
            raise ValueError("Not logged in.")
        response = requests.delete(
            f"{self.api_host}{endpoint}", headers=self._get_headers(), **kwargs
        )
        response.raise_for_status()
        return response.json() if response.content else None
