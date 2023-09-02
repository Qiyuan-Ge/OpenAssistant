import re
import openai
import numpy as np
from tqdm.auto import tqdm
from typing import List, Dict
    
      
prompt_template_1 = """Question: {instruction}
{response}"""
    
class SimCaseSearch:
    def __init__(self, data: List[Dict], model_name: str = "text-embedding-ada-002"):
        self.data = data
        self.model_name = model_name
        self.client = openai.Embedding
        self.embeddings = None
        self.template = prompt_template_1

    def create_embeddings(self):
        embeddings = []
        for example in tqdm(self.data):
            embedding = self.client.create(model=self.model_name, input=example['instruction'])
            embeddings.append(np.array(embedding['data'][0]['embedding']))
        embeddings = np.stack(embeddings, axis=0)

        return embeddings.T   
        
    def __call__(self, query: str):
        if self.embeddings is None:
            self.embeddings = self.create_embeddings()
        embedding = self.client.create(model=self.model_name, input=query)
        query_embedding = np.array(embedding['data'][0]['embedding'])
        sim = np.matmul(query_embedding, self.embeddings)
        idx = sim.argmax()
        rec = self.data[idx]
        
        return self.template.format(instruction=rec['instruction'], response=rec['response'])


prompt_template_2 = """You are provided with a conversation history between an AI assistant and a user. Based on the context of the conversation, please predict the three most probable questions or requests the user is likely to make next.

Previous conversation history:
{conversation}

Please respond in the following format:
1. text
2. text
3. text

Your predictions:
""" 

class ConversationMimic:
    def __init__(self, model_name: str = "gpt-3.5-turbo", roles: dict = {'user':'user', 'assistant':'assistant'}):
        self.client = openai.ChatCompletion
        self.model_name = model_name
        self.roles = roles
        self.template = prompt_template_2
        
    def __call__(self, messages: List[dict], context_window_size: int = 4):
        conv_prompt = self.convert_messages_to_conversation(messages, context_window_size)
        prompt = self.template.format(conversation=conv_prompt)
        completion = self.client.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        llm_output = completion.choices[0].message.content
        pattern = r"\d+\.\s*(.+)"
        predictions = re.findall(pattern, llm_output)
        
        return predictions
    
    def convert_messages_to_conversation(self, messages: List[dict], context_window_size: int = 4):
        conv_prompt = ""
        for i, message in enumerate(messages[::-1]):
            if i == context_window_size:
                break
            if message["role"] == "assistant":
                conv_prompt = f"{self.roles['assistant']}: {message['content']}\n" + conv_prompt
            elif message["role"] == "user":
                conv_prompt = f"{self.roles['user']}: {message['content']}\n" + conv_prompt
                
        return conv_prompt
