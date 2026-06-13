import streamlit as st

from services.upload_service import UploadService
from services.intelligence_service import IntelligenceService


def render_intelligence_page():

    st.header("Document Intelligence")

    pdfs = UploadService.get_uploaded_files()

    if not pdfs:
        st.warning("Upload PDF first.")
        return

    selected_pdf = st.selectbox(
        label="Select PDF For Analysis",
        options=pdfs,
        index=0,
        key="intelligence_pdf_unique_2026"
    )

    analyze_btn = st.button(
        "Analyze Document",
        key="analyze_document_btn"
    )

    if analyze_btn:

        with st.spinner("Analyzing Document..."):

            result = IntelligenceService.analyze_pdf(
                selected_pdf
            )

        st.success("Analysis Complete")

        st.subheader("Pattern Detection")
        st.json(result["patterns"])

        st.subheader("Missing Numbers")
        st.write(result["missing_numbers"])

        st.subheader("AI Entities")
        st.write(result["entities"])