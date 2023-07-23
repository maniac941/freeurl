from flask import Flask,render_template,request
import pyshorteners

app = Flask(__name__)
app.secret_key = "#Enter your own secret_key"


class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def shorten_url(self, url):
        shortened_url = self.shortener.tinyurl.short(url)
        return shortened_url

url_shortener = URLShortener()


@app.route('/',methods=["GET","POST"])
def urlapp():
    if request.method == "POST":
        original_url = request.form['urltoshort']
        shortened_url = url_shortener.shorten_url(original_url)
        
        try:

            return render_template('index.html',shortened_url=shortened_url)
        except:
            return "Enter a Valid link"
        
    return render_template('index.html')




