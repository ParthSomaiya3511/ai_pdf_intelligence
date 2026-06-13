import os
import streamlit as st

from core.pdf_highlighter import (
    PDFHighlighter
)


def render_pdf_highlight():

    st.header(
        "PDF Highlight Viewer"
    )

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="highlight_pdf"
    )

    search_text = st.text_input(
        "Search Text",
        key="highlight_search"
    )

    if uploaded_pdf and search_text:

        temp_pdf = (
            f"temp_{uploaded_pdf.name}"
        )

        with open(
            temp_pdf,
            "wb"
        ) as f:

            f.write(
                uploaded_pdf.read()
            )

        output_pdf = (
            f"highlighted_{uploaded_pdf.name}"
        )

        PDFHighlighter.highlight_text(
            temp_pdf,
            search_text,
            output_pdf
        )

        st.success(
            "Highlight Generated"
        )

        with open(
            output_pdf,
            "rb"
        ) as pdf:

            st.download_button(
                "Download Highlighted PDF",
                pdf,
                file_name=output_pdf
            )