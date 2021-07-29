from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/organizer_form", methods=["GET", "POST"])
def form():
	"""Input purpose of going to form"""

	# User reached route via POST (as by submitting a form via POST)
	if request.method == "POST":

		# Ensure user has typed in name
		if not request.form.get("name") or not request.frm.get("purpose"):
			return apology()





