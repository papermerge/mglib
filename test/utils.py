

class TemporaryDir:
    """
    Handy class when it comes to testing files/directories
    structures.

    Example of usage:

    with TemporaryDir(MEDIA_ROOT) as media_root:
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
        pass
