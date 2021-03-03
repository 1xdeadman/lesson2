import requests
import os
import hashlib
import typing
import logging


_page_dir = 'pages'


def _check_page_dir() -> bool:
    """
    check, is page dir exist.
    Create new dir if page dir is not existing

    :return:
      True - if dir is existed
      False - if dir is not existed
    """
    if os.path.isdir(_page_dir):
        return True
    os.mkdir(_page_dir)
    logging.info(f'page dir is created')
    return False


def _find_loaded_page(url: str) -> str:
    """
    check, is page with specified url loaded already

    :param url:
      url of the checked page
    :return:
      page's text in str format or empty str if page not founded
    """
    hash_value = hashlib.sha512(url.encode(encoding='utf-8')).hexdigest()
    logging.debug(f'searching page ({url}) with specified hash value ({hash_value})')
    filepath = f"{_page_dir}/{hash_value}"
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            page_text = file.read()
        logging.info(f'page ({url}) was loaded from cache: {hash_value}')
        return page_text
    return ""


def _save_loaded_page(url: str, page_text: str) -> bool:
    try:
        hash_value = hashlib.sha512(url.encode(encoding='utf-8')).hexdigest()
        logging.debug(f'create hash value ({hash_value}) for page: {url}')
        with open(f'{_page_dir}/{hash_value}', 'w', encoding='utf-8') as file:
            file.write(page_text)
        return True
    except Exception as ex:
        logging.error(f'error occurred while write page file: {url}. Exception: {ex}')
        return False


def get_page(url: str) -> str:
    """
    get text of the specified page

    :param url:
      url of the page
    :return:
      page's text in str or empty str
    """

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    _check_page_dir()
    page_text = _find_loaded_page(url)
    if page_text != "":
        return page_text
    try:
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            logging.warning(f'could not find page with specified url: {url}')
            return ""
        _save_loaded_page(url, res.text)
        return res.text
    except Exception as ex:
        logging.error(f'could not load page with specified url: {url}. Exception: {str(ex)}')
        return ""
