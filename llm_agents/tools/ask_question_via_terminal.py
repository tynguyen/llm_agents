import sys
from io import StringIO
from typing import Dict, Optional, List

from pydantic import BaseModel, Field
from llm_agents.tools.base import ToolInterface
import json


class AskUserViaTerminal(ToolInterface):
    """A tool for asking user for more information."""

    name: str = "Ask User Via Terminal"
    description: str = (
        "An interface to ask user questions. Use this to ask users a list of questions. "
        "Input should be a list of questions separated by ;"
    )

    def use(self, input_text: List[str]) -> str:
        input_text = input_text.strip().strip("```")
        parsed_input = input_text.split(";")
        answers = []
        for question in parsed_input:
            print(f"Bot: {question}")
            print(f"User: ")
            answer = input()
            answers.append(answer)

        return str(answers)


class AskAssistantViaTerminal(ToolInterface):
    """A tool for asking assistant for more information."""

    name: str = "Ask Assistant Via Terminal"
    description: str = (
        "An interface to ask assistant questions. Assistant is a person you can seek for help when really necessary."
        "Use this to ask assistant a list of questions when you cannot find answers using other approaches. "
        "Input should be a list of questions separated by ;"
    )

    def use(self, input_text: List[str]) -> str:
        input_text = input_text.strip().strip("```")
        parsed_input = input_text.split(";")
        answers = []
        for question in parsed_input:
            print(f"Bot: {question}")
            print(f"Assistant: ")
            answer = input()
            answers.append(answer)

        return str(answers)


if __name__ == "__main__":
    ask_user_tool = AskUserViaTerminal()
    result = ask_user_tool.use(
        "['when did you go to Vietnam?', 'What is your favorite book?']"
    )
    print(result)
