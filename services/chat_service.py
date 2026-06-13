from ai.ai_chat import (
    AIChat
)


class ChatService:

    @staticmethod
    def ask(question):

        return AIChat.ask(
            question
        )