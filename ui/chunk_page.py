import streamlit as st

from services.upload_service import (
    UploadService
)

from services.chunk_service import (
    ChunkService
)


def render_chunk_page():

    st.header(
        "Chunking Engine"
    )

    pdf_files = (
        UploadService.get_uploaded_files()
    )

    if not pdf_files:

        st.warning(
            "Please upload a PDF first."
        )

        return

    selected_pdf = st.selectbox(
        "Select PDF For Chunking",
        pdf_files,
        key="chunk_pdf_unique"
    )

    if st.button(
        "Generate Chunks"
    ):

        chunks = (
            ChunkService.generate_chunks(
                selected_pdf
            )
        )

        st.success(
            f"{len(chunks)} chunks generated."
        )

        st.subheader(
            "Chunk Statistics"
        )

        st.write(
            f"Total Chunks: {len(chunks)}"
        )

        for i, chunk in enumerate(
            chunks[:10]
        ):

            with st.expander(
                f"Chunk {i+1}"
            ):

                st.text_area(
                    f"Content {i+1}",
                    chunk,
                    height=200
                )