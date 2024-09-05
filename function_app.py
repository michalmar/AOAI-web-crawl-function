import azure.functions as func
import logging

from crawl_utils import main as crawl

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

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
    url = "https://www.rigassatiksme.lv/lv/biletes/"
    # Base URL is the domain name of the website. For example: https://www.example.com to crawl only this domain.
    base = "https://www.rigassatiksme.lv/lv/"
    crawl(url, base)

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )