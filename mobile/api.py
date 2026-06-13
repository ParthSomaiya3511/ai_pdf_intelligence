import requests


class MobileAPI:

    BASE_URL = (
        "http://127.0.0.1:8000"
    )

    @staticmethod
    def search(
        query
    ):

        response = requests.post(
            f"{MobileAPI.BASE_URL}/search/",
            json={
                "query": query
            }
        )

        return response.json()

    @staticmethod
    def chat(
        question
    ):

        response = requests.post(
            f"{MobileAPI.BASE_URL}/chat/",
            json={
                "question": question
            }
        )

        return response.json()