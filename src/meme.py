
# TASK DONE
import os
import random
import argparse
import pathlib

from Ingestor.Ingestor import Ingestor
from MemeEngine import MemeEngine
from QuoteEngine import QuoteModel

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        #endfor
        img = random.choice(imgs)
    else:
        img = path[0]
    #endif

    if body is None:
        quote_files =  ['./_data/DogQuotes/DogQuotesTXT.txt',
                        './_data/DogQuotes/DogQuotesDOCX.docx',
                        './_data/DogQuotes/DogQuotesPDF.pdf',
                        './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        #endfor
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
    #endif

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path
#enddef

if __name__ == "__main__":
    # TASK DONE
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=pathlib.Path, default=None, help="Input image file path.")
    parser.add_argument('-b', '--body', type=str, default=None, help="Quote body text.")
    parser.add_argument('-a', '--author', type=str, default=None, help="Quote author.")

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
#endif
