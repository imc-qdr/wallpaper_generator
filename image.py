from PIL import Image, ImageFont, ImageDraw
from pexels_api import API
import random as rn
import requests as req
from io import BytesIO
import textwrap
import json


def get_pic(topic):
    with open("pexel_key.json") as key:
        api_key = json.load(key)['key']
    api = API(api_key)
    pics = api.search(topic, results_per_page=40)
    num_pages = pics['total_results']//pics['per_page']
    api.search(topic, page=rn.randint(1, num_pages))
    wallpapers = filter(lambda x: 1.4 < x.width/x.height < 1.9, api.get_entries())
    return rn.choice(list(wallpapers)).original


def quote_container(pic_size, text_size, rows):
    w, h = text_size
    rec = Image.new('RGBA', pic_size, (0, 0, 0, 0))
    rec_draw = ImageDraw.Draw(rec)
    rec_draw.rectangle([pic_size[0] // 4, pic_size[1] // 2 - (h * (rows / 2)) - h,
                        3 * pic_size[0] // 4, pic_size[1] // 2 + (h * (rows / 2)) + h * 1.8], fill=(255, 255, 255, 60))
    return rec, rec_draw


def add_quote(pic_obj, text):
    quote, author = text
    text = textwrap.wrap(quote, width=33) + [author]
    img_data = BytesIO(req.get(pic_obj).content)
    img_obj = Image.open(img_data).convert("RGBA")
    pic_w, pic_h = img_obj.width, img_obj.height
    font = ImageFont.truetype(r'files\GOTHIC.TTF', img_obj.height//25)
    draw = ImageDraw.Draw(img_obj)
    w, h = draw.textsize(text[0], font=font)
    rec, rec_draw = quote_container((pic_w, pic_h), (w, h), len(text))
    current_y = (pic_h/2) - ((len(text)/2) * h) - (len(text) * 5)
    for line in range(len(text)):
        if line == len(text) - 1:
            font = ImageFont.truetype(r'files\GOTHIC.TTF', pic_h//30)
        w = rec_draw.textsize(text[line], font=font)[0]
        rec_draw.text((pic_w/2 - w/2, current_y), text[line], font=font, fill=(20, 20, 20))
        current_y += h + 10
    img_obj = Image.alpha_composite(img_obj, rec)
    if __name__ == '__main__':
        img_obj.show()
    return img_obj.convert("RGB")


if __name__ == '__main__':
    add_quote(get_pic('galaxy'), 'it feels good when it works. -Abdulkader')
