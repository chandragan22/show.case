from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

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