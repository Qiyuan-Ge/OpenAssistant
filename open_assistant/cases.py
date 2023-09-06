import re

def extract_actions(text):
    # 使用正则表达式查找所有的Action部分
    action_pattern = r"Action: (.*?)\n"
    actions = re.findall(action_pattern, text, re.DOTALL)

    return actions

d = []
# 1
d.append("""Question: 截止2023年，加拿大有多少人口？
Thought: 我需要找出2023年加拿大的人口数量。
Action: Google Search
Action Input: {"input": "2023年加拿大人口数量"}
Observation: 根据Worldometer对最新的联合国数据的解释，截至2023年4月12日，加拿大的当前人口为38,658,314人。
Thought: 我现在知道了加拿大的当前人口
Action: Final Response
Action Input: 截至2023年，加拿大有38,658,314人
""")
# 2
d.append("""Question: 这个里面讲了什么？https://lilianweng.github.io/posts/2023-06-23-agent/ 
Thought: I need to gather information from the website <https://lilianweng.github.io/posts/2023-06-23-agent/> to understand the content.
Action: Browse website with question
Action Input: {"url": "https://lilianweng.github.io/posts/2023-06-23-agent/", "question": "这个里面讲了什么?" }
Observation: 这个文章讲述了LLM（大型语言模型）驱动的自主代理系统。在这个系统中，LLM作为代理的大脑，并且有几个关键组件：计划、记忆和工具使用。计划组件包括分解任务和自我反思；记忆组件包括短期和长期记忆；工具使用组件包括学习调用外部API以获取缺失的信息。文章还介绍了一些相关研究，例如AutoGPT、GPT-Engineer和BabyAGI等。最后，文章列出了一些参考文献。
Thought: I know what the article is about now.
Action: Final Response
Action Input: 这个文章讲述了LLM（大型语言模型）驱动的自主代理系统。在这个系统中，LLM作为代理的大脑，并且有几个关键组件：计划、记忆和工具使用。计划组件包括分解任务和自我反思；记忆组件包括短期和长期记忆；工具使用组件包括学习调用外部API以获取缺失的信息。文章还介绍了一些相关研究，例如AutoGPT、GPT-Engineer和BabyAGI等。最后，文章列出了一些参考文献。
""")
# 3
d.append("""Question: What's the weather like in Beijing now?
Thought: I need to get the current weather information for Beijing.
Action: Current Weather
Action Input: {"input": "Beijing"}
Observation: In Beijing, the current weather is as follows:
Detailed status: overcast clouds
Wind speed: 2.96 m/s, direction: 158°
Humidity: 47%
Temperature:
  - Current: 32.94°C
  - High: 32.94°C
  - Low: 32.94°C
  - Feels like: 35.35°C
Rain: None
Heat index: None
Cloud cover: 94%
Thought: I have the current weather information for Beijing.
Action: Final Response
Action Input: In Beijing, the current weather is overcast clouds with a wind speed of 2.96 m/s, direction 158°, humidity 47%, temperature 32.94°C, feels like 35.35°C, no rain and cloud cover at 94%.
""")
# 4
d.append("""Question: 10,000 raised to the power of 0.5 minus 50 equals?
Thought: I should calculate the result of 10,000 raised to the power of 0.5 minus 50.
Action: Calculator
Action Input: {"input": "10000 ** 0.5 - 50"}
Observation: 50.0
Thought: Now that I have calculated the result, I should format it for the user.
Action: Final Response
Action Input: The result is 50.0
""")
# 5
d.append("""Question: Who create Spiderman?
Thought: I need to gather information about who created Spiderman.
Action: Wikipedia with question
Action Input: {"input": "Spiderman", "question": "Who created Spiderman?"}
Observation: Stan Lee and Steve Ditko created Spider-Man.
Thought: I know who created Spiderman now.
Action: Final Response
Action Input: Stan Lee and Steve Ditko created Spider-Man.
""")

CASES = []
for i, example in enumerate(d):
    instruction = example.split('Thought')[0].lstrip('Question:').strip()
    tools = set(extract_actions(example)[:-1])
    response = example[example.find('Thought'):]
    CASES.append({"id":i, "instruction":instruction, "response":response, "tools":tools})
    

