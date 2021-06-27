from autoscraper import AutoScraper

url = 'https://finance.yahoo.com/quote/BTC-USD'

wanted_list = ['32,680.82']

scraper = AutoScraper()
scraper.build(url, wanted_list)


print(scraper.get_result_exact('https://finance.yahoo.com/quote/BTC-USD'))


scraper.save('coins_scraper')

