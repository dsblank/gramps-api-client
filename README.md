# gramps-api-client

A Python client library for interacting with [gramps-web-api](https://github.com/gramps-project/gramps-web-api).

## Installation

Install the package using pip:

```bash
pip install gramps-api-client
```

## Usage

```python
from gramps_api_client import API

# Initialize the API client
api = API(
    api_host="http://localhost:5000",
    user="your_username",
    password="your_password"
)

# Get metadata
metadata = api.get_metadata()

# Get people
people = api.get_people()

# Get other resources
citations = api.get_citations()
events = api.get_events()
families = api.get_families()
media = api.get_media()
places = api.get_places()
repositories = api.get_repositories()
sources = api.get_sources()
```

## License

This project is licensed under the GNU Affero General Public License Version 3. See the [LICENSE](LICENSE) file for details.

## Repository

https://github.com/dsblank/gramps-api-client

