from flask import Flask, render_template, request
from models import db
from forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/showcase'
db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "development-key"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	form = SignupForm()

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html', form=form)
		else:
			return "Success!"

	elif request.method == 'GET':
		return render_template("signup.html", form=form)

@app.route("/music")
def music():
	return render_template("music.html")

@app.route("/dance")
def dance():
	return render_template("dance.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/charttoppers")
def charttoppers():
	return render_template("charttoppers.html")

if __name__ == "__main__":
	app.run(debug=True)