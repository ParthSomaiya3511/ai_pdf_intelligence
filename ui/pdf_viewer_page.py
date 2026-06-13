import streamlit as st

from services.upload_service import (
    UploadService
)

from services.pdf_service import (
    PDFService
)


def render_pdf_viewer():

    st.header(
        "Advanced PDF Viewer"
    )

    pdf_files = (
        UploadService
        .get_uploaded_files()
    )

    if not pdf_files:

        st.warning(
            "Upload PDF first"
        )

        return

    selected_pdf = st.selectbox(
        "Select PDF",
        pdf_files,
        key="advanced_pdf_viewer"
    )

    data = PDFService.load_pdf(
        selected_pdf
    )

    st.metric(
        "Pages",
        data["pages"]
    )

    search_text = st.text_input(
        "Find In PDF",
        key="pdf_find_text"
    )

    content = (
        data["text"]
    )

    if search_text:

        content = content.replace(
            search_text,
            f"[FOUND:{search_text}]"
        )

    st.text_area(
        "PDF Preview",
        content[:15000],
        height=700
    )