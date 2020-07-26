import os
import logging

from mglib.runcmd import run

logger = logging.getLogger(__name__)


def resize_img(page_path, media_root):

    local_abspath = os.path.join(
        media_root,
        page_path.document_path.url()
    )
    logger.debug(f"Resizing image {page_path.img_url()}")

    ppmroot = os.path.join(media_root, page_path.ppmroot)
    ppmroot_dirname = os.path.dirname(ppmroot)

    width = page_path.step.width

    if not os.path.exists(ppmroot_dirname):
        logger.debug(f"PPMROOT {ppmroot_dirname} does not exists. Creating.")
        os.makedirs(
            ppmroot_dirname, exist_ok=True
        )
    else:
        logger.debug(f"PPMROOT {ppmroot_dirname} already exists.")

    cmd = (
        "convert",
        "-resize",
        f"{width}x",
        local_abspath,
        # output directory path, similar to ppmroot
        f"{ppmroot}-1.jpg"
    )

    run(cmd)


def extract_img(page_path, media_root):

    local_abspath = os.path.join(
        media_root,
        page_path.document_path.url()
    )
    logger.debug(f"Extracing image for {page_path.img_url()}")

    ppmroot = os.path.join(media_root, page_path.ppmroot)
    ppmroot_dirname = os.path.dirname(ppmroot)

    page_num = page_path.page_num
    width = page_path.step.width

    if not os.path.exists(ppmroot_dirname):
        logger.debug(f"PPMROOT {ppmroot_dirname} does not exists. Creating.")
        os.makedirs(
            ppmroot_dirname, exist_ok=True
        )
    else:
        logger.debug(f"PPMROOT {ppmroot_dirname} already exists.")
    cmd = (
        "pdftoppm",
        "-jpeg",
        "-f",
        str(page_num),
        "-l",  # generate only one page
        str(page_num),
        "-scale-to-x",
        str(width),
        "-scale-to-y",
        "-1",  # it will adjust height according to img ratio
        local_abspath,
        # output directory path,
        ppmroot
    )

    run(cmd)


def extract_hocr(page_url, lang, media_root):
    page_abspath = os.path.join(
        media_root,
        page_url.img_url()
    )

    hocr_root, hocr_ext = os.path.splitext(
        os.path.join(media_root, page_url.hocr_url())
    )
    cmd = (
        "tesseract",
        "-l",
        lang,
        page_abspath,
        hocr_root,
        "hocr"
    )
    run(cmd)
    logger.debug(f"OCR for {page_url.img_url()} - Complete.")
    logger.debug(f"OCR Result {page_url.hocr_url()}.")


def extract_txt(page_url, lang, media_root):
    page_abspath = os.path.join(
        media_root,
        page_url.img_url()
    )
    txt_root, txt_ext = os.path.splitext(
        os.path.join(
            media_root, page_url.txt_url()
        )
    )
    cmd = (
        "tesseract",
        "-l",
        lang,
        page_abspath,
        txt_root
    )
    run(cmd)


#def text_from_pdf(filepath, lang, dry_run=False):
#
#    # suffix .tiff in file name is required by conver utility, otherwise
#    # it won't convert to tiff format!
#    tiff = tempfile.NamedTemporaryFile(suffix=".tiff")
#    conv = convert.Convert(dry_run=dry_run)
#    conv(filepath=filepath, fout=tiff)
#    try:
#        tsact = tesseract.Tesseract()
#        text = tsact(filepath=tiff.name, lang=lang)
#    except subprocess.CalledProcessError as e:
#        print(e)
#        print(e.stderr)
#        return
#
#    return text
#
#
#def text_from_image(filepath, lang, dry_run=False):
#
#    tsact = tesseract.Tesseract(dry_run=dry_run)
#    text = tsact(filepath=filepath, lang=lang)
#
#    return text
#
