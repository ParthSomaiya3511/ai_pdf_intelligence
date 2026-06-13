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
    ).decode("utf-8")

    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="900"
        type="application/pdf">
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

    left, right = st.columns(
        [1, 2]
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

    with left:

        selected_pdf = st.selectbox(
            "Select Document",
            pdf_files,
            key="enterprise_pdf_select"
        )

        query = st.text_input(
            "Search Anything",
            placeholder="""
5000
Invoice
GST
Phone
Email
Employee
Keyword
Sentence
""",
            key="enterprise_search"
        )

        if st.button(
            "Search",
            key="enterprise_btn"
        ):

            pattern_results = (
                SearchService
                .pattern_search(
                    selected_pdf,
                    query
                )
            )

            semantic_results = (
                SearchService
                .search_documents(
                    query
                )
            )

            st.session_state[
                "pattern_results"
            ] = pattern_results

            st.session_state[
                "semantic_results"
            ] = semantic_results

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

    if (
        "pattern_results"
        in st.session_state
    ):

        st.divider()

        st.subheader(
            "Exact Match Results"
        )

        results = (
            st.session_state[
                "pattern_results"
            ]
        )

        st.success(
            f"{len(results)} Matches Found"
        )

        for result in results:

            with st.expander(
                f"Line {result['line']}"
            ):

                st.write(
                    result["text"]
                )

    if (
        "semantic_results"
        in st.session_state
    ):

        st.divider()

        st.subheader(
            "AI Semantic Results"
        )

        for i, doc in enumerate(
            st.session_state[
                "semantic_results"
            ]
        ):

            with st.expander(
                f"Result {i+1}"
            ):

                st.write(
                    doc.page_content
                )