from flask import Flask, render_template # render_template connects python and html

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=False)  #http://localhost:5000/about/
#Press ctrl+C to quit
#PS E:\Python> python .\website.py
#https://www.geeksforgeeks.org/introduction-and-installation-of-heroku-cli-on-windows-machine/
#crtl+R to refresh host webpage to reflect new changes
