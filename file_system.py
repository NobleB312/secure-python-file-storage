import os


class File:
    """Represents a file, allowing for read and write operations."""

    def __init__(self, path):
        self.path = path

    def write(self, data):
        """Writes data to the file."""
        with open(self.path, 'w') as file:
            file.write(data)

    def read(self):
        """Reads and returns the content of the file."""
        with open(self.path, 'r') as file:
            return file.read()


class Directory:
    """Represents a directory, providing methods to interact with it."""

    def __init__(self, path):
        self.path = path

    def create(self):
        """Creates the directory."""
        os.makedirs(self.path, exist_ok=True)

    def list_files(self):
        """Lists all files in the directory and its subdirectories."""
        files = []
        for dirpath, _, filenames in os.walk(self.path):
            for filename in filenames:
                files.append(os.path.join(dirpath, filename))
        return files

    def search_file(self, filename):
        """Searches for files with a given name in the directory."""
        found_files = []
        for dirpath, _, filenames in os.walk(self.path):
            if filename in filenames:
                found_files.append(os.path.join(dirpath, filename))
        return found_files


class FileSystem:
    """Represents the entire file system, with methods to manipulate files and directories."""

    def __init__(self, root):
        self.root = Directory(root)

    def create_file(self, path):
        """Creates an empty file at the specified path."""
        File(path).write('')

    def create_directory(self, path):
        """Creates a new directory at the specified path."""
        Directory(path).create()

    def list_files(self, path):
        """Lists all files in the specified directory."""
        return Directory(path).list_files()

    def insert_file(self, file_path, data):
        """Inserts a file with the given data at the specified path."""
        directory_path = os.path.dirname(file_path)
        Directory(directory_path).create()
        File(file_path).write(data)

    def view_directory(self, path):
        """Prints the contents of the specified directory."""
        print(f"Listing contents of directory: {path}")
        for file_path in self.list_files(path):
            print(file_path)

    def search_file(self, filename, target_directory=None):
        """Searches for a file in the specified directory or the entire file system."""
        if target_directory:
            return Directory(target_directory).search_file(filename)
        else:
            return self.root.search_file(filename)


if __name__ == '__main__':
    # Main interaction with the file system
    root_path = input("Enter root directory path: ")
    fs = FileSystem(root_path)

    file_path = input("Enter file path: ")
    data = input("Enter data to write to file: ")
    fs.insert_file(file_path, data)

    fs.view_directory(root_path)

    file_to_search = input("Enter file name to search: ")
    target_directory = input("Enter directory to search in (optional): ")
    found_files = fs.search_file(file_to_search, target_directory)

    if not found_files:
        print("No files found.")
    else:
        print("Found files:")
        for path in found_files:
            print(path)
