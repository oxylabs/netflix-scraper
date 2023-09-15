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
