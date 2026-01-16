import autogen
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Configure Gemin
config_list = [
    {
        "model": "gemini-2.5-flash",
        "api_key": os.getenv("GEMINI_API_KEY"),
        "api_type": "google"
    }
]

def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

def run_agent():
    # 1. The Expert EPLAN Engineer
    assistant = autogen.AssistantAgent(
        name="EplanEngineer",
        is_termination_msg=termination_msg,
        system_message="""You are an expert EPLAN API Automation Engineer.
        Your goal is to write precise, compilation-ready C# scripts for EPLAN Electric P8.
        
        RULES:
        1. Always use the retrieved context (from the RAG agent) to write code.
        2. Do not invent classes or methods. Rely on the documentation provided.
        3. Wrap your C# code in logical blocks.
        4. If you lack information, ask for clarification.
        5. When finished, reply with terminate.
        """,
        llm_config={
            "config_list": config_list,
            "timeout": 120,
        },
    )

    # 2. The Admin + RAG Engine (Native)
    rag_proxy = RetrieveUserProxyAgent(
        name="Admin",
        human_input_mode="ALWAYS",
        max_consecutive_auto_reply=3,
        retrieve_config={
            "task": "code",
            "docs_path": [
                "src/ai/Knowledge/Scripts",      # JSON Examples
                "src/ai/Knowledge/eplan_docs",   # Markdown Docs
            ],
            "chunk_token_size": 2000,
            "model": config_list[0]["model"],
            "collection_name": "eplan_knowledge_base",
            "get_or_create": True,  # Re-use ChromaDB collection if exists
        },
        code_execution_config=False,  # We don't execute C# here yet
    )

    # 3. Start Chat!
    print("🚀 EPLAN AutoGen Assistant Ready!")
    
    # Start with a welcome message or prompt
    rag_proxy.initiate_chat(
        assistant,
        problem="Welcome! I am your EPLAN Assistant. What script do you need?",
    )

if __name__ == "__main__":
    run_agent()
