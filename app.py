from flask import Flask, render_template, request
from fetch_tweets import get_recent_tweets
from analyze_sentiment import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        tweets = get_recent_tweets(query)
        results = [{"text": t, "sentiment": analyze_sentiment(t)} for t in tweets]
        return render_template("results.html", query=query, results=results)
    return render_template("index.html")

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)