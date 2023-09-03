import streamlit as st
from typing import List
from langchain.agents import Tool
from langchain.tools import StructuredTool
from .google_search import GoogleSearch
from .weather import OpenWeatherMapAPIWrapper
from .browse_website import BrowseWebsiteWithQuestion
from .llm_math import Calulator
from .translator import Translator

            
def load_tools(tool_names: List[str], model_name="gpt-3.5-turbo", embedding_model_name="text-embedding-ada-002") -> List[Tool]:
    tools = []
    for tool_name in tool_names:
        if tool_name == "Google Search":
            try:
                tool_func = GoogleSearch(model_name=model_name)
                tool = Tool(
                    name="Google Search",
                    func=tool_func.run,
                    description='gather information from Internet, args: {"input": "query"}',
                )
                tools.append(tool)
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
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Browse Website":
            try:
                tool_func = BrowseWebsiteWithQuestion(model_name=model_name, embedding_model_name=embedding_model_name)
                tool = StructuredTool.from_function(
                    name="Browse website with question",
                    func=tool_func.run,
                )
                tool.description = 'gather information from a specified website, args: {"url": "url", "question": "question"}'
                tools.append(tool)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Calculator":
            try:
                tool_func = Calulator(model_name=model_name)
                tool = Tool(
                    name="Calculator",
                    func=tool_func.run,
                    description='language model that interprets a prompt and executes python code to do math, args: {"input": "math expression"}',
                )
                tools.append(tool)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        elif tool_name == "Translator":
            try:
                tool_func = Translator(model_name=model_name)
                tool = StructuredTool.from_function(
                    name="Translator",
                    func=tool_func.run,
                )
                tool.description = 'translate text to another language, args: {"text": "text", "language":"language"}'
                tools.append(tool)
            except Exception as e: 
                st.info(f"Failed to add {tool_name} to tool list", icon="ℹ️")
        else:
            st.info(f"Unknown tool name: {tool_name}", icon="ℹ️")
    tool = Tool(
        name="Final Response",
        func=lambda x: None,
        description='call this function when you know the final answer or complete all tasks, args: {"content": "markdown_format"}',
        )
    tools.append(tool)
    return tools
