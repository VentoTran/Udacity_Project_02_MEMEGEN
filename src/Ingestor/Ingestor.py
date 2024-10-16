"""
Main Ingestor.

Ingestor for all extension file.
"""
from typing import List
from QuoteEngine import QuoteModel

# TASK DONE


class IngestorInterface:
    """Base Class."""

    extension_ingestor_list = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        can_ingest checker return bool.

        Check if extension can be ingested

        :param path: path to file
        :type path: str
        :return: true/false that the file can be handled
        :rtype: bool
        """
        file_extension = path.split('.')[-1]
        return file_extension in cls.extension_ingestor_list
    # enddef

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the input file."""
        """! This should be implement in children class !"""
        print("You should not reach here... Missing implement somewhere!!")
        pass
    # enddef

# endclass

# TASK DONE


class Ingestor(IngestorInterface):
    """Main Class."""

    extension_ingestor_list = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        can_ingest a file.

        Check if extension can be ingested

        :param path: path to file
        :type path: str
        :return: true/false that the file can be handled
        :rtype: bool
        """
        file_extension = path.split('.')[-1]
        subclass_set = set(cls.__base__.__subclasses__())
        for subclass in subclass_set:
            if file_extension in subclass.extension_ingestor_list:
                return True
            # endif
        # endfor
        return False
    # enddef

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the input file.

        Pasre the file to get the Quote[Body, Author]

        :return: a List of Quote
        :rtype: list
        """
        file_extension = path.split('.')[-1]
        subclass_set = set(cls.__base__.__subclasses__())
        for subclass in subclass_set:
            if subclass is Ingestor:
                continue
            # endif
            if file_extension in subclass.extension_ingestor_list:
                return subclass.parse(path)
            # endif
        # endfor
        return None
    # enddef

# endclass
