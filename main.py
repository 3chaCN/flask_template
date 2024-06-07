from flask import Flask
from flask import render_template
from flask import url_for 
import lorem
import about

app = Flask(__name__)

#topmenu = ["index", "about"]
#navitm = {"index" : ["item 1", "item 2", "item 3"], "about":["item 1"]}
#url_for('static', filename='style.css')

menu = [{"caption":"index","href":"http://127.0.0.1:5000/"},{"caption":"about","href":"/about"}]

f = {"author":"Woo"}

topmenu = [menu]

app.config.from_pyfile('config.cfg')

@app.route('/')
def index_page(menubar=None, nav=None, section=None, content=None, footer=None):
    return render_template("view.html", menubar=menu, nav=lorem.navitm, section=lorem.s[0], content=lorem.c[0], footer=f)

@app.route('/about')
def about_page(menubar=None, nav=None, section=None, content=None, footer=None):
    return render_template("view.html", menubar=menu, nav=about.navitm, section=about.s, content=about.c, footer=f)



# define Pager(navbar["lorem", "ipsum"], "title", data[""])
#
# WebPager start from a template "index.html" (html=)
# Next searching for a child named "pname"
# Child page must have {% block body %}{% endblock %} tag
# 

# /status
# /config
# /about (running version, ...)

# /config/[vm1, vm2, ...]
