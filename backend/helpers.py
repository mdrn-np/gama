from urllib.parse import urlparse

def get_domain_name(url: str) -> str:
    if not url.startswith('http'):
        url = 'http://' + url
    parsed_url = urlparse(url)
    domain_name = "{uri.netloc}".format(uri=parsed_url)
    return domain_name