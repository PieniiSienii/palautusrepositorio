from urllib import request
from project import Project
import tomlkit 


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_data = tomlkit.parse(content)

        tool = toml_data["tool"]
        poetry = tool["poetry"]
        name = poetry["name"]
        description = poetry["description"]
        dependencies = poetry["dependencies"]
        dev_dependencies = poetry["group"]["dev"]["dependencies"]
        authors = poetry["authors"]
        license_type = poetry["license"]
        return Project(name, description, dependencies, dev_dependencies, license_type, authors)
        
