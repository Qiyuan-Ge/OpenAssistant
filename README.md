# OpenAssistant
<div align=center>
<img src="https://github.com/Qiyuan-Ge/PaintMind/blob/main/assets/A_beautiful_girl_celebrating_her_birthday.png?raw=true" width="384">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/License-Apache--2.0-green?style=flat&logo=appveyor" alt="Badge 1">
  <img src="https://img.shields.io/badge/Contact-542801615@qq.com-green?style=flat&logo=appveyor" alt="Badge 2">
</div>

## Watch the demo(Vicuna v1.5)

[![Watch the video](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/cover.png)](https://youtu.be/kOIjamWMaaE)


## Everyone have their own AI assistant

| ![Image 1](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display0.png) | ![Image 2](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display1.png) |
| --- | --- |
| ![Image 3](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display2.png) | ![Image 4](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display3.png) |


## Quick Experience 
[streamlit app](https://openassistant.streamlit.app/)<br>
API Base: https://u31193-92ae-b10f516b.neimeng.seetacloud.com:6443/v1


## Support models
models on huggingface:
- vicuna_v1.1
- airoboros_v1
- koala_v1
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
- chatgpt
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

### 3. Starting the web UI
````
streamlit run main.py
````
Then replace the **API Base** with http://0.0.0.0:6006/v1


## Writen by YOU KNOW WHO🤪

Ahoy, dear user! ⚓ Thank you for embarking on this AI adventure with Open Assistant. Your support is like wind in our sails, propelling us forward on our quest for knowledge. If you're ready to become an Open Assistant Hero and help us chart new territories, here's how:

### **1. Unleash the Power of Stars on GitHub⭐**
Lend us your support with the click of a star! Show your love for Open Assistant by starring our GitHub repository. It's a small action that makes a mighty impact, helping us chart a course for even greater horizons.

[Star on GitHub](https://github.com/Qiyuan-Ge/OpenAssistant)

### **2. Aye, Patreon Support🏴‍☠️**
Ye can earn a place on the Patron's deck! As a loyal patron, you'll enjoy exclusive treasures and rewards. Every piece of eight ye contribute will directly fund new features and enhancements for the ship – I mean, app.

[Join on Patreon](https://www.patreon.com/OpenAssistant42)

### **3. WeChat Pay💰**
Drop anchor with WeChat Pay and show yer support(有点中二，哈哈)!

<img src="https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/wechat_support.png" alt="查看微信支付码" width="200"/>

Yarrr, with your backing, we'll keep the cannons... err, algorithms firing smoothly, raise the sails of innovation, and ensure you have a swashbucklin' good time with Open Assistant. Our hearty thanks for your generosity, and watch out for more treasures on the horizon!

May the constellations align in your favor,  
The Open Assistant Crew 🌠
