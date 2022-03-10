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
    postCode = request.form.get('postCode')
    file = "./food-hygiene-data/belfast-all.csv"
    data = pd.read_csv(file, header=0, usecols=['BusinessName','PostCode', 'BusinessType','RatingValue'])
    data.set_index = (['BusinessName'])
    data.index.name = None

    information = data.loc[(data.RatingValue == '5')&(data['PostCode'].str.contains(postCode))]
    print(type(information))

    print(information.to_html(classes=['table table-dark']))

    # print(rating)
    if postCode:
        print('Request for hello page received with Post Code=%s' % postCode)
        return render_template('hello.html', tables=[information.to_html(classes=['table table-dark'],index=False,columns=['BusinessName','PostCode','RatingValue'],justify='left')],
                               data=['na','Rating Table'])
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
