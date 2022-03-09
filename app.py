from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
from local_file_queries import main

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')
   data = main()

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = data)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()