from services.pdf_service import (
    PDFService
)


class PatternSearch:

    @staticmethod
    def search_in_pdf(
        filename,
        pattern
    ):

        pdf = PDFService.load_pdf(
            filename
        )

        text = pdf["text"]

        results = []

        if not pattern.strip():

            return results

        search_terms = (
            pattern.lower()
            .strip()
            .split()
        )

        lines = text.split(
            "\n"
        )

        for index, line in enumerate(
            lines
        ):

            line_text = (
                line.lower()
            )

            score = sum(
                1
                for term in search_terms
                if term in line_text
            )

            if score > 0:

                results.append(
                    {
                        "line": index + 1,
                        "text": line,
                        "score": score
                    }
                )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results