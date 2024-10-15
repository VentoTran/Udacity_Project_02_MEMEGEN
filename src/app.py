import random
import os
import requests
from flask import Flask, render_template, abort, request

# Task DONE
from Ingestor.Ingestor import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')

def setup():
    """ Load all resources """

    quote_files =  ['./_data/DogQuotes/DogQuotesTXT.txt',
                    './_data/DogQuotes/DogQuotesDOCX.docx',
                    './_data/DogQuotes/DogQuotesPDF.pdf',
                    './_data/DogQuotes/DogQuotesCSV.csv']

    # Task DONE
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))
    #endfor

    for each in quotes:
        print(each)
    #endfor

    images_path = "./_data/photos/dog/"

    # Task DONE
    imgs = []
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, image) for image in files]
    #endfor

    return quotes, imgs
#enddef

quotes, imgs = setup()

print("End DONE")
exit()

@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = None
    quote = None
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)
#enddef


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')
#enddef

@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template('meme.html', path=path)
#enddef

if __name__ == "__main__":
    app.run()
#endif
