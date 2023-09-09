from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """
    Abstract base class for actual Ingestor classes for different types of files.

    Each child class will actually ingest the files and return the desired data.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check whether path(file) is applicable for each ingestor class."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method for parsing each type of file."""
        pass
