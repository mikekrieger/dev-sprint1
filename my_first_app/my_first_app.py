# This is whre you can start you python file for your week1 web app
# Name: Michael Krieger

import flask, flask.views
app = flask.Flask(__name__)

class View(flask.views.MethodView):
	def get(self):
		return "Hello world!"

app.add_url_rule('/', view_func=View.as_view('main'))

app.debug = True
app.run()