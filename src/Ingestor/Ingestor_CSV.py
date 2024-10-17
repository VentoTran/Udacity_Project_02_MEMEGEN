"""
CSV type Ingestor.

Ingestor for CSV extension file.
"""
from typing import List
from QuoteEngine import QuoteModel
from .Ingestor import IngestorInterface

import pandas

# TASK DONE


class CSV_Ingestor(IngestorInterface):
    """Support module to read CSV file."""

    extension_ingestor_list = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """CSV Reader."""
        quotes = []
        csv_line = pandas.read_csv(path)

        for _, row in csv_line.iterrows():
            quote = QuoteModel('"' + row['body'] + '"', row['author'])
            quotes.append(quote)
        # endfor

        return quotes
    # enddef

# endclass
