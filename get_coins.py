from autoscraper import AutoScraper

scraper = AutoScraper()

scraper.load('coins_scraper')


def get_coin_value(url):
    return scraper.get_result_exact(url)



coins = ['BTC', 'DOGE', 'ETH', 'BAT', 'XMR']

for coin in coins:
    url = f'https://finance.yahoo.com/quote/{coin}-USD'
    coin_value = get_coin_value(url)
    print(f'{coin} : {coin_value[0]}')


