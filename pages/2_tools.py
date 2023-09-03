import os
import json
import streamlit as st
from io import StringIO
    

if "env_key_data" not in st.session_state:
    st.session_state.env_key_data = {"OPENWEATHERMAP_API_KEY": "0b4591ad2028813c97dedeffa0d08c9c"}


def add_tool(name):
    if name not in st.session_state.tool_names:
        st.session_state.tool_names.append(name)


def remove_tool(name):
    if name in st.session_state.tool_names:
        st.session_state.tool_names.remove(name)
        

def check_state(name):
    if name in st.session_state.tool_names:
        return True
    else:
        return False
    

def update(tool_name, obj_key):
    if st.toggle('Turn on/off', value=check_state(tool_name), key=obj_key, label_visibility='hidden'):
        add_tool(tool_name)
    else:
        remove_tool(tool_name)


def update_key(env_name, obj_key):
    key = st.session_state.env_key_data.get(env_name, "")
    os.environ[env_name] = st.text_input(label="API Key", value=key, key=obj_key, type="password")
    st.session_state.env_key_data[env_name] = os.environ[env_name]
    
    
@st.cache_data
def convert_json(data_dict):
    return json.dumps(data_dict, indent=4)
    
    
st.set_page_config(page_title="Tool store", page_icon="🏪")

st.title("Tool store🏪")


with st.container():
    key_data = convert_json(st.session_state.env_key_data)
    
    st.markdown(
        """
        Download the keys you have entered in the tool store.
        """
    )

    st.download_button(
        label="Download",
        data=key_data,
        file_name='tool_key.json',
        mime='text/json',
        use_container_width=True,
    )
    
    st.markdown(
        """
        Upload the key file to restore the keys.
        """
    )
    
    uploaded_file = st.file_uploader("Upload the key file", label_visibility="collapsed")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        st.session_state.env_key_data = json.loads(string_data)

st.divider()

with st.container():
    st.subheader('Google Search🔍')
    update("Google Search", "ck1")
    st.markdown(
        """
        Use the Google Serper component to search the web.
        
        Sign up for a free account at [serper](https://serper.dev/) and get your api key.
        """
    )
    update_key("SERPER_API_KEY", "api_key_1")

st.divider()

with st.container():
    st.subheader('Current Weather🌦️') 
    update("Current Weather", "ck2")
    st.markdown(
        """
        Use the OpenWeatherMap component to fetch weather information.
        
        Sign up for a free account at [openweathermap](https://openweathermap.org/api/) and get your api key.
        """
    )
    update_key("OPENWEATHERMAP_API_KEY", "api_key_2")

st.divider()

with st.container():
    st.subheader('Browse Website📱')
    update("Browse Website", "ck3")
    st.markdown(
        """
        Fetch information from the given web page.
        """
    )

st.divider()

with st.container():
    st.subheader('Calculator➗') 
    update("Calculator", "ck4")
    st.markdown(
        """
        Language model that interprets a prompt and executes python code to do math.
        """
    )

st.divider()

with st.container():
    st.subheader('Translator🗣️') 
    update("Translator", "ck5")
    st.markdown(
        """
        Translate text to another language.
        """
    )
