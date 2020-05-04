import os


class TemporaryNode:
    """
    Handy class when it comes to testing files/directories
    structures.

    Example of usage:

    with TemporaryNode(MEDIA_ROOT) as media_root:
        docs = media_root.add_folder("docs")
        res = media_root.add_folder("results")
        f1 = docs.add_folder("user_1/document_2")
        f1.add_file("doku.pdf")
        res.add_folder("user_1/document_2/pages")

        docp = DocumentPath(
            user_id=1,
            document_id=2,
            file_name='doku.pdf'
        )

        storage.delete_document(docp)

        self.assertFalse(
            docs.exists()
        )

        self.assertFalse(
            res.exists()
        )
    """

    def __init__(self, location):
        self._location = location

    @property
    def location(self):
        return self._location

    def __enter__(self):
        if not os.path.exists(self.location):
            os.makedirs(self.location)

        return self

    def __exit__(self):
        if os.path.exists(self.location):
            if os.path.is_dir(self.location):
                os.rmdir(self.location)
            else:
                os.remove(self.location)

    def add_folder(self, folder):
        new_location = os.path.join(
            self.location,
            folder
        )
        os.makedirs(new_location)
        return TemporaryNode(new_location)

    def exists(self):
        return os.path.exists(self.location)

    def add_file(self, file):
        pass
        return self
