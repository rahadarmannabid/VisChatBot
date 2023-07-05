#library
import openai
import pandas as pd
import os
from IPython.display import display, HTML
import json
from redlines import Redlines
from IPython.display import display, Markdown
import re
import urllib.request as urllib2
import requests
from bs4 import BeautifulSoup
from IPython.display import Javascript
from IPython.display import display, HTML
from string import Template
import json
import IPython.display as dp
import time
import ast


#gpt-4.0
openai.api_key = "sk-FMyijawHFRnfjE9IazAzT3BlbkFJX0fSTRWHl3XLD32B7z67000"




def get_completion(prompt, model='gpt-4'):
    messages = [{'role':'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
    model = model,
    messages = messages,
    temperature = 0,)
    return response.choices[0].message["content"]


def printing(html_code, data):
    ques = pd.read_csv("prompts_scatterplot.csv")
    a , b = ques.shape
    for i in range(0, a):
        prompt_base = str(ques.iloc[i][3]) + str(ques.iloc[i][4])
        prompt = f""" ```{prompt_base}```
        The html code is inside this backtick.
        ```{html_code}```
        The data associate with it is inside this backtick.
        ```{data}```
        """
        response = get_completion(prompt)
        print(response)