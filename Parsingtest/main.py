import requests

cookies = {
    'PHPSESSID': '1qnv1bu5gd4f2qvkc3khehvts5',
    '_csrf': 'e38089f25d7bfb4f911a4461c5b35516df7d9c6c945cd60389d162ef6d38695ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22ZezJ0Cc4t8BrnZkBauCxwy92s8EQbTx9%22%3B%7D',
    '_gcl_aw': 'GCL.1678303881.cj0kcqiagaggbhc8arisaaaylfgmucdkdpeunjpdkllu1q0gsyfyo7one5r7xg6e0fuohukratlsvx8aangzealw_wcb',
    '_gcl_au': '1.1.122815489.1678303267',
    '_ga_JWPW0MM28G': 'GS1.1.1678303267.1.1.1678304057.0.0.0',
    '_ga': 'GA1.2.1775894618.1678303267',
    'astratop': '1',
    '_gid': 'GA1.2.771472258.1678303270',
    '_gac_UA-27923957-1': '1.1678303881.cj0kcqiagaggbhc8arisaaaylfgmucdkdpeunjpdkllu1q0gsyfyo7one5r7xg6e0fuohukratlsvx8aangzealw_wcb',
    '_ym_uid': '1678303270412336275',
    '_ym_d': '1678303270',
    '_ym_visorc': 'w',
    '_ym_isad': '2',
    '_gat_UA-27923957-1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.kivano.kg/?gclid=cj0kcqiagaggbhc8arisaaaylfgmucdkdpeunjpdkllu1q0gsyfyo7one5r7xg6e0fuohukratlsvx8aangzealw_wcb',
    'Alt-Used': 'www.kivano.kg',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=1qnv1bu5gd4f2qvkc3khehvts5; _csrf=e38089f25d7bfb4f911a4461c5b35516df7d9c6c945cd60389d162ef6d38695ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22ZezJ0Cc4t8BrnZkBauCxwy92s8EQbTx9%22%3B%7D; _gcl_aw=GCL.1678303881.cj0kcqiagaggbhc8arisaaaylfgmucdkdpeunjpdkllu1q0gsyfyo7one5r7xg6e0fuohukratlsvx8aangzealw_wcb; _gcl_au=1.1.122815489.1678303267; _ga_JWPW0MM28G=GS1.1.1678303267.1.1.1678304057.0.0.0; _ga=GA1.2.1775894618.1678303267; astratop=1; _gid=GA1.2.771472258.1678303270; _gac_UA-27923957-1=1.1678303881.cj0kcqiagaggbhc8arisaaaylfgmucdkdpeunjpdkllu1q0gsyfyo7one5r7xg6e0fuohukratlsvx8aangzealw_wcb; _ym_uid=1678303270412336275; _ym_d=1678303270; _ym_visorc=w; _ym_isad=2; _gat_UA-27923957-1=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get(
    'https://www.kivano.kg/planshety',
    cookies=cookies,
    headers=headers)

with open('result.html', 'w') as file:
    file.write(response.text)
