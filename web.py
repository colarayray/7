from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 41146635 吳享叡的求職相關資訊</h1>"
    homepage += "<a href=/today>興趣何倫碼測驗結果</a><br>"
    homepage += "<a href=/welcome?nick=tcyang>有興趣的MIS相關工作</a><br>"
    homepage += "<a href=/about>自傳履歷</a><br>"
    return homepage

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html",datetime = str(now))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)


if __name__ == "__main__":
    app.run()
