import json

from pprint import pprint
from octopus import Octopus


def create_request(urls):
    data = []

    otto = Octopus(
           concurrency=4, auto_start=True, cache=True, expiration_in_seconds=3
    )

    def handle_url_response(url, response):
        if "Not found" == response.text:
            print ("URL Not Found: %s" % url)
        else:
            data.append(response.text)

    otto.wait()

    json_data = json.JSONEncoder(indent=None,
                                 separators=(',', ': ')).encode(data)

    return pprint(json_data)


print(create_request(['http://www.mocky.io/v2/5ea8d84f2d0000c54d3a412b']))



