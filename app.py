import os
from dotenv import load_dotenv
import streamlit as st

from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_classic.agents import AgentType, initialize_agent
from langchain_classic.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq
# from langchain_huggingface import HuggingFaceEmbeddings

# Loading environment variable
# groq_api_key=os.getenv('GROQ_API_KEY')
# os.environ['HF_TOKEN']=os.getenv('HF_TOKEN')
# embeddings = HuggingFaceEmbeddings(model="all-MiniLM-L6-v2")

# Arxiv and wikipedia tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

# Creating search tool from internet
search = DuckDuckGoSearchRun(name='Search')

# Tool title
st.title("🔎 LangChain - Chat with search")
# """
# In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
# Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
# """

# Side bar setting
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if "messages" not in st.session_state:
    st.session_state['messages'] =[
        {
            "role":"assistant",
            "content":"Hi, I'm a web search chatbot. How can I help you?"
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])


if prompt:=st.chat_input(placeholder="What is machine learning?"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=api_key,
                   model='llama-3.1-8b-instant', 
                   streaming=True, 
                   tool_choice="none")
    tools = [search, arxiv, wiki]

    search_agent = initialize_agent(tools=tools, 
                                    llm=llm,
                                    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                    handling_parsing_errors=True)
    
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(),
                                         expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant',
                                          'content':response})
        st.write(response)





























































