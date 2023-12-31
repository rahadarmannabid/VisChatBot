#these are the libraries we are going to use in building our app
from flask import Flask, render_template, request, jsonify, Response, render_template_string
from prompts_looping import printing, get_completion, str2dict, LM_guided_1_1, LM_guided_2_1, LM_guided_2_2,LM_guided_3_1

# Initialize the Flask application
app = Flask(__name__)
#global variables
increment = -1  #this is the serial number of the question that will be asked to chatgpt
html_code = '' # this is the html file
data = '' # this is the data associated with the html file
selected_value = '' # this is the value selected by the user from the dropdown menu

# Define a route for the default URL, which loads the form, this is the initial page
@app.route('/')
def index():
    return render_template('exp_process_selection.html')

@app.route('/exp_process', methods=['POST'])
def send_data():
    global selected_value
    selected_value = request.form['value']
    print(selected_value)
    return render_template('input.html')

#process the data from the form and send it to the progress page
@app.route('/process', methods=['POST'])
def process():
    global html_code, data, selected_value
    html_code = request.form['paragraph1']
    data = request.form['paragraph2']
    print(str(selected_value))
    if selected_value == '1-1':
        topics = LM_guided_1_1()
  
    if selected_value == '2-1':
        topics = LM_guided_2_1()
        print(topics)
    if selected_value == '2-2':
        topics = LM_guided_2_2()
        print(topics)
    if selected_value == '2-3':
        topics = LM_guided_2_1()
        print(topics)
    if selected_value == '3-1':
        topics = LM_guided_3_1()
        print(topics)

    print(topics)
    print(type(topics))
    

    return render_template("topics_all.html", topics=topics)


#this is the page where the chatbot will be displayed
@app.route('/send_data', methods=['POST'])
def send_number():
    global increment #initialize the global variable increment
    number = int(request.form['value']) #get the value from the frontend which is always 1
    increment = number + increment # we will increment each value by 1 to iterate all the questions one by one
    print('increment', increment) #print the value of increment
    response, prompt_base = printing(html_code, data, increment) #call the printing function to get the response from chatgpt, response is the output from chatgpt in dictionary format
    
    if isinstance(response, str): #if the response is a string then we will convert it into dictionary
        print("The variable is a string.") #print the value of string

        #we will convert the response into dictionary format using the get completion and str2dict function
        prompt = f"""
        Convert this response into python dictionary format. Do not use other information than python dictionary.
        The response is 
        ```{response}```
        """
        response = get_completion(prompt)
        response = str2dict(response)
        # again we will check if the response is a string or dictonary
        if isinstance(response, str):
            response = {"error": "The response is not a string."} #if not we will print the error
        else:
            pass #otherwise we will pass
    else:
        print('hello', type(response))
    # response = {'response': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.(This is a dummy response"}
    
    
    return render_template('progress.html', response=response, chart=html_code, data=data, prompt_base = prompt_base)


if __name__ == '__main__':
    app.run(port='127.0.0.1:5001',debug=True)
