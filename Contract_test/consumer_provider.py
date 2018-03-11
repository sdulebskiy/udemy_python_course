import requests
import atexit
import time
import unittest
from pact import Consumer, Provider

def generation(generation_id):
    """Fetch a generation by generationid from the server."""
    uri = 'http://maxbill-docker03-dc2.maxbilldev.impello.co.uk:13200/maxbill__billing--sensibility-api/v1/sensibility_result?generationId=' + generation_id
    return requests.get(uri).json()

pact = Consumer('Consumer').has_pact_with(Provider('Provider'),  pact_dir='./pacts')
#
pact.start_service()

atexit.register(pact.stop_service)

class GetUserInfoContract(unittest.TestCase):
  def test_get_user(self):
    expected = {
      'username': 'UserA',
      'id': 123,
      'groups': ['Editors']
    }

    (pact
     .given('UserA exists and is not an administrator')
     .upon_receiving('a request for UserA')
     .with_request('get', '/users/UserA')
     .will_respond_with(200, body=expected))

    with pact:
      result = generation(2178)

    self.assertEqual(result, expected)
