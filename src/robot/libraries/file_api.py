import os


class FileApi:
    def get_latest_exported_file_path(self, directory: str) -> str:
        files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.endswith(".bib")
        ]
        latest_file = max(files, key=os.path.getctime)
        return latest_file


file_api = FileApi
