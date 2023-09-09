from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess
import random
import os

class PDFImporter(IngestorInterface):
    """Helper module to read PDF files and extract quotes.

    This class provides methods to ingest data from PDF files and extract quotes. It inherits from the
    IngestorInterface abstract base class.

    Attributes:
        allowed_extensions (list): A list of allowed file extensions for PDF files ('pdf').

    Methods:
        parse(cls, path: str) -> List[QuoteModel]: Parse a PDF file and return a list of QuoteModel objects.

    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a PDF file and return a list of QuoteModel objects.

        Args:
            cls: The class itself.
            path (str): The path to the PDF file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing the extracted quotes.

        Raises:
            Exception: If the file does not have a valid extension.

        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
        try:
            subprocess.call(['pdftotext', '-layout', path, tmp])
            with open(tmp, "r") as file_ref:
                for line in file_ref:
                    line = line.strip('\n\r').strip()
                    if line:
                        parsed = line.split('-')
                        new_quote = QuoteModel(parsed[0].strip().strip('"'), parsed[1].strip())
                        quotes.append(new_quote)
        finally:
            os.remove(tmp)

        return quotes
