class Project:
    def __init__(self, name: str, description: str, dependencies: list, dev_dependencies: list, licence_type: str, authors: list):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.licence_type = licence_type
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _stringify_authors(self, authors):
        return "\n- ".join(authors) if len(authors) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.licence_type}\n"
            f"\nAuthors:\n- {self._stringify_authors(self.authors)}\n"
            f"\nDependencies:\n- {self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n- {self._stringify_dependencies(self.dev_dependencies)}"
        )
