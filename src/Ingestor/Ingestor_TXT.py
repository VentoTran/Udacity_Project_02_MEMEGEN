
from typing import List
from QuoteEngine import QuoteModel
from .Ingestor import IngestorInterface

class TXT_Ingestor(IngestorInterface):
    """ Support module to read TXT file """

    extension_ingestor_list = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ This is the implementation of the TXT Reader """

        quotes = []

        txt_file = open(path, "r")
        for line in txt_file.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(quote)
            #endif
        #endfor

        # Remember to close file !!!
        txt_file.close()

        return quotes
    #enddef

#endclass

