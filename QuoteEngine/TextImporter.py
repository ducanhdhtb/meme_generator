from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextImporter(IngestorInterface):
    """Helper class to read text files and extract quotes.

    This class provides methods to ingest data from text files and extract quotes. It inherits from the
    IngestorInterface abstract base class.

    Attributes:
        allowed_extensions (list): A list of allowed file extensions for text files ('txt').

    Methods:
        parse(cls, path: str) -> List[QuoteModel]: Parse a text file and return a list of QuoteModel objects.

    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a text file and return a list of QuoteModel objects.

        Args:
            cls: The class itself.
            path (str): The path to the text file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing the extracted quotes.

        Raises:
            Exception: If the file does not have a valid extension.

        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []

        with open(path, 'r') as file_ref:
            for line in file_ref:
                parts = line.split("-")
                if len(parts) == 2:
                    body = parts[0].strip().strip('"')
                    author = parts[1].strip()
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)

        return quotes
