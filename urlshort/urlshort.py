from flask import render_template,request,redirect,url_for,flash,abort,session,jsonify,Blueprint
import json 
import os.path
# Allows us to check if any file is save or not
# dependency in flask
from werkzeug.utils import secure_filename

bp = Blueprint('urlshort',__name__)

#base url
@bp.route('/')
def home():
    # render_template loads the html pages
    return render_template("home.html",codes=session.keys())
    # html tags works properly
    return "<h1> Hello Flask! </h1>"

# Url and function name need not to be same
@bp.route("/about")
def about():
    return "<center><h1>This is url shortener</h1></center>"

@bp.route("/your-url",methods=["GET","POST"])
def your_url():
    if request.method == "POST":
        urls = {}
        if os.path.exists("urls.json"):
            with open("urls.json") as urls_file:
                urls = json.load(urls_file)
        
        if request.form["code"] in urls.keys():
            flash("That short name has already been taken.Please select another name")
            return redirect(url_for("home"))

        if "url" in request.form.keys():
            urls[request.form["code"]] = {"url":request.form["url"]}
        else:
            f = request.files['file']
            full_name = request.form["code"] + secure_filename(f.filename)
            f.save("C:/Users/piyus/Desktop/url-shortener/static/user_files/"+full_name)
            urls[request.form["code"]] = {"file":full_name}

        
        with open("urls.json","w") as url_file:
            json.dump(urls,url_file)
            # Setting the code to True will save it in the cookies
            session[request.form["code"]] = True
        return render_template("your_url.html",code=request.form['code'])
    else:
        return redirect("/about")
        return redirect(url_for("home"))

# look for a string after the / and store in a variable called code
@bp.route("/<string:code>")
def redirect_to_url(code):
    if os.path.exists("urls.json"):
        with open("urls.json") as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if "url" in urls[code].keys():
                    return redirect(urls[code]["url"])
                else:
                    return redirect(url_for("static",filename="user_files/"+urls[code]['file']))
    #return abort(403)
    return abort(404)


@bp.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"),403


@bp.route("/api")
def session_api():
    # Jsonify takes list/dictionary as input and convert it to json
    return jsonify(list(session.keys()))