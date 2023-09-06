import streamlit as st
from typing import List
from langchain.agents import Tool
from langchain.tools import StructuredTool
from .google_search import GoogleSearch
from .weather import OpenWeatherMapAPIWrapper
from .browse_website import BrowseWebsiteWithQuestion
from .llm_math import Calulator
from .translator import Translator
from .wikipedia import Wikipedia
from .code_agent import CodeAgent

            
def load_tools(
    tool_names: List[str], 
    chat_model_name="gpt-3.5-turbo",
    code_model_name="code-llama", 
    embedding_model_name="text-embedding-ada-002",
    wiki_lang="en") -> List[Tool]:
    tools = []
    inside_tool_names = []       
    for tool_name in tool_names:
        if tool_name == "Google Search":
            try:
                tool_func = GoogleSearch(model_name=chat_model_name)
                tool = Tool(
                    name="Google Search",
                    func=tool_func.run,
                    description='gather information from Google, args: {"input": "query"}',
                )
                tools.append(tool)
                inside_tool_names.append(tool.name)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Current Weather":
            try:
                tool_func = OpenWeatherMapAPIWrapper()
                tool = Tool(
                    name="Current Weather",
                    func=tool_func.run,
                    description='get the current weather information for a specified location, args: {"input": "city_name"}',
                )
                tools.append(tool)
                inside_tool_names.append(tool.name)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Browse Website":
            try:
                tool_func = BrowseWebsiteWithQuestion(model_name=chat_model_name, embedding_model_name=embedding_model_name)
                tool = StructuredTool.from_function(
                    name="Browse website with question",
                    func=tool_func.run,
                )
                tool.description = 'gather information from a specified website, args: {"url": "url", "question": "question"}'
                tools.append(tool)
                inside_tool_names.append(tool.name)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Wikipedia":
            try:
                tool_func = Wikipedia(model_name=chat_model_name, embedding_model_name=embedding_model_name, lang=wiki_lang)
                tool = StructuredTool.from_function(
                    name="Wikipedia with question",
                    func=tool_func.run,
                )
                tool.description = 'gather information from Wikipedia, args: {"input": "input", "question":"question"}'
                tools.append(tool)
                inside_tool_names.append(tool.name)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Calculator":
            try:
                tool_func = Calulator(model_name=chat_model_name)
                tool = Tool(
                    name="Calculator",
                    func=tool_func.run,
                    description='model that interprets a prompt and executes python code to do math, args: {"input": "math expression"}',
                )
                tools.append(tool)
                inside_tool_names.append(tool.name)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Translator":
            try:
                tool_func = Translator(model_name=chat_model_name)
                tool = StructuredTool.from_function(
                    name="Translator",
                    func=tool_func.run,
                )
                tool.description = 'translate text, args: {"text": "text", "language":"language"}'
                tools.append(tool)
                inside_tool_names.append(tool.name)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Code Agent":
            try:
                tool_func = CodeAgent(model_name=code_model_name)
                tool = Tool(
                    name="Code Agent",
                    func=tool_func.run,
                    description='args: {"instruction": "instruction"}',
                )
                tools.append(tool)
                inside_tool_names.append(tool.name)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        else:
            st.info(f"Unknown tool name: {tool_name}", icon="ℹ️")
    tool = Tool(
        name="Final Response",
        func=lambda x: None,
        description='call this function when you know the final answer or complete all tasks',
        )
    tools.append(tool)
    return tools, inside_tool_names
