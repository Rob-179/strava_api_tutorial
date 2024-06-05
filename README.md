.gitignore ignores the .env file and the virtual environment
with that, the client ID and secret are stored within the
-the .env file so that they're never out in the open

load_dotenv() needs to be run to start it and then--
os.getenv gets the referenced env variable
