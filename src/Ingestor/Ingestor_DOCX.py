
from typing import List
from QuoteEngine import QuoteModel
from .Ingestor import IngestorInterface

import docx

class DOC_Ingestor(IngestorInterface):
    """ Support module to read DOCX file """

    extension_ingestor_list = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ This is the implementation of the DOCX Reader """

        quotes = []

        docx_file = docx.Document(path)
        for paragraph in docx_file.paragraphs:
            if paragraph.text != "":
                parsed = paragraph.text.split(' - ')
                quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(quote)
            #endif
        #endfor

        return quotes
    #enddef

#endclass

