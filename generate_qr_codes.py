# -*- coding: utf-8 -*-

import os
import qrcode
import yaml


BASE_URL = "https://baml.ink/"
HERE = os.path.abspath(os.path.dirname(__file__))

def main():
    fp = os.path.join(HERE, 'baml.yaml')
    config = yaml.safe_load(open(fp))
    for short_name, url in config['urls'].items():
        short_url = BASE_URL + short_name
        img = qrcode.make(short_url)
        img_filepath = os.path.join(HERE, "qr", short_name + ".png")
        print(f"Writing qr code for {short_url} to {img_filepath}")
        img.save(img_filepath)

if __name__ == "__main__":
    main()
