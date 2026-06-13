from collections import Counter


class DuplicateDetector:

    @staticmethod
    def find_duplicates(items):

        counter = Counter(items)

        duplicates = {}

        for item, count in counter.items():

            if count > 1:

                duplicates[item] = count

        return duplicates   