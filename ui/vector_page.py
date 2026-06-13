import streamlit as st

from services.upload_service import (
    UploadService
)

from services.vector_service import (
    VectorService
)


def render_vector_page():

    st.header(
        "Vector Database"
    )

    pdf_files = (
        UploadService.get_uploaded_files()
    )

    if not pdf_files:

        st.warning(
            "Please upload PDF first."
        )

        return

    selected_pdf = st.selectbox(
        "Select PDF For Embedding",
        pdf_files,
        key="vector_pdf_unique"
    )

    if st.button(
        "Generate Embeddings"
    ):

        with st.spinner(
            "Creating Vector Database..."
        ):

            VectorService.create_embeddings(
                selected_pdf
            )

        st.success(
            "Embeddings Created Successfully"
        )

        st.info(
            "Stored in ChromaDB"
        )