import random
import os
import requests
from flask import Flask, render_template, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)
meme = MemeEngine('./static')

def setup():
    """
    Set up the system and load necessary resources.

    Returns:
        tuple: A tuple containing two lists, consisting of a list of quotes and a list of image file paths.
    """
    images_path = "./_data/photos/dog/"

    """ Load all resources """
    quote_files = ["./_data/DogQuotes/DogQuotesTXT.txt",
                   "./_data/DogQuotes/DogQuotesDOCX.docx",
                   "./_data/DogQuotes/DogQuotesPDF.pdf",
                   "./_data/DogQuotes/DogQuotesCSV.csv"]

    """Load and parse all quote resources."""
    quotes = []
    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file))

    """Load image file paths."""
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs.extend([os.path.join(root, name) for name in files])
    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user-defined meme."""
    image_url = request.form.get("image_url")

    if not image_url:
        return render_template('meme_form.html')

    try:
        response = requests.get(image_url, verify=False)
        if response.status_code == 200:
            tmp = f'./tmp/{random.randint(0, 100000000)}.png'
            with open(tmp, 'wb') as image_file:
                image_file.write(response.content)
        else:
            raise Exception("Bad Image URL")

    except Exception as e:
        print(f"Error: {e}")
        return render_template('meme_form.html')

    body = request.form.get("body")
    author = request.form.get("author")
    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
