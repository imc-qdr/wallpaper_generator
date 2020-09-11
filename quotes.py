import requests as rq
from string import ascii_lowercase
import random as rn
import re
import html


def brainy_quotes_random():
    random_chr = rn.choice(ascii_lowercase)
    chr_page = rq.get(f'https://www.brainyquote.com/authors/{random_chr}')
    pages_num = re.findall(fr'/authors/{random_chr}\d', chr_page.text)
    if pages_num:
        max_page = max(pages_num, key=lambda x: int(re.match(r'/authors/[a-z](\d+)', x).group(1)))
        authors_page = rq.get(f'https://www.brainyquote.com{max_page}')
        random_author = rn.choice(re.findall(fr'/authors/{random_chr}[a-z]+-[a-z]+-?[a-z]*',
                                  authors_page.text))
        get_author = rq.get(f'https://www.brainyquote.com{random_author}')
        all_quotes = re.findall('title="view quote">(.+)</a>', html.unescape(get_author.text))
        return rn.choice(all_quotes), f"\n{random_author[9:-7].replace('-', ' ')}"


def brainy_quotes_specific(author):
    get_author = rq.get(f'https://www.brainyquote.com/authors/{author}-quotes')
    pages = re.findall(fr'{author}-quotes_(\d+)"', get_author.text)
    if pages:
        max_page = max(pages, key=int)
        page = rn.randint(1, int(max_page))
        if page > 1:
            get_author = rq.get(f'https://www.brainyquote.com/authors/{author}-quotes_{page}')
    all_quotes = re.findall('title="view quote">(.+)</a>', html.unescape(get_author.text))
    author = ' '.join(map(lambda x: x.capitalize(), author.split('-')))
    return rn.choice(all_quotes), f"\n-{author}"


if __name__ == '__main__':
    print(brainy_quotes_specific('carl-jung'))
