#!/usr/bin/env python3

import argparse
import requests
import sys
import yaml

URL = "https://pastebin.com/api/api_post.php"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name")
    parser.add_argument("-e", "--expire", choices=["10M", "1H", "1D", "1W", "2W", "1M", "6M", "1Y"])
    parser.add_argument("-l", "--language")
    args = parser.parse_args()

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

        "api_paste_name": args.name,
        "api_paste_expire_date": args.expire,
        "api_paste_format": args.language,
    }
    r = requests.post(URL, paste)
    print(r.content.decode())

if __name__ == "__main__":
    main()
