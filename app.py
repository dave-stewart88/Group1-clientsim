from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
from local_file_queries import main
import pandas as pd


@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')
    file = "./food-hygiene-data/belfast-all.csv"
    data = pd.read_csv(file, header=0, usecols=['BusinessName','PostCode', 'BusinessType','RatingValue'])
    data.set_index = (['BusinessName'])
    data.index.name = None
    # print(type(data))
    # business = data.loc[data.BusinessName]
    # rating = data.loc[data.RatingValue]
    test1 = data.loc[(data.BusinessType == 'Retailers - other') & (data.RatingValue == '5')]
    # print(business)
    # print(rating)
    if name:
        print('Request for hello page received with name=%s' % name)
        return render_template('hello.html', name=name, tables=[test1.to_html(classes=['BusinessName, RatingValue'])],
                               data=['na','Rating Table'])
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
