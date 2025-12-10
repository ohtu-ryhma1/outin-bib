import requests


class RepositoryApi:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def reset_db(self):
        requests.post(f"{self._base_url}/test/reset-db", timeout=5)

    def create_reference_via_request(self, ref_type, ref_key, fields):
        ref_data = {"ref-type-select": ref_type, "ref-key-input": ref_key, **fields}

        requests.post(f"{self._base_url}/new-reference", data=ref_data, timeout=5)


repository_api = RepositoryApi
