import streamlit as st
import base64

from services.upload_service import (
    UploadService
)

from services.search_service import (
    SearchService
)

from services.pdf_service import (
    PDFService
)


def show_pdf(pdf_bytes):

    base64_pdf = base64.b64encode(
        pdf_bytes
    ).decode(
        "utf-8"
    )

    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="900px">
    </iframe>
    """

    st.markdown(
        pdf_display,
        unsafe_allow_html=True
    )


def render_search_page():

    st.header(
        "Smart PDF Search"
    )

    pdf_files = (
        UploadService
        .get_uploaded_files()
    )

    if not pdf_files:

        st.warning(
            "Upload PDF first."
        )

        return

    left, right = st.columns(
        [1, 2]
    )

    with left:

        selected_pdf = st.selectbox(
            "Select Document",
            pdf_files,
            key="search_pdf_select"
        )

        query = st.text_input(
            "Search Number / Pattern / Keywords",
            placeholder="""
5000
Invoice
GST
Email
Phone
Travel Invoice
Employee Rajkot
""",
            key="search_query_input"
        )

        search_clicked = st.button(
            "Search",
            key="search_button"
        )

    with right:

        st.subheader(
            "Live PDF Viewer"
        )

        pdf_bytes = (
            PDFService.get_pdf_bytes(
                selected_pdf
            )
        )

        show_pdf(
            pdf_bytes
        )

    if search_clicked:

        if not query:

            st.warning(
                "Enter search text."
            )

            return

        with st.spinner(
            "Searching..."
        ):

            results = (
                SearchService
                .pattern_search(
                    selected_pdf,
                    query
                )
            )

        st.divider()

        st.subheader(
            "Search Results"
        )

        st.success(
            f"{len(results)} Results Found"
        )

        if len(results) == 0:

            st.info(
                "No matching records found."
            )

        for result in results:

            with st.expander(
                f"Line {result['line']} | Score {result['score']}"
            ):

                st.write(
                    result["text"]
                )