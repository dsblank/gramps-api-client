from .client import Client


class API:
    """
    API class for talking to gramps-web-api via the client.
    """

    def __init__(
        self,
        api_host: str,
        user: str,
        password: str,
    ):
        self.client = Client(api_host, user, password)

    def get_metadata(self, **kwargs):
        return self.client.get("/api/metadata/", **kwargs)

    def get_people(self, **kwargs):
        return self.client.get("/api/people/", **kwargs)

    def get_citations(self, **kwargs):
        return self.client.get("/api/citations/", **kwargs)

    def get_events(self, **kwargs):
        return self.client.get("/api/events/", **kwargs)

    def get_families(self, **kwargs):
        return self.client.get("/api/families/", **kwargs)

    def get_media(self, **kwargs):
        return self.client.get("/api/media/", **kwargs)

    def get_places(self, **kwargs):
        return self.client.get("/api/places/", **kwargs)

    def get_repositories(self, **kwargs):
        return self.client.get("/api/repositories/", **kwargs)

    def get_sources(self, **kwargs):
        return self.client.get("/api/sources/", **kwargs)
