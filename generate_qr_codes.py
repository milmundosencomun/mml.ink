# -*- coding: utf-8 -*-

import os
import qrcode
import yaml

from PIL import ImageDraw, ImageFont


DOMAIN = "baml.ink/"
HERE = os.path.abspath(os.path.dirname(__file__))

def main():
    fp = os.path.join(HERE, 'baml.yaml')
    config = yaml.safe_load(open(fp))
    for short_name, url in config['urls'].items():
        short_url = DOMAIN + short_name
        img = qrcode.make(f"https://{short_url}")
        img = img.resize((370, 370))
        img_draw = ImageDraw.Draw(img)
        font = ImageFont.load_default(size=16)
        img_draw.text((45, 340), short_url, fill="black", font=font)
        img_filepath = os.path.join(HERE, "qr", short_name + ".png")
        print(f"Writing qr code for {short_url} to {img_filepath}")
        img.save(img_filepath)

if __name__ == "__main__":
    main()
