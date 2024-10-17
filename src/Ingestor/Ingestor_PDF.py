"""
PDF type Ingestor.

Ingestor for PDF extension file.
"""
from typing import List
from QuoteEngine import QuoteModel
from .Ingestor import IngestorInterface

import subprocess
import os

# TASK DONE


class PDF_Ingestor(IngestorInterface):
    """Support module to read PDF file."""

    extension_ingestor_list = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """PDF Reader."""
        quotes = []

        # Temporary place to load PDF content
        # Will be delete when this func end
        tmp_pdf2text_path = "pdf2text.txt"

        # Use subprocess to run the pdftotext command
        subprocess.run(["pdftotext", "-layout", path, tmp_pdf2text_path])

        pdf2text = open(tmp_pdf2text_path, "r")
        for line in pdf2text:
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(quote)
            # endif
        # endfor

        # Remember to close/delete all temporary file !!!
        pdf2text.close()
        os.remove(tmp_pdf2text_path)

        return quotes
    # enddef

# endclass
