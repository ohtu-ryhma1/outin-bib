import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def reset_db(self):
        requests.post(f"{self._base_url}/test/reset-db", timeout=5)

    def create_reference_directly(self, ref_type, ref_key, fields):
        ref_data = {"ref-type-input": ref_type, "ref-key-input": ref_key, **fields}

        requests.post(f"{self._base_url}/new-reference", data=ref_data, timeout=5)


app_library = AppLibrary
