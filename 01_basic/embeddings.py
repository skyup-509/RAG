import requests
from langchain_core.embeddings import Embeddings

class NVIDIAEmbeddingsCustom(Embeddings):

    def __init__(self, api_key, model: str = "nvidia/nemotron-3-embed-1b"):
        self.api_key = api_key
        self.url = "https://integrate.api.nvidia.com/v1/embeddings"
        self.model = model

    def _request(self, texts):
        payload = {
            "model": self.model,
            "encoding_format": "float",
            "truncate": "NONE",
            "input": texts
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(self.url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["data"]

    def embed_documents(self, texts):
        data = self._request(texts)
        return [item["embedding"] for item in data]

    def embed_query(self, text):
        data = self._request([text])
        return data[0]["embedding"]