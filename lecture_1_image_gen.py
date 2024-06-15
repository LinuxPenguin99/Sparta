'''
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ""

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.images.generate(
  model="dall-e-3",
  prompt="대나무 숲의 판다",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
'''

import os
from openai import OpenAI
from skimage import io
import matplotlib.pyplot as plt

os.environ["OPENAI_API_KEY"] = ""

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.images.generate(
  model="dall-e-3",
  prompt="대나무 숲의 판다",
  size="1024x1024",
  quality="standard",
  n=1,
)

image = io.imread(response.data[0].url)
plt.imshow(image)
plt.show()

