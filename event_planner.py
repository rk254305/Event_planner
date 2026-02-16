from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent


class EventPlannerAI:
    def __init__(self):
        # LLM
        self.llm = ChatOllama(model="llama2", temperature=0.7)
        self.parser = StrOutputParser()

        # -------- VECTOR DB --------
        embeddings = OllamaEmbeddings(model="llama2")
        self.vectorstore = FAISS.load_local(
            "vectorstore",
            embeddings,
            allow_dangerous_deserialization=True
        )
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})

        # -------- RAG PROMPT --------
        self.rag_prompt = PromptTemplate.from_template("""
You are an expert event planner.

Use the following context to answer:
{context}

Question:
{question}
""")

        self.rag_chain = (
            self.rag_prompt
            | self.llm
            | self.parser
        )

        @tool
        def event_knowledge_tool(query: str) -> str:
            """Use this tool to answer event planning questions using knowledge base"""
            docs = self.retriever.invoke(query)
            context = "\n".join([d.page_content for d in docs])
            return self.rag_chain.invoke({
                "context": context,
                "question": query
            })

        self.tools = [event_knowledge_tool]

        self.agent = create_react_agent(self.llm, self.tools)

        def ask_agent(self, query: str):
         response = self.agent.invoke({
            "messages": [("user", query)]
         })
         return response["messages"][-1].content
