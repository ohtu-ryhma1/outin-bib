import os


class FileApi:
    def get_latest_file(self, directory: str) -> str:
        files = [os.path.join(directory, f) for f in os.listdir(directory)]
        latest_file = max(files, key=os.path.getctime)
        return latest_file


file_api = FileApi
