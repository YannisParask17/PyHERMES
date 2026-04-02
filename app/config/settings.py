from dotenv import load_dotenv
import os

load_dotenv()

class Credentials:
    """
    Environment variables:

        -Email account credentials, imported from .env file
    """

    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')


credentials = Credentials()