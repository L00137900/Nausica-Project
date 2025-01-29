"""Basic Flask application for rendering web pages."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page using the 'home.html' template."""
    return render_template("home.html")


@app.route("/about")
def about():
    """Render the about page using the 'about.html' template."""
    return render_template("about.html")

#if __name__ == '__main__':
    #"""Start the app in debug mode."""
    # app.run(debug=True)  # Uncomment for local debugging; comment out for deployment
