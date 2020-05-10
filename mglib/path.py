import logging

logger = logging.getLogger(__name__)

AUX_DIR_DOCS = "docs"
AUX_DIR_RESULTS = "results"


class DocumentPath:
    """
    Document path:
    /<aux_dir>/<user_id>/<doc_id>/<version>/<file_name>

    If version = 0, it is not included in DocumentPath.
    Document's version is incremented everytime pdftk operation runs on it
    (when pages are deleted, reordered, pasted)
    """

    def __init__(
        self,
        user_id,
        document_id,
        file_name,
        aux_dir=AUX_DIR_DOCS,
        version=0
    ):
        self.user_id = user_id
        self.document_id = document_id
        self.file_name = file_name
        self.aux_dir = aux_dir
        # by default, document has version 0
        self.version = version
        self.pages = "pages"

    def url(self):
        return f"{self.dirname}{self.file_name}"

    @property
    def path(self):
        return self.url()

    @property
    def dirname_docs(self):
        _path = (
            f"{AUX_DIR_DOCS}/user_{self.user_id}/"
            f"document_{self.document_id}/"
        )

        return _path

    @property
    def dirname_results(self):
        _path = (
            f"{AUX_DIR_RESULTS}/user_{self.user_id}/"
            f"document_{self.document_id}/"
        )

        return _path

    @property
    def dirname(self):
        full_path = (
            f"{self.aux_dir}/user_{self.user_id}/"
            f"document_{self.document_id}/"
        )

        if self.version > 0:
            full_path = f"{full_path}v{self.version}/"

        return full_path

    @property
    def pages_dirname(self):
        return f"{self.dirname}{self.pages}/"

    def __repr__(self):
        message = (
            f"DocumentPath(version={self.version},"
            f"user_id={self.user_id},"
            f"document_id={self.document_id},"
            f"file_name={self.file_name})"
        )
        return message

    def inc_version(self):
        self.version = self.version + 1

    def copy_from(doc_ep, aux_dir):
        return DocumentPath(
            user_id=doc_ep.user_id,
            document_id=doc_ep.document_id,
            file_name=doc_ep.file_name,
            version=doc_ep.version,
            aux_dir=aux_dir
        )


class PagePath:
    """
    <aux_dir>/<doc_id>/pages/<page_num>/<step>/page-<xyz>.jpg
    """

    def __init__(
        self,
        document_path,
        page_num,
        page_count,
        step=None
    ):
        if not isinstance(page_num, int):
            msg_err = f"PagePath.page_num must be an int. Got {page_num}."
            raise ValueError(msg_err)

        self.document_path = document_path
        self.results_document_ep = DocumentPath.copy_from(
            document_path,
            aux_dir=AUX_DIR_RESULTS
        )
        self.page_count = page_count
        self.page_num = page_num
        self.step = step
        self.pages = self.document_path.pages

    @property
    def ppmroot(self):
        # returns schema://.../<doc_id>/pages/<page_num>/<step>/page
        pages_dirname = self.results_document_ep.pages_dirname
        result = (
            f"{pages_dirname}page_{self.page_num}/"
            f"{self.step.percent}/page"
        )
        return result

    @property
    def pages_dirname(self):
        return self.document_path.pages_dirname

    @property
    def path(self):
        return self.url()

    def url(self):
        return self.txt_url()

    @property
    def txt_path(self):
        return self.txt_url()

    def txt_url(self):
        pages_dirname = self.results_document_ep.pages_dirname
        return f"{pages_dirname}page_{self.page_num}.txt"

    @property
    def hocr_path(self):
        return self.hocr_url()

    def hocr_url(self):
        url = f"{self.ppmroot}-{self.ppmtopdf_formated_number}.hocr"
        return url

    @property
    def img_path(self):
        return self.img_url()

    def img_url(self):
        url = f"{self.ppmroot}-{self.ppmtopdf_formated_number}.jpg"
        return url

    @property
    def ppmtopdf_formated_number(self):

        if self.page_count <= 9:
            fmt_num = "{num:d}"
        elif self.page_count > 9 and self.page_count < 100:
            fmt_num = "{num:02d}"
        elif self.page_count > 100:
            fmt_num = "{num:003d}"

        return fmt_num.format(
            num=int(self.page_num)
        )
