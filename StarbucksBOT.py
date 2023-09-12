#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('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')


# In[ ]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


# In[ ]:


messages =  [  
{'role':'system', 'content':'You are an assistant that speaks like Elon Musk.'},    
{'role':'user', 'content':'tell me a joke'},   
{'role':'assistant', 'content':'Why did the chicken cross the road'},   
{'role':'user', 'content':'I don\'t know'}  ]


# In[ ]:


response = get_completion_from_messages(messages, temperature=1)
print(response)


# In[ ]:


messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},    
{'role':'user', 'content':'Hi, my name is Deepak Lenka'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)


# In[ ]:


messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},    
{'role':'user', 'content':'Yes,  can you remind me, What is my name?'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)


# In[ ]:


messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},
{'role':'user', 'content':'Hi, my name is Deepak Lenka'},
{'role':'assistant', 'content': "Hi Deepak Lenka! It's nice to meet you. \
Is there anything I can help you with today?"},
{'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)


# In[ ]:


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)


# In[ ]:


import panel as pn

pn.extension()

panels = []  # collect display

context = [{'role': 'system', 'content': """
You are StarbucksBot, an automated service to take Starbucks orders. \
You first greet the customer, then collect their order, \
and ask if it's for pickup or delivery. \
You wait to collect the entire order, then summarize it and check for any final additions. \
If it's for delivery, you ask for the delivery address. \
Finally, you collect the payment.\
Make sure to clarify all coffee options, sizes, and extras to ensure accuracy. \
You respond in a friendly, conversational style. \
The menu includes: \
- Espresso (Single/Double): $2.50/$3.50 \
- Cappuccino: $4.00 \
- Latte: $4.25 \
- Mocha: $4.50 \
- Iced Coffee: $3.75 \
- Hot Chocolate: $3.75 \
- Tea (Green/Black/Herbal): $2.75 \
Extras: \
- Extra shot: $0.50 \
- Whipped cream: $0.75 \
- Caramel syrup: $0.50 \
- Vanilla syrup: $0.50 \
- Chocolate syrup: $0.50 \
- Almond milk: $0.75 \
- Soy milk: $0.75 \
- Oat milk: $0.75 \
- Cinnamon sprinkle: $0.25 \
- Nutmeg sprinkle: $0.25 \
- Cocoa powder sprinkle: $0.25 \
- Marshmallows: $0.50 \
- Whipped cream: $0.75 \
- Sugar (Brown/White): $0.25 \
- Honey: $0.50 \
- Cinnamon stick: $0.25 \
- Lemon slice: $0.25 \
Drinks: \
- Still Water: $1.50 \
- Sparkling Water: $2.00 \
""" }]

# Define the TextInput and Button
inp = pn.widgets.TextInput(value="Hi, I'd like to place an order.", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

# Replace collect_messages with the appropriate function for the Starbucks order assistant
interactive_conversation = pn.bind(your_starbucks_order_function, button_conversation)

# Create the dashboard
dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

# Change the title to reflect the Starbucks order assistant
dashboard.title = "Starbucks Order Assistant"

# Show the dashboard
dashboard.servable()


# In[ ]:


messages = context.copy()
messages.append({
    'role': 'system',
    'content': 'Create a JSON summary of the previous Starbucks order. Itemize the price for each item. '
               'The fields should be: '
               '1) coffee (include size) '
               '2) list of extras '
               '3) list of drinks (include size) '
               '4) total price '
})

response = get_completion_from_messages(messages, temperature=0)
print(response)

