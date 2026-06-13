import json
import os


class SyncService:

    CACHE_FILE = (
        "mobile_cache.json"
    )

    @staticmethod
    def save(
        data
    ):

        with open(
            SyncService.CACHE_FILE,
            "w"
        ) as file:

            json.dump(
                data,
                file
            )

    @staticmethod
    def load():

        if not os.path.exists(
            SyncService.CACHE_FILE
        ):

            return {}

        with open(
            SyncService.CACHE_FILE,
            "r"
        ) as file:

            return json.load(
                file
            )