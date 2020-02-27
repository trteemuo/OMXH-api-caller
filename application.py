from flask import Flask, flash, render_template
import requests

application = Flask(__name__, template_folder= 'templates')


base_url = 'https://www.nordnet.fi/graph/indicator/HEX/OMXHPI?from=2019-04-12&to=2019-04-12&fields=last'


@application.route('/')
def scrape():
    r = requests.get(base_url)
    if r.status_code == 200:
        value = r.json()[-1]['last']
        val = 9818.042
        if value > val:
            flash(f'Higher than {val} ' + f'({round((value/val-1)*100, 2)} %)')
        return render_template('index.html', value=value)


if __name__ == '__main__':
    application.run(debug = False)
