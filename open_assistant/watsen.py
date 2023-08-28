import openai
import numpy as np
from tqdm.auto import tqdm
from typing import List, Dict
    
      
prompt_template = """Question: {instruction}
{response}"""
    
class SimCaseSearch:
    def __init__(self, data: List[Dict], model_name: str = "text-embedding-ada-002"):
        self.data = data
        self.model_name = model_name
        self.client = openai.Embedding
        self.embeddings = None
        self.template = prompt_template

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