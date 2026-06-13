import re


class SequenceDetector:

    @staticmethod
    def find_missing_numbers(text):

        numbers = re.findall(
            r'\d+',
            text
        )

        numbers = sorted(
            set(
                map(int, numbers)
            )
        )

        missing = []

        for i in range(
            len(numbers) - 1
        ):

            current_num = numbers[i]

            next_num = numbers[i + 1]

            if next_num > current_num + 1:

                for value in range(
                    current_num + 1,
                    next_num
                ):
                    missing.append(value)

        return missing[:100]