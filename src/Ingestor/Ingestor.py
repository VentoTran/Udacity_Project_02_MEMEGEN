

from typing import List
from QuoteEngine import QuoteModel


class IngestorInterface:
    """ Base Class """

    extension_ingestor_list = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        file_extension = path.split('.')[-1]
        return file_extension in cls.extension_ingestor_list
    #enddef

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
    #enddef

#endclass


class Ingestor(IngestorInterface):
    """ Main Class """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        pass
    #enddef

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
    #enddef

#endclass