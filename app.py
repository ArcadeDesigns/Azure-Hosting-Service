from flask import Flask, render_template, flash, request, redirect, url_for
import urllib.request
import uuid as uuid
import os

#create a flask instance
app = Flask(__name__)

#secret key!
app.config['SECRET_KEY'] = "cairocoders-ednalan"


@app.route("/contact")
def contact():
		return render_template("contact.html")

@app.route("/searchengineoptimization")
def searchengineoptimization():
		return render_template("searchengineoptimization.html")

@app.route("/optimization_fullest")
def optimization_fullest():
		return render_template("optimization_fullest.html")

@app.route("/googleadsense")
def googleadsense():
		return render_template("googleadsense.html")

@app.route("/ccpa")
def ccpa():
		return render_template("ccpa.html")

@app.route("/affiliate_marketing")
def affiliate_marketing():
		return render_template("affiliate_marketing.html")

@app.route("/content")
def content():
		return render_template("content.html")

@app.route("/democratic")
def democratic():
		return render_template("democratic.html")

@app.route("/portfolio")
def portfolio():
		return render_template("portfolio.html")

@app.route("/cryptocurrency")
def cryptocurrency():
		return render_template("cryptocurrency.html")

@app.route("/global_prospect")
def global_prospect():
		return render_template("global_prospect.html")

@app.route("/posts")
def posts():
		return render_template("posts.html")

@app.route("/website_development")
def website_development():
		return render_template("construction.html")

@app.route("/dashboard")
def dashboard():
		return render_template("construction.html")

@app.route("/software_programming")
def software_programming():
		return render_template("construction.html")

@app.route("/seo_service")
def seo_service():
		return render_template("construction.html")

@app.route("/backlink")
def backlink():
		return render_template("construction.html")

@app.route("/consulting")
def consulting():
		return render_template("construction.html")

@app.route("/career")
def career():
		return render_template("construction.html")

@app.route("/service")
def service():
		return render_template("service.html")

@app.route("/construction")
def construction():
		return render_template("construction.html")

@app.route("/about")
def about():
		return render_template("about.html")

@app.route("/terms-and-conditions")
def terms_and_conditions():
		return render_template("terms-and-conditions.html")

@app.route("/disclaimer")
def disclaimer():
		return render_template("disclaimer.html")

@app.route("/")
def index():
	return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500