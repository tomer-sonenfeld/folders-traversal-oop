
class File:
    def __init__(self, path: str):
        self._path = path

    def open(self):
        print("opening file...")

    def write(self, content: str):
        print(f"writing_to_file: {content}")

    def close(self):
        print("closing file...")


if __name__ == "__main__":
    _file = File('some/path/to/file')
    _file.open()
    _file.write('some-content')
    _file.close()