class FolderNotFoundError(Exception):
    def __init__(self, folder_path):
        message = f"Folder not found: {folder_path}"
        super().__init__(message)