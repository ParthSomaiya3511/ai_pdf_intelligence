import fitz


class PDFHighlighter:

    @staticmethod
    def highlight_text(
        pdf_path,
        search_text,
        output_path
    ):

        doc = fitz.open(pdf_path)

        for page in doc:

            matches = page.search_for(
                search_text
            )

            for inst in matches:

                highlight = (
                    page.add_highlight_annot(
                        inst
                    )
                )

                highlight.update()

        doc.save(
            output_path
        )

        doc.close()

        return output_path