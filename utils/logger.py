import os
import types
import json
import allure
import logging
import datetime
from utils import resource
from curlify import to_curl
from requests import Response

def response_logging(response: Response):
    curl = to_curl(response.request)
    logging.info(to_curl(response.request))
    logging.info("Request: " + response.request.url)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Status code: " + str(response.status_code))
    logging.info("Response: " + response.text)
    logging.debug(to_curl(response.request))
    allure.attach(body=curl, name="curl", attachment_type=allure.attachment_type.TEXT, extension='txt')
    allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                  name="response",
                  attachment_type=allure.attachment_type.JSON,
                  extension='json')