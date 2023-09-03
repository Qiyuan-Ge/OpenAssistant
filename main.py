import io
import os
import openai
import requests
import streamlit as st
from openai.error import AuthenticationError
from langchain.callbacks import StreamlitCallbackHandler

from open_assistant import load_tools, load_agent
from open_assistant.cases import CASES
from open_assistant.watsen import SimCaseSearch, ConversationMimic


st.set_page_config(page_title="My Assistant", page_icon="💬")
st.title("My Assistant")


def init_session_state():
    if "server_api_key" not in st.session_state:
        st.session_state.server_api_key = "EMPTY"
    if "server_api_base" not in st.session_state:
        st.session_state.server_api_base = "https://u31193-92ae-b10f516b.neimeng.seetacloud.com:6443/v1" #"https://api.openai.com/v1"
    if "generate_params" not in st.session_state:
        st.session_state.generate_params = {'max_tokens':2048, 'temperature':0.9, 'top_p':0.6}
    if "tool_names" not in st.session_state:
        st.session_state.tool_names = ["Browse Website"]
    if "chat_model_name" not in st.session_state:
        st.session_state.chat_model_name = "gpt-3.5-turbo"
    if "completion_model_name" not in st.session_state:
        st.session_state.completion_model_name = "text-davinci-003"
    if "embedding_model_name" not in st.session_state:
        st.session_state.embedding_model_name = "text-embedding-ada-002"
    if "prompt_template" not in st.session_state:
        st.session_state.prompt_template = "vicuna_v1.1"
    if "system_message" not in st.session_state:
        st.session_state.system_message = "You are Vic, an AI assistant that follows instruction extremely well. Help as much as you can."
    if "translation" not in st.session_state:
        st.session_state.translation = ""
    if "translation_lang" not in st.session_state:
        st.session_state.translation_lang = "中文"
        

def set_openai_keys(api_key="EMPTY", api_base="https://api.openai.com/v1"):
    os.environ['OPENAI_API_KEY'] = api_key
    os.environ['OPENAI_API_BASE'] = api_base
    openai.api_key = api_key
    openai.api_base = api_base


init_session_state()
set_openai_keys(st.session_state.server_api_key, st.session_state.server_api_base)


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
    if st.session_state.messages[-1]["role"] == "assistant":
        del st.session_state.messages[-1]


def clear_messages():
    del st.session_state.messages


def click_add_message(message):
    st.session_state.messages.append({"role": "user", "content": message})


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


def translate_func(params):
    translator = load_tools(tool_names=['Translator'], model_name=chat_model_name)[0]
    st.session_state.translation = translator(params)
    

def main():
    template_name = st.session_state.prompt_template
    system_message = st.session_state.system_message
    
    chat_model_name = st.session_state.chat_model_name
    embedding_model_name = st.session_state.embedding_model_name
    completion_model_name = st.session_state.completion_model_name
    
    tool_names = st.session_state.tool_names
    tools = load_tools(tool_names=tool_names, model_name=chat_model_name, embedding_model_name=embedding_model_name)

    generate_params = st.session_state.generate_params
    agent = load_agent(model_name=completion_model_name, tools=tools, generate_params=generate_params)
    
    sim_case_search = init_sim_case_search(CASES, model_name=embedding_model_name)
    conversation_mimic = ConversationMimic(model_name=chat_model_name)

    avatar_user = None
    avatar_assistant = None
    messages = init_messages(avatar_user=avatar_user, avatar_assistant=avatar_assistant)

    if prompt := st.chat_input("Shift + Enter 换行, Enter 发送"):
        with st.chat_message("user", avatar=avatar_user):
            st.markdown(prompt)
        messages.append({"role": "user", "content": prompt})

    if len(messages) == 0:
        with st.container():
            col1, col2, col3 = st.columns([2, 2.5, 3])
            with col1:
                example1 = "Who are you?"
                st.button(f"💬{example1}", key='b_r1', on_click=click_add_message, kwargs={'message':example1})
            with col2:
                example2 = "What can you do for me?"
                st.button(f"💬{example2}", key='b_r2', on_click=click_add_message, kwargs={'message':example2})
            with col3:
                example3 = "What are the headlines today?"
                st.button(f"💬{example3}", key='b_r3', on_click=click_add_message, kwargs={'message':example3})
            
            col1, col2 = st.columns([2.5, 3])
            with col1:
                example4 = "Search Marvel Movies Coming in 2024."
                st.button(f"💬{example4}", key='b_r4', on_click=click_add_message, kwargs={'message':example4})
            with col2:
                example5 = "Write a letter to invite my friend to Shanghai."
                st.button(f"💬{example5}", key='b_r5', on_click=click_add_message, kwargs={'message':example5})
            
            example6 = "Give me a summary of this web page: https://github.com/Qiyuan-Ge/OpenAssistant"
            st.button(f"💬{example6}", key='b_r6', on_click=click_add_message, kwargs={'message':example6})
        
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
                        {'user': prompt, 'history': messages[:-1], 'example': one_shot, 'system_message': system_message , 'conv_template_name': template_name}, 
                        callbacks=[st_callback]
                    )
                placeholder.markdown(response)
            except AuthenticationError:
                response = "Something wrong happened. The system is taking over the AI assistant"
                st.info("For users interested in HuggingFace models", icon="ℹ️")
                st.error("Incorrect API Base provided. See how to set API base at https://github.com/Qiyuan-Ge/OpenAssistant.")
                st.info("For users interested in OpenAI models", icon="ℹ️")
                st.error("Incorrect API Key provided. Find your API key at https://platform.openai.com/account/api-keys.")
                st.stop()
            except Exception as e:
                response = "Something wrong happened. The system is taking over the AI assistant"
                st.error(e)
                st.stop()
        placeholder.markdown(response)
        messages.append({"role": "assistant", "content": response})
        print(messages)
        with st.spinner('You might ask...'):
            try:
                predictions = conversation_mimic(messages)
            except Exception as e:
                predictions = None

        if predictions is not None:
            st.button(f"🔵{predictions[0]}", key='b1', on_click=click_add_message, kwargs={'message':predictions[0]})
            st.button(f"🔴{predictions[1]}", key='b2', on_click=click_add_message, kwargs={'message':predictions[1]})
         
    if len(messages) > 0:
        col1, col2, col3 = st.columns([2, 2, 8])
        with col1:
            st.button("try again", key='b3', on_click=try_again)
        with col2:
            st.button("go back", key='b4', on_click=go_back)
        with col3:
            st.button("clear conversation", key='b5', on_click=clear_messages)
        
    with st.container():
        with st.expander("Translator"):
            col1, col2, col3 = st.columns([6, 1, 1])
            with col1:
                text = st.text_input(label="Text", key='text')
            with col2:
                lang = st.text_input(label="Language", key='lang', value=st.session_state.translation_lang, max_chars=20)
            with col3:
                st.button("Translate", key='b_trans', on_click=translate_func, kwargs={'text':text, 'language':lang})
            st.write(st.session_state.translation)

        
if __name__ == "__main__":
    main()
