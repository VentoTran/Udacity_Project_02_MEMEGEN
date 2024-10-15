

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
        """ ! This should be implement in children class ! """
        print("You should not reach here... Missing implement somewhere!!")
        pass
    #enddef

#endclass


class Ingestor(IngestorInterface):
    """ Main Class """

    extension_ingestor_list = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        file_extension = path.split('.')[-1]
        subclass_set = set(cls.__base__.__subclasses__())
        for subclass in subclass_set:
            if file_extension in subclass.extension_ingestor_list:
                return True
            #endif
        #endfor
        return False
    #enddef

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        file_extension = path.split('.')[-1]
        subclass_set = set(cls.__base__.__subclasses__())
        for subclass in subclass_set:
            if file_extension in subclass.extension_ingestor_list:
                return subclass.parse(path)
            #endif
        #endfor
        return None
    #enddef

#endclass