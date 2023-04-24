from llm_agents import (
    Agent,
    ChatLLM,
    PythonREPLTool,
    HackerNewsSearchTool,
    SerpAPITool,
    AskUserViaTerminal,
    AskAssistantViaTerminal,
)

if __name__ == "__main__":
    prompt = input("Enter a question / task for the agent: ")
    # prompt = "When can I apply for Canadian citizenship application?"
    # prompt = "Am I eligible to apply for Canadian citizenship application?"
    # prompt = "Am I eligible to apply for Canadian citizenship application?"

    agent = Agent(
        llm=ChatLLM(),
        tools=[
            PythonREPLTool(),
            SerpAPITool(),
            AskUserViaTerminal(),
            AskAssistantViaTerminal(),
        ],
    )
    result = agent.run(prompt)

    print(f"Final answer is {result}")
