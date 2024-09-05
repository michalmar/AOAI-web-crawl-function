import azure.functions as func
import logging
import os

from crawl_utils import main as crawl

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

CRAWL_URL = os.getenv("CRAWL_URL")
CRAWL_BASE = os.getenv("CRAWL_BASE")

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # URL is the address of the website you want to crawl. For example: https://www.example.com/some-page/subpage/etc
    url = CRAWL_URL
    # Base URL is the domain name of the website. For example: https://www.example.com to crawl only this domain.
    base = CRAWL_BASE

    processed_pages = 0
    try:
        processed_pages = crawl(url, base)
    except Exception as e:
        return func.HttpResponse(
            f"Failed to crawl {url}. Error: {e}",
            status_code=500
        )

    return func.HttpResponse(
            f"Succesfully crawled {processed_pages} pages from {url} and stored in Azure Storage.",
            status_code=200
    )