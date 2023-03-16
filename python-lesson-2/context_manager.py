
class File:
    def __init__(self, path: str):
        self._path = path

    def __enter__(self):
        self._open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close()

    def _open(self):
        print("opening file...")

    def write(self, content: str):
        print(f"writing_to_file: {content}")

    def _close(self):
        print("closing file...")



if __name__ == "__main__":
    with File('some/path/to/file') as _file:
        _file.write('some-content')

    print('out of scope')
