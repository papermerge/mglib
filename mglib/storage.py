import os


class Storage:
    """
    Storage class which works with Endpointsf
    """

    def __init__(self, location=None):
        self._location = location

    @property
    def location(self):
        return self._location

    def path_doc(self, ep):
        return os.path.join(
            self.location,
            ep.path_doc
        )

    def path_result(self, ep):
        return os.path.join(
            self.location, ep.path_result
        )

    def delete(self, ep):
        pass


