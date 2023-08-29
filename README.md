# OpenAssistant
<div align=center>
<img src="https://github.com/Qiyuan-Ge/PaintMind/blob/main/assets/A_beautiful_girl_celebrating_her_birthday.png?raw=true" width="384">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/License-Apache--2.0-green?style=flat&logo=appveyor" alt="Badge 1">
  <img src="https://img.shields.io/badge/Contact-542801615@qq.com-green?style=flat&logo=appveyor" alt="Badge 2">
</div>

## Everyone have their own AI assistant

| ![Image 1](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display0.png) | ![Image 2](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display1.png) |
| --- | --- |
| ![Image 3](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display2.png) | ![Image 4](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display3.png) |

## Quick Experience 
[streamlit app](https://openassistant.streamlit.app/)

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
