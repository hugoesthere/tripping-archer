from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

#mongodb_uri = 'mongodb://5chackathon:hackweek@ds041367.mongolab.com:41367/hackweek'
#db_name = 'hackweek'
#connection = pymongo.Connection(mongodb_uri)
#db = connection[db_name]


@app.route('/')
def majors():
    return render_template("homepage.html")

@app.route('/searchbox.html')
def search():
    return render_template("searchbox.html")

@app.route('/pomona-full-campus.html')
def map():
	return render_template("pomona-full-campus.html")

@app.route('/harwood.html')
def harwood():
	return render_template("harwood.html")

@app.route('/hw2e4person.html')
def h2e():
	return render_template("hw2e4person.html")

@app.route('/drawEntry.html')
def draw():
	return render_template("drawEntry.html")



if __name__ == '__main__':
    app.run(debug=True)
