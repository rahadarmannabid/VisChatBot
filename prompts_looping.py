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



topic_list = """
{
    '1': 'Trend',
    '2': 'Mean',
    '3': 'Encodings',
    '4': 'Marks',
    '5': 'Types of chart',
    '6': 'Hypothesis Testing',
    '7': 'Point-wise comparisons',
    '8': 'Summary',
    '9': 'Categories Labels',
    '10': 'Regression',
    '11': 'Outliers',
    '12': 'Number of Charts',
    '13': 'Basic Introduction',
    '14': 'Complex Trend',
    '15': 'Misleading',
    '16': 'Standard Deviation',
    '17': 'Statistics',
    '18': 'Correlation',
    '19': 'Sample Size',
    '20': 'Ranges',
    '21': 'Titles',
    '22': 'Axis',
    '23': 'Axis Labels'
}


"""



learned_topics = {}

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
    
def LM_guided_1_1():
    Seq_topic_list = {'1': 'Basic Introduction', '2': 'Types of chart', '3': 'Marks', '4': 'Encodings', '5': 'Axis', '6': 'Axis Labels', '7': 'Categories Labels', '8': 'Titles', '9': 'Ranges', '10': 'Number of Charts', '11': 'Statistics', '12': 'Mean', '13': 'Standard Deviation', '14': 'Outliers', '15': 'Sample Size', '16': 'Trend', '17': 'Complex Trend', '18': 'Correlation', '19': 'Regression', '20': 'Hypothesis Testing', '21': 'Point-wise comparisons', '22': 'Misleading', '23': 'Summary'}
    return Seq_topic_list

def LM_guided_2_1():
    prompt = f"""
    As an experienced teacher, you aim to teach a student about scatter plots. The student is non-expert in data literacy, he doesn't know anything about any charts or charts idioms. The teacher showed a scatterplot. Give a list of topics so that the student needs to learn to konw different idioms and become expert interpreting data from scatterplot for education purpose.
    """

    response = get_completion(prompt)

    prompt = f"""
    Make the list of topics text consise within one-two word and convert this list into pyhton dictonary format. 
    The lists are given inside the backticks ```{response}```.
    """

    response = get_completion(prompt)
    response = str2dict(response)
    return response

def LM_guided_2_2():
    prompt = f"""
    As an experienced teacher, you aim to teach a student about scatter plots to become expert in data literacy. 
    Sequence these topics inside backticks ```{topic_list}```or add or remove other topics that help student to become expert in interpreting data from scatterplot. Convert the output inside pyhton dictonary format.
    """
    response = get_completion(prompt)
    response = str2dict(response)
    return response

def LM_guided_3_1():
    prompt = f"""
    VLAT stands for Visualization Literacy Assessment Test. It is a 45-item multiple-choice test that assesses a person's knowledge of data visualization principles and techniques. The test is divided into three sections:

    Design principles: This section assesses a person's understanding of the principles of good data visualization design, such as using color effectively, choosing the right chart type, and creating clear and concise labels.
    Interpretation: This section assesses a person's ability to interpret data visualizations, such as identifying the main message of a visualization, understanding the relationships between different data points, and identifying potential biases in a visualization.
    Creation: This section assesses a person's ability to create data visualizations, such as choosing the right chart type for a given dataset, formatting a visualization effectively, and adding annotations to a visualization.
    The VLAT is a valid and reliable measure of data visualization literacy. It has been shown to be able to distinguish between people with different levels of data visualization knowledge. However, it is important to note that the VLAT is just one measure of data visualization expertise. There are other factors that can contribute to expertise in data visualization, such as experience, creativity, and communication skills.

    Here is a table of the VLAT score ranges and their corresponding levels of expertise : 
    Score Range	Level of Expertise
    49 or below	Non-expert
    50-69	Novice
    70-79	Proficient
    80 or above	Expert

    As an experienced teacher, you aim to teach a student about scatter plots. The student's VLAT score is 0. 
    The student already learned these topics inside three backticks```{learned_topics}```. 
    What is the next one topic from this list inside backticks ```{topic_list}``` he should learn? Give the answer in python dictonary format.
    """

    response = get_completion(prompt)
    response = str2dict(response)
    print(type(response), response)
    learned_topics.update(response)
    print(learned_topics)
    return response
