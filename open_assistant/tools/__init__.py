from typing import List
from langchain.agents import Tool
from langchain.tools import StructuredTool
from .google_search import GoogleSearch
from .weather import OpenWeatherMapAPIWrapper
from .browse_website import BrowseWebsiteWithQuestion

            
def load_tools(tool_names: List[str], model_name="gpt-3.5-turbo", embedding_model_name="text-embedding-ada-002") -> List[Tool]:
    tools = []
    for tool_name in tool_names:
        if tool_name == "Google Search":
            try:
                tool_func = GoogleSearch(model_name=model_name)
                tool = Tool(
                    name="Google Search",
                    func=tool_func.run,
                    description='gather information from Internet, args: {"input": "<query>"}',
                )
                tools.append(tool)
            except:
                pass
        elif tool_name == "Current Weather":
            try:
                tool_func = OpenWeatherMapAPIWrapper()
                tool = Tool(
                    name="Current Weather",
                    func=tool_func.run,
                    description='get the current weather information for a specified location, args: {"input": "<city_name>"}',
                )
                tools.append(tool)
            except:
                pass
        elif tool_name == "Browse Website":
            try:
                tool_func = BrowseWebsiteWithQuestion(model_name=model_name, embedding_model_name=embedding_model_name)
                tool = StructuredTool.from_function(
                    name="Browse website with question",
                    func=tool_func.run,
                )
                tool.description = 'gather information from a specified website, args: {"url": "<url>", "question": <question>}'
                tools.append(tool)
            except:
                pass
        else:
            raise ValueError(f"Unknown tool name: {tool_name}")
    tool = Tool(
        name="Final Response",
        func=lambda x: None,
        description='call this function when you know the final answer or complete all tasks, args: {"content": "<markdown_format>"}',
        )
    tools.append(tool)
    return tools