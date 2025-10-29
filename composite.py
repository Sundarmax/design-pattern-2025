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

class File(FileSystemComponent):

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        # print(f"size of file - > {self.size}")
        return  self.size

    def delete(self):
        print(f"Deleting the file - > {self.name}")

    def show_details(self):
        print(f"file name: {self.name} and file size : {self.size}")

class Folder(FileSystemComponent):

    def __init__(self, name):
        self.name = name
        self.children = []

    def add_item(self, name):
        self.children.append(name)
        print("Item added")

    def get_size(self):
        total = 0
        for file in self.children:
            print(file.__dict__)
            total += file.get_size()
        print("Total size",total)

    def delete(self):
        if self.children:
            for file in self.children:
                file.delete()
        print("Folder deleted", self.name)

    def show_details(self):
        if self.children:
            for file in self.children:
                print(f"file name : {file.name} and file size  {file.get_size()}")



if __name__ == "__main__":

    newfile = File("sundar",1)
    newfile.get_size()
    newfile.show_details()
    newfile.delete()
    newfile2 = File("max",2)

    newfolder = Folder("docs")
    newfolder.add_item(newfile)
    newfolder.add_item(newfile2)
    newfolder.get_size()
    newfolder.show_details()