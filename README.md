# OpenAssistant
<div align=center>
<img src="https://github.com/Qiyuan-Ge/PaintMind/blob/main/assets/A_beautiful_girl_celebrating_her_birthday.png?raw=true" width="384">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/License-Apache--2.0-green?style=flat&logo=appveyor" alt="Badge 1">
  <img src="https://img.shields.io/badge/Contact-542801615@qq.com-green?style=flat&logo=appveyor" alt="Badge 2">
</div>


## Quick Experience 
[openassistant app](https://openassistant.streamlit.app/)<br>

darkassistant is the new version:<br>
[darkassistant app](https://darkassistant.streamlit.app/)<br>


## Features
Let's ask the assistant first🤔:
<div style="text-align: center;">
    <img src="https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display4.png" alt="display4">
</div>

So this project encompasses the following features:

#### 1. Rapid Conversion of LLM to Agent🤖

Effortlessly transform your Language Model (LLM) into an Agent.

#### 2. LLM Proficiency Testing Tool🛠️

Explore and evaluate the capabilities of your Language Model through the integrated testing tool. 

#### 3. Open Assistant WebUI

Experience the convenience of the Open Assistant Web User Interface (WebUI). 

## Watch the demo(Vicuna v1.5)
- Youtube
[![Watch the video](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/cover.png)](https://youtu.be/kOIjamWMaaE)
- BiliBili
[![Watch the video](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/cover.png)](https://www.bilibili.com/video/BV1ru4y1e7of/?vd_source=9d5543a5652fd4789c2e2c4f4a10267a)

## Everyone have their own AI assistant

| ![Image 1](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display0.png) | ![Image 2](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display1.png) |
| --- | --- |
| ![Image 3](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display2.png) | ![Image 4](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display3.png) |

## Support models
models on huggingface:
- vicuna
- airoboros
- koala
- alpaca
- chatglm
- chatglm2
- dolly_v2
- oasst_pythia
- oasst_llama
- tulu
- stablelm
- baize
- rwkv
- openbuddy
- phoenix
- claude
- mpt-7b-chat
- mpt-30b-chat
- mpt-30b-instruct
- bard
- billa
- redpajama-incite
- h2ogpt
- Robin
- snoozy
- manticore
- falcon
- polyglot_changgpt
- tigerbot
- xgen
- internlm-chat
- starchat
- baichuan-chat
- llama-2
- cutegpt
- open-orca
- qwen-7b-chat
- aquila-chat
- ...


## How to use
### 1. Installation
````
git clone https://github.com/Qiyuan-Ge/OpenAssistant.git
cd OpenAssistant
pip install -r requirements.txt
````
### 2. Starting the server
First, launch the controller:
````
python3 -m fastchat.serve.controller
````
Then, launch the model worker(s):
````
python3 -m fastchat.serve.multi_model_worker \
    --model-path model_math \
    --model-names "gpt-3.5-turbo,text-davinci-003" \
    --model-path embedding_model_math \
    --model-names "text-embedding-ada-002"
````
Finally, launch the RESTful API server：
````
python3 -m fastchat.serve.openai_api_server --host 0.0.0.0 --port 6006
````
You should see terminal output like：
````
INFO:     Started server process [1301]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:6006 (Press CTRL+C to quit)
````
See more details in https://github.com/lm-sys/FastChat/blob/main/docs/openai_api.md

### 3. Starting the web UI
````
streamlit run main.py
````
Then replace the **API Base** with your api base (in this case is http://0.0.0.0:6006/v1) <br>
<img src="https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/api%20base.png" alt="apibase" width="128"/>
