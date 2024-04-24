from typing import Optional

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from service import Expense
from langchain_core.utils.function_calling import convert_to_openai_tool

class LLMService:
    def __init__(self):
        self.prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert extraction algorithm. "
                "Only extract relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value.",
            ),
        ]
        )
        self.llm = ChatMistralAI(model="mistral-large-latest", temperature=0)
        self.runnable = self.prompt | self.llm.with_structured_output(schema=Expense)

    def runLLM(self, message):
        return self.runnable.invoke({"text": message})