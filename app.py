from flask import Flask, render_template, request, redirect
import shortuuid

app = Flask(__name__)

# In-memory dictionary to store short URLs
url_mapping = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['original_url']
    short_url = shortuuid.uuid()[:8]  # Generate a short code using shortuuid
    url_mapping[short_url] = original_url
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return render_template('index.html', error='Short URL not found')

if __name__ == '__main__':
    app.run(debug=True)
