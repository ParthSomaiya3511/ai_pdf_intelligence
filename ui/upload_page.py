import streamlit as st

from services.upload_service import UploadService


def render_upload():

    st.header("📄 Upload PDF Documents")

    uploaded_files = st.file_uploader(
        "Choose PDF Files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        for file in uploaded_files:

            UploadService.save_file(file)

        st.success(
            f"{len(uploaded_files)} PDF file(s) uploaded successfully."
        )

    st.divider()

    st.subheader("Uploaded PDFs")

    pdf_files = UploadService.get_uploaded_files()

    if pdf_files:

        for pdf in pdf_files:
            st.write(f"📄 {pdf}")

    else:
        st.info("No PDF files uploaded yet.")