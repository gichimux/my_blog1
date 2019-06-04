import urllib.request,json
from .models import Quote

#Getting apikey
base_url = None

def configure_request(app):
  global base_url
  base_url = app.config['QUOTES_API_BASE_URL']

def get_quote():
  '''
  Function that get the json response to our url request
  '''
  get_quote_url = base_url.format()
  with urllib.request.urlopen(get_quote_url) as url:
    get_quote_data = url.read()
    get_quote_response = json.loads(get_quote_data)

    random_quote = None

    if get_quote_response:
      new_quote =  get_quote_response
      random_quote = process_quote(new_quote)

  return random_quote

def process_quote(quote):
  '''
  Function that proces the quote source to an object
  '''
  id = quote.get('id')
  author = quote.get('author')
  quote = quote.get('quote')

  quote_object = Quote(id,author,quote)

  return quote_object