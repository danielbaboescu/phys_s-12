from flask import Flask, redirect, render_template, url_for, request
import sqlite3
from flask_mail import Mail, Message
from secret import MAIL_DEFAULT_SENDER, MAIL_PASSWORD, MAIL_USERNAME

app = Flask(__main__)
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
mail = Mail(app)

db = SQL("sqlite:/organizerform.db")

@app.route("/organizer_form1", methods=["GET", "POST"])
def form1():
	"""Input purpose of going to form"""

	# User reached route via POST (as by submitting a form via POST)
	if request.method == "POST":

		# Ensure user has typed in name
		if not request.form.get("name") or not request.form.get("purpose"):
			return apology()

		session["name_id"] = rows[0]["id"]

	return redirect(url_for("form2"))

	else:
		return render_template("organizer_form1.html")

@app.route("/organizer_form2", method=["GET", "POST"])
def form2():
	"""Input tools and quantity"""
	if request.method == "POST":

		# Ensure user has selected tool
		if not request.form.get("tool")
			return apology()

	else:
		return render_template("organizer_form2.html") 


if __name__ == "__main__":
	app.run()




