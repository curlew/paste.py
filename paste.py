#!/usr/bin/env python3

import requests
import sys
import yaml

URL = "https://pastebin.com/api/api_post.php"

def main():
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
            api_key = config["api_key"]
    except Exception as e:
        print(e)
        sys.exit(1)

    try:
        text = sys.stdin.read()
    except KeyboardInterrupt:
        return

    paste = {
        "api_dev_key": api_key,
        "api_option": "paste",
        "api_paste_code": text,
    }
    r = requests.post(URL, paste)
    print(r.content.decode())

if __name__ == "__main__":
    main()
