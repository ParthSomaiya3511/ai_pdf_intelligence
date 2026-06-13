import streamlit as st

from ui.upload_page import (
    render_upload
)

from ui.pdf_viewer_page import (
    render_pdf_viewer
)

from ui.chunk_page import (
    render_chunk_page
)

from ui.vector_page import (
    render_vector_page
)

from ui.search_page import (
    render_search_page
)

from ui.chat_page import (
    render_chat_page
)

from ui.intelligence_page import (
    render_intelligence_page
)

st.set_page_config(
    page_title="AI PDF Intelligence",
    layout="wide"
)

st.title(
    "AI PDF Intelligence Platform"
)

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    [
        "Upload",
        "PDF Viewer",
        "Chunking",
        "Vector DB",
        "Search",
        "AI Chat",
        "Intelligence"
    ]
)

with tab1:
    render_upload()

with tab2:
    render_pdf_viewer()

with tab3:
    render_chunk_page()

with tab4:
    render_vector_page()

with tab5:
    render_search_page()
    
with tab6:
    render_chat_page()
    
with tab7:
    render_intelligence_page()