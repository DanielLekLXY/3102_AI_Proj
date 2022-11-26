# -*- coding: utf-8 -*-
"""3102

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IXEm1zNLnixFUsxJcRUzAh3udYYfk8kb
"""

import anvil.server # import Anvil server lib
import anvil.media
import anvil
anvil.server.connect("OAPVFXXPPQMYZT3YFBUV5H4W-JYAZCJAUIZUTN3MY") # Connection uplink to Anvil Front End
from urllib.parse import urljoin
import requests
import base64
import os
import time
import urllib.parse
import cProfile
#################################################################
######################### QandA Modules #########################
#################################################################
@anvil.server.callable
def QandA_Generated(image):
    
    cProfile.runctx('Test_Caption(image)', globals(), locals(), filename=None)
    return Test_Caption(image)


@anvil.server.callable
def Caption_Function(image):
    url = 'http://captions:8080/image_captioning'
    files = {'img': image.get_bytes()}
    r = requests.post(url, files=files)
    # extracting data in json format
    data = r.json()
    return data['caption'] # Return text(str) for caption of image


@anvil.server.callable
def QnA_Function(caption):
    # caption = 'The herb is generally safe to use. There is limited research to suggest that stinging nettle is an effective remedy. Researchers need to do more studies before they can confirm the health benefits of stinging nettle.'
    # sending get request and saving the response as response object
    payload = {'captions': caption}
    QnA_Response = requests.get('http://Transformer:8888/transformer', params=payload)
    # extracting data in json format
    data = QnA_Response.json()
    for i in data:
        Question = f"{i['question']}"
        Answer = f"{i['answer']}"
        Q = Question
        A = Answer
    return [Q, A] # Return text(str) for Answer for image



#################################################################
########################## DB Modules ###########################
#################################################################
@anvil.server.callable
def Call_All_DB():
    # Code
    URL = 'http://mongo-express:8081/db/data3102/expArr/datatable?key=&value=&type=&query=&projection='
    QnA_Response = requests.get(url = URL)
    data = QnA_Response.json()

    for dx in data:
        if "image" in dx:
            try:
                #f = open('/uploads/' + dx["image"])
                dx["imagedata"] = anvil.media.from_file('/uploads/' + dx["image"], "img/png")
                #f.close()
            except:
                dx["imagedata"] = "error"
            

    return data # returns all the items in DB

@anvil.server.callable
def Search_DB():
    # Code
    return 0 # returns a specific DB item

@anvil.server.callable
def Update_DB(Caption, Answer, Question,image, id):
    URL = 'http://mongo-express:8081/db/data3102/datatable'
    # sending get request and saving the response as response object
    if not os.path.exists("/uploads"):
        os.makedirs("/uploads")
    named = str(time.time()) + "_" + image.name
    f = open('/uploads/' + named, 'wb+')
    f.write(image.get_bytes())
    f.close()

    ##id is following ObjectId('6381addcfd7141e464242296')
    mongoresult = requests.post(url = URL, data = {"_method": "put", "document": '{"id":"'+id +'" "image":"'+ named+'","question":"'+ Question +'","answer":"'+ Answer +'","caption":"'+ Caption +'"}'})

    return ("Savede: ", Caption, Answer, Question, " Image: ", image.name) # test code excutable
 

@anvil.server.callable
def Delete_DB(id):
    #http://localhost:8081/db/data3102/datatable/%226381ab55fd7141e464242294%22?skip=0&key=&value=&type=&query=&projection=
    URL = 'http://mongo-express:8081/db/data3102/datatable/' + urllib.parse.quote(id) + "?skip=0&key=&value=&type=&query=&projection="
    
    mongoresult = requests.post(url = URL, data = {"_method": 'delete'})
    
    # Code
    return 0 # Deletes a item in DB

@anvil.server.callable
def Add_DB(Caption, Answer, Question, image):
    # Function to save all 4 args into DB
    # Code
    URL = 'http://mongo-express:8081/db/data3102/datatable'
    # sending get request and saving the response as response object
    if not os.path.exists("/uploads"):
        os.makedirs("/uploads")
    named = str(time.time()) + "_" + image.name
    f = open('/uploads/' + named, 'wb+')
    f.write(image.get_bytes())
    f.close()

    mongoresult = requests.post(url = URL, data = {"document": '{"image":"'+ named+'","question":"'+ Question +'","answer":"'+ Answer +'","caption":"'+ Caption +'"}'})
    
    return ("Savede: ", Caption, Answer, Question, " Image: ", image.name) # test code excutable

def Test_Caption(image):
    # image argument should be the image object pass from the user
    # This function should then call the other function for Caption, Ques and Ans

    # Caption Function call
    Cap = Caption_Function(image)
    cProfile.runctx('Caption_Function(image)', globals(), locals(), filename=None)

    # Answer Function call
    Result = QnA_Function(caption=Cap)
    Ans = Result[1]
    Ques = Result[0]
    
    # This should return the Caption, Question and Answer
    QA_Generated = [Cap, Ans, Ques] # test code excutable
    return(QA_Generated)


#################################################################
###### Set this sever to wait forever like a restful API ########
#################################################################
anvil.server.wait_forever()

# Simple Check code of available lib in environment
# !pip freeze
