from autoscraper import AutoScraper
from flask import Flask, request

scraper = AutoScraper()

scraper.load('coins_scraper')

app = Flask(__name__)

def get_coins(coin):
    url = f'https://finance.yahoo.com/quote/{coin}-USD'
    result = scraper.get_result_exact(url)
    return result

@app.route('/', methods=['GET'])
def search_api():
    query = request.args.get('coin')
    return dict(result=get_coins(query))


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')



