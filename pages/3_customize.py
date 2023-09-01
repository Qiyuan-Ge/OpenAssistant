import streamlit as st
from fastchat.conversation import conv_templates, get_conv_template

st.image("https://cdn.pixabay.com/photo/2023/02/11/16/32/ai-generated-7783344_640.jpg", width=256)

tab1, tab2, tab3 = st.tabs(["Prompt Template", "Custom Instructions", "Generate Params"])

if "customize_button" not in st.session_state:
    st.session_state.customize_button = True

def get_options():
    options = list(conv_templates.keys())
    options.remove(st.session_state.prompt_template)
    options.insert(0, st.session_state.prompt_template)
    
    return options

with tab1:
   st.markdown('**Select a conversation prompt template**')
   option = st.selectbox(
       label='Select a conversation prompt template',
       options=get_options(),
       label_visibility='collapsed',
    )
   st.session_state.prompt_template = option
   
   conv = get_conv_template(option)
   conv.append_message(conv.roles[0], "Hello!")
   conv.append_message(conv.roles[1], "Hi! How can I assist you today?")
   
   st.markdown(f'**{option} prompt template:**')
   st.text(conv.get_prompt())

with tab2:
    st.markdown('**What kind of assistant do you wish for?**')
    st.markdown('**Note:** the prompt you write below will overwrite the original system prompt.')
    if st.toggle('Turn on/off', value=st.session_state.customize_button, key="turn", label_visibility='hidden'):
        st.session_state.system_message = st.text_input(
            label="sys_prompt", 
            key="sys_prompt", 
            value=st.session_state.system_message,
            label_visibility='collapsed',
        )
    else:
        st.session_state.system_message = None

with tab3:
    st.markdown('**Params**')
    st.markdown('**Max New Tokens**')
    st.markdown("""
    Max New Tokens refers to the maximum number of new words or tokens that a language model can generate in a single response.

    For example, if the max new tokens value is set to 50, the model will generate a response with no more than 50 new words. If the response exceeds this limit, it may truncate or omit some text to fit within the specified maximum.
    """)
    max_toknes = st.slider('Max New Tokens', 1, 4096)
    st.markdown('**Temperature**')
    temperature = st.slider('Temperature', 0, 1)
    st.markdown('**Top-p (Nucleus Sampling)**')
    top_p = st.slider('Top-p', 0, 1)
