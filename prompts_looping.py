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


#gpt-3.5
openai.api_key = 




def get_completion(prompt, model='gpt-4'):
    messages = [{'role':'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
    model = model,
    messages = messages,
    temperature = 0,)
    return response.choices[0].message["content"]


def printing(html_code, data, number):
    ques = pd.read_csv("prompts_scatterplot.csv")
    a , b = ques.shape
    prompt_base = str(ques.iloc[number][3]) + str(ques.iloc[number][4])
    prompt = f""" ```{prompt_base}```
    The html code is inside this backtick.
    ```{html_code}```
    The data associate with it is inside this backtick.
    ```{data}```
    """
    response = get_completion(prompt)
    response = str2dict(response)
  
    return response, prompt_base


def str2dict(string_data):
    start = []
    stop = []
    for index, char in enumerate(string_data):
        if char == "{":
            start.append(index)
        if char == "}":
            stop.append(index)
      # Character not found

    try:
        a = start[0]
        b = stop[-1]
        dict_str = string_data[a : b + 1]
        dict_str = dict_str.replace("\'", "\"")
        print(dict_str)
        nested_dict = json.loads(dict_str)
        print(type(nested_dict))
        return nested_dict
    except:

        return string_data