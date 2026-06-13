import streamlit as st

from services.chat_service import (
    ChatService
)


def render_chat_page():

    st.header(
        "AI PDF Chat"
    )

    question = st.text_area(
        "Ask Question",
        key="chat_question_unique"
    )

    if st.button(
        "Ask AI"
    ):

        if not question:

            st.warning(
                "Enter question."
            )

            return

        with st.spinner(
            "Thinking..."
        ):

            result = (
                ChatService.ask(
                    question
                )
            )

        st.subheader(
            "AI Answer"
        )

        st.write(
            result["answer"]
        )

        st.subheader(
            "Retrieved Context"
        )

        for i, doc in enumerate(
            result["documents"]
        ):

            with st.expander(
                f"Context {i+1}"
            ):

                st.write(
                    doc.page_content
                )