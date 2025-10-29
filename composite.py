from abc import  ABC,abstractmethod

# component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def get_size(self):
        pass
    @abstractmethod
    def delete(self):
        pass
    @abstractmethod
    def show_details(self):
        pass

class File:
    pass

class Folder:
    pass
