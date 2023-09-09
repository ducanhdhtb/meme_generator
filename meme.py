import os
import random
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
import argparse

def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path, body, and author."""
    images = "./_data/photos/dog/"
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    if path is None:
        img = random.choice([os.path.join(root, name) for root, dirs, files in os.walk(images) for name in files])
    else:
        img = path[0]

    if body is None:
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    generated_path = meme.make_meme(img, quote.body, quote.author)
    return generated_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate meme!!')
    parser.add_argument('--body', type=str, default=None, help="text to be displayed")
    parser.add_argument('--author', type=str, default=None, help="author of the text")
    parser.add_argument('--path', type=str, default=None, help="file path for background image")

    args = parser.parse_args()
    generated_path = generate_meme(args.path, args.body, args.author)
    print(f"Meme generated at '{generated_path}'")
