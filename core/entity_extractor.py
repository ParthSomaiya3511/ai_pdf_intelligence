from ai.llm_manager import (
    LLMManager
)


class EntityExtractor:

    @staticmethod
    def extract(text):

        llm = (
            LLMManager.get_llm()
        )

        prompt = f"""
Extract entities from the text.

Return:

People
Companies
Emails
Phones
Invoices
Locations

Text:

{text[:4000]}
"""

        response = (
            llm.invoke(
                prompt
            )
        )

        return response.content