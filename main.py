import io
import os
import openai
import requests
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

from open_assistant import load_tools, load_agent
from open_assistant.cases import CASES
from open_assistant.watsen import SimCaseSearch

st.set_page_config(page_title="My Assistant", page_icon="💬")
st.title("My Assistant")


def init_server():
    if "server_api_key" not in st.session_state:
        st.session_state.server_api_key = "EMPTY"
    if "server_api_base" not in st.session_state:
        st.session_state.server_api_base = "https://api.openai.com/v1"
        

def set_openai_keys(api_key="EMPTY", api_base="https://api.openai.com/v1"):
    os.environ['OPENAI_API_KEY'] = api_key
    os.environ['OPENAI_API_BASE'] = api_base
    
    openai.api_key = api_key
    openai.api_base = api_base


init_server()


with st.sidebar:
    st.markdown(
        "## How to use?\n"
        "#### 1.Server\n"
        "Enter your OpenAI API Key for accessing OpenAI models, otherwise ignore this."
    )
    st.session_state.server_api_key = st.text_input(
        label="API Key", 
        key="api_key", 
        type="password",
        value=st.session_state.server_api_key,
    )
    st.session_state.server_api_base = st.text_input(
        label="API Base", 
        key="api_base", 
        value=st.session_state.server_api_base,
    )
    set_openai_keys(st.session_state.server_api_key, st.session_state.server_api_base)
    
    st.markdown(
        "#### 2.Select tools\n"
        "#### 3.Custom instructions\n"
        "#### 4.Chat with your assistant!\n"
    )


@st.cache_resource
def init_sim_case_search(case, model_name):
    return SimCaseSearch(data=case, model_name=model_name)
    

def go_back():
    st.session_state.messages = st.session_state.messages[:-2]
    

def try_again():
    del st.session_state.messages[-1]


def clear_messages():
    del st.session_state.messages
    

def init_tool_names():
    if "tool_names" not in st.session_state:
        st.session_state.tool_names = []
    return st.session_state.tool_names


def init_prompt_template():
    if "prompt_template" not in st.session_state:
        st.session_state.prompt_template = "vicuna_v1.1"
    return st.session_state.prompt_template


def init_system_message():
    if "system_message" not in st.session_state:
        st.session_state.system_message = "You are Joi, an AI that follows instructions extremely well."
    return st.session_state.system_message


def init_messages(avatar_user='🧑‍💻', avatar_assistant='🤖'):
    with st.chat_message("assistant", avatar=avatar_assistant):
        st.markdown("Welcome back!😊")

    if "messages" in st.session_state:
        for message in st.session_state.messages:
            avatar = avatar_user if message["role"] == "user" else avatar_assistant
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])
    else:
        st.session_state.messages = []

    return st.session_state.messages


def read_image(image_path):
    if image_path.startswith('http'):
        resp = requests.get(image_path)
        resp.raise_for_status()
        image_data = io.BytesIO(resp.content)
    else:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image_data = io.BytesIO(image_data)
    
    return image_data
    

def main():
    avatar_user = None
    avatar_assistant = None
    
    tool_names = init_tool_names()
    tools = load_tools(tool_names=tool_names, model_name="gpt-3.5-turbo", embedding_model_name="text-embedding-ada-002")
    
    agent = load_agent(model_name="text-davinci-003", tools=tools)
    
    sim_case_search = init_sim_case_search(CASES, model_name="text-embedding-ada-002")

    conv_template_name = init_prompt_template()
    system_message = init_system_message()
    messages = init_messages(avatar_user=avatar_user, avatar_assistant=avatar_assistant)
    
    if prompt := st.chat_input("Shift + Enter 换行, Enter 发送"):
        with st.chat_message("user", avatar=avatar_user):
            st.markdown(prompt)
    
    if len(messages) > 0 and messages[-1]['role'] == 'user':
        prompt = messages[-1]['content']

    if prompt:
        with st.chat_message("assistant", avatar=avatar_assistant):
            placeholder = st.empty()
            st_callback = StreamlitCallbackHandler(st.container())
            try:
                one_shot = sim_case_search(prompt)
                with st.spinner('I am thinking🤔...'):
                    response = agent.run(
                        {'user': prompt, 'history': messages, 'example': one_shot, 'system_message': system_message , 'conv_template_name': conv_template_name}, 
                        callbacks=[st_callback]
                    )
            except Exception as e:
                st.warning("[For users interested in HuggingFace models]")
                st.warning("Incorrect API Base provided. See how to set API base at https://github.com/Qiyuan-Ge/OpenAssistant.")
                st.warning("[For users interested in OpenAI models]")
                st.warning("Incorrect API Key provided. Find your API key at https://platform.openai.com/account/api-keys.")
                st.stop()
            placeholder.markdown(response)
        messages.append({"role": "user", "content": prompt})
        messages.append({"role": "assistant", "content": response})
        
        st.button("clear conversation", key='b3', on_click=clear_messages)
        st.button("try again", key='b2', on_click=try_again)
    
    if len(messages) > 0:
        st.button("go back", key='b1', on_click=go_back)
            

if __name__ == "__main__":
    main()
