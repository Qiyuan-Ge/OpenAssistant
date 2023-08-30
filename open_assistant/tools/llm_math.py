import re
import openai
import numexpr

prompt_template = """Translate a math problem into a expression that can be executed using Python's numexpr library. Use the output of running this code to answer the question.

Question: ${{Question with math problem.}}
```text
${{single line mathematical expression that solves the problem}}
```
...numexpr.evaluate(text)...
```output
${{Output of running the code}}
```
Answer: ${{Answer}}

Begin.

Question: What is 37593 * 67?
```text
37593 * 67
```
...numexpr.evaluate("37593 * 67")...
```output
2518731
```
Answer: 2518731

Question: 37593^(1/5)
```text
37593**(1/5)
```
...numexpr.evaluate("37593**(1/5)")...
```output
8.222831614237718
```
Answer: 8.222831614237718

Question: {question}
"""


class Calulator:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.client = openai.ChatCompletion
        self.model_name = model_name
        self.template = prompt_template
        
    def run(self, input: str):
        prompts = self.template.format(question=input)
        completion = self.client.create(model=self.model_name, messages=[{"role": "user", "content": prompts}])
        llm_output = completion.choices[0].message.content
        
        pattern = r'numexpr\.evaluate\("([^"]+)"\)'
        matches = re.findall(pattern, llm_output)
        expression = matches[0].strip()
          
        try:
            output = str(numexpr.evaluate(expression, global_dict={}))
        except Exception as e:
            error_msg = f'"{question}" raised error: {e}. Please try again with a valid question, such as "What is 37 * 67?"'
            return error_msg
            
        return re.sub(r"^\[|\]$", "", output)
