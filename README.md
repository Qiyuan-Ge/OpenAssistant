# OpenAssistant
<div align=center>
<img src="https://github.com/Qiyuan-Ge/PaintMind/blob/main/assets/A_beautiful_girl_celebrating_her_birthday.png?raw=true" width="384">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/License-Apache--2.0-green?style=flat&logo=appveyor" alt="Badge 1">
  <img src="https://img.shields.io/badge/Contact-542801615@qq.com-green?style=flat&logo=appveyor" alt="Badge 2">
</div>

### Everyone have their own AI assistant

| ![Image 1](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display0.png) | ![Image 2](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display1.png) |
| --- | --- |
| ![Image 3](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display2.png) | ![Image 4](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display3.png) |

### Quick Experience 
[streamlit app](https://openassistant.streamlit.app/)

### How to use?
#### 1. Installation
````
git clone https://github.com/Qiyuan-Ge/OpenAssistant.git
cd OpenAssistant
pip install -r requirements.txt
````
#### 2. Start the server
First, launch the controller
````
python3 -m fastchat.serve.controller
````
Then, launch the model worker(s)
````
python3 -m fastchat.serve.multi_model_worker \
    --model-path model_math \
    --model-names "gpt-3.5-turbo,text-davinci-003" \
    --model-path embedding_model_math \
    --model-names "text-embedding-ada-002"
````
Finally, launch the RESTful API server
````
python3 -m fastchat.serve.openai_api_server --host 0.0.0.0 --port 6006
````
<img src="https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/server3.png" alt="server" width="300">



| ![Image 1](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display0.png) |
| --- |
| ![Image 3](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/display2.png) |
| --- |
| ![Image 3](https://github.com/Qiyuan-Ge/OpenAssistant/blob/main/assets/server3.png) |


Now, let us replace the openai's API base with "http://0.0.0.0:6006/v1".

#### 3. Start the webui
````
streamlit run main.py
````
