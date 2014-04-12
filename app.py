from flask import Flask, render_template, request, redirect, url_for
import pymongo


app = Flask(__name__)

#mongodb_uri = 'mongodb://5chackathon:hackweek@ds041367.mongolab.com:41367/hackweek'
#db_name = 'hackweek'
#connection = pymongo.Connection(mongodb_uri)
#db = connection[db_name]


@app.route('/pomona')
def majors():
    return render_template("pomona-full-campus.html")


if __name__ == '__main__':
    app.run(debug=True)
