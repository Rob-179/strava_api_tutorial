from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os
import requests

load_dotenv()

#client_id = os.getenv('CLIENT_ID')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_url = "https://localhost/exchange_token"

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

#found in documentation
auth_base_url = "https://www.strava.com/api/v3/oauth/authorize"
#documentation will show all the scopes
session.scope = ["profile:read_all"]
auth_link = session.authorization_url(auth_base_url)
#click link, get ourselves verified and get a token from the former


print(f"Click here!! {auth_link[0]}")

r = requests.get(auth_link[0])
print(r.url)

#next is starting the exchange process

redirect_response = input("Paste redirect url here: ")

#send token to make exchange
token_url = "https://www.strava.com/api/v3/oauth/token"
session.fetch_token(
  token_url=token_url,
  client_id=client_id,
  client_secret=client_secret,
  authorization_response=redirect_response,
  include_client_id=True
)


response = session.get("https://www.strava.com/api/v3/athlete")

print("\n")
print(f"Reponse Status: {response.status_code}")
print(f"Response Reason: {response.reason}")
print(f"Time Elapsed: {response.elapsed}")
print(f"Response Text: \n{response.text}")
