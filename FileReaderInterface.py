from abc import ABC, abstractmethod

class FileReaderInterface(ABC):
    @abstractmethod
    def read_file(self, file_path):
        pass

