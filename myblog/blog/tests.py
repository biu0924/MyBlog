from django.test import TestCase

# Create your tests here.

from openai import OpenAI

# openai.api_base = "https://api.openai.com/v1" # 换成代理，一定要加 v1
# openai.api_base = "https://apikeyplus.com/v1" # 换成代理，一定要加 v1
#
# # openai.api_key = "API_KEY"
# openai.api_key = "sk-d5ZEmOs4xWfs8Mq8B151Ef66D55a4254Be0060B6E6AeA4Ba"

client = OpenAI(
    api_key="sk-d5ZEmOs4xWfs8Mq8B151Ef66D55a4254Be0060B6E6AeA4Ba",
    base_url="https://apikeyplus.com/v1",
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "你好，今天天气怎么样？"}
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)