"""
Main Script Body.

Full Process of the Project.
"""
import random
import os
import requests
from flask import Flask, render_template, request

# TASK DONE
from Ingestor.Ingestor import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TASK DONE
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))
    # endfor

    images_path = "./_data/photos/dog/"

    # TASK DONE
    imgs = []
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, image) for image in files]
    # endfor

    return quotes, imgs
# enddef


quotes, images = setup()

# ========================== APP ==========================

# TASK DONE


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(images)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)
# enddef


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')
# enddef

# TASK DONE


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    if not request.form["image_url"]:
        return render_template('meme_form.html')
    # endif

    image_url = request.form["image_url"]
    try:
        received_image_byte = requests.get(image_url, verify=False)
        tmp_file = './temp_image.png'
        open(tmp_file, 'wb').write(received_image_byte.content)
    except Exception:
        print("Bad Image URL")
        return render_template('meme_form.html')
    # endtrycatch

    body = request.form["body"]
    author = request.form["author"]

    path = meme.make_meme(tmp_file, body, author)

    # Remember to delete tmp file !!!
    os.remove(tmp_file)

    return render_template('meme.html', path=path)
# enddef


if __name__ == "__main__":
    app.run()
# endif
