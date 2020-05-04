import os


class Storage:
    """
    Storage class which works with DocumentPath and PagePath
    """

    def __init__(self, location=None):
        self._location = location

    @property
    def location(self):
        return self._location

    def path(self, _path):
        return os.path.join(
            self.location, _path
        )

    def delete_document(self, doc_path):
        """
        Receives a mglib.path.DocumentPath instance
        """
        pass

    def exists(self, _path):
        return os.path.exists(
            self.path(_path)
        )



