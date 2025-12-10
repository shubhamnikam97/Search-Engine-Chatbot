# 🔎 LangChain Search Engine Chatbot  
A Streamlit-powered intelligent chatbot that performs real-time web search using **LangChain**, **Groq LLM**, **DuckDuckGo**, **Wikipedia**, and **Arxiv**.  
The chatbot uses a LangChain agent to decide which tool to use based on the user query and streams results back interactively.

---

## 🚀 Features

- **Search-enabled chatbot** capable of:
  - 🔍 DuckDuckGo internet search  
  - 📚 Wikipedia lookup  
  - 🧪 Arxiv research paper search  
- **Groq LLM integration** using the `llama-3.1-8b-instant` model  
- **Streamed responses** inside an interactive chat UI  
- **Memory support** using Streamlit session state  
- **Safe error handling**  
  - Missing API key  
  - Search tool errors  
  - LLM initialization errors  
- Clean, user-friendly interface built with Streamlit  

---

## 🧠 How It Works

The chatbot uses a **LangChain Zero-Shot ReAct Agent** which:  
1. Reads the user input  
2. Decides which tool (Wikipedia, Arxiv, DuckDuckGo) is best  
3. Fetches external information  
4. Uses the Groq LLM to produce a final answer  
5. Displays streaming intermediate thoughts in Streamlit (via `StreamlitCallbackHandler`)  

This creates a powerful cognitive workflow that combines search + AI reasoning.

---

## 📦 Tech Stack

- **Python 3.12+**
- **Streamlit**
- **LangChain Classic**
- **LangChain Community Tools**
- **Groq LLM API** (LLaMA 3.1 8B Instant)
- **DuckDuckGo Search**
- **Wikipedia API**
- **Arxiv API**

---

## 📁 Project Structure

