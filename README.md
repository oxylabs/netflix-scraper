# Netflix Scraper

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

Netflix Scraper extracts public data from Netflix on any scale you need.
This quick tutorial will show you how to scrape Netflix with [<u>Oxylabs’
Scraper API</u>]([https://oxylabs.io/products/scraper-api](https://oxylabs.io/products/scraper-api/web/netflix)).

## How it works

You can gather Netflix data by sending a request to our API and
including the Netflix URLs you want to scrape. Our service will send
back the HTML of any Netflix page.

### Python code example

This code sample makes a request to our service, which then renders
JavaScript via a headless browser and retrieves the HTML of a Netflix
page:

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
   'source': 'universal',
   'url': 'https://www.netflix.com/de-en/title/80057281',
   'render': 'html'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'), #Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
```

Visit our
[<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/all-domains)
for more information about payload parameters.

### Output sample

```json
{
  "results": [
    {
      "content": "<!doctype html>\n<html lang=\"en\">\n<head>
      ...
      </script></div>\n</html>\n",
      "created_at": "2023-05-18 12:23:06",
      "updated_at": "2023-05-18 12:23:25",
      "page": 1,
      "url": "https://www.netflix.com/de-en/title/80057281",
      "job_id": "7064938450625018881",
      "status_code": 200
    }
  ]
}
```

Oxylabs’ Netflix Scraper API makes it much easier to collect public
information from Netflix. You can gather details about movies or TV
series, like episode names, descriptions, cast, ratings, similar shows,
etc. You can also monitor pricing plans or the news about subscription
changes. In case you have any questions, you can reach us via [<u>live
chat</u>](https://oxylabs.io/) or
[<u>email</u>](mailto:support@oxylabs.io).

Also, check this tutorial on [pypi](https://pypi.org/project/Netflix-scraper/)
