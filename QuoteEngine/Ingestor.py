"""Module that encapsulates modules for ingesting different types of files.

This module provides a class `Ingestor` that encapsulates various importer modules
for parsing and extracting data from different file types, including CSV, Docx, PDF, and Text files.

Attributes:
    ingestors (list): A list of available importer classes for different file types.

Methods:
    parse(cls, path): Parse a file at the given path using the appropriate ingestor.

"""

from QuoteEngine.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVImporter import CSVImporter
from .DocxImporter import DocxImporter
from .PDFImporter import PDFImporter
from .TextImporter import TextImporter
from typing import List


class Ingestor(IngestorInterface):
    """Class encapsulating each importer module."""

    ingestors = [CSVImporter, DocxImporter, PDFImporter, TextImporter]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse paths (files) using the appropriate ingestor.

        Args:
            cls: The class itself.
            path (str): The path to the file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing parsed quotes.

        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
