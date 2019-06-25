import requests
from auth import get_token

if __name__ == "__main__":
    print(get_token('admin'))