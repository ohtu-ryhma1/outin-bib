import requests
import os
import time

class FileExportLibrary:
    def download_reference_file(self, base_url, target_path):
        url = f"{base_url}/export/file"

        response = requests.post(url)
        response.raise_for_status()

        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(target_path, "wb") as f:
            f.write(response.content)
        return os.path.abspath(target_path)

    def file_should_exist(self, path, timeout=10):
        end = time.time() + timeout
        while time.time() < end:
            if os.path.exists(path):
                return True
            time.sleep(0.2)
        raise AssertionError(f"File not found: {path}")

    def get_file_content(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
