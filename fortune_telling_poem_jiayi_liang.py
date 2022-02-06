# -*- coding: utf-8 -*-
"""Fortune-telling Poem_Jiayi Liang.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w4nr_zpSuWXzjzlW3GNfN_cNG1O4Avnv
"""

import requests
import re
from bs4 import BeautifulSoup
import random
from time import sleep

#analyze text
from textblob import TextBlob      
! python -m textblob.download_corpora
import nltk
nltk.download('punkt')

from json import detect_encoding

tarot_url = 'https://labyrinthos.co/blogs/tarot-card-meanings-list'
poem_url = 'https://www.shortpoems.org/poems/fate/'
meaning_url = 'https://www.tarot.com/tarot/cards/major-arcana'

req1 = requests.get(tarot_url)
req2 = requests.get(poem_url)
req3 = requests.get(meaning_url)

soup1 = BeautifulSoup(req1.content, 'html.parser')
soup2 = BeautifulSoup(req2.content, 'html.parser')
soup3 = BeautifulSoup(req3.content, 'html.parser')

past_number = random.randint(0,21) 
present_number = random.randint(0,21) 
future_number = random.randint(0,21) 
number = [past_number,present_number,future_number]
print(number)

tarot_elements = soup1.find_all('h3')
card_pattern = r'^.*Meaning.*$'
matches = []
for i in tarot_elements:
  matches += re.findall(card_pattern, i.text, re.MULTILINE)



for i in range(0,22):
    matches[i] = re.sub(r" Meaning ", "", matches[i])


#for i in range(0,22):
  #print(matches[i])

interpret_elements = soup1.find_all('div',class_="rte rte--indented-images")
for i in range(0,len(interpret_elements)):
  interpret_list = re.split("[:,]", interpret_elements[i].text)
  #print(interpret_list)

 # print(interpret_elements[i].text)
 # interpret_list.pop(0)
 # for i in range (-7,0):
   # interpret_list.pop(i)

interpret_elements = soup1.find_all('div',class_="rte rte--indented-images")
#for i in range(0,len(interpret_elements)):
 #interpret_list = re.split('[:,]', interpret_elements[i].text)

 # interpret_list.pop(0)
 # for i in range (-7,0):
   # interpret_list.pop(i)
  #print(interpret_list)

explanation = soup3.find_all('p')
explanation.reverse()
for i in range(0,23):
 explanation[i] = re.sub(r"Learn more.*.$","",explanation[i].text)
explanation.pop(11)
for i in range(0,22):
  explanation[i]
print (number)

past_poem = TextBlob(explanation[past_number])
verb_present1 = []
noun_s1 = [] 
noun_p1 = []                            
verb_s1 = []  
verb_p1 = []                        
adjective1 = []      


for word, tag in past_poem.tags:
   # print("%s ||%s" % (word, tag))
    if tag == "NN":           
        noun_s1.append(word)     
    elif tag == "NNS":       
        noun_p1.append(word)
    elif tag == "JJ":          
        adjective1.append(word)
    elif tag == "VBP":          
        verb_p1.append(word)
    elif tag == "VBZ":          
        verb_s1.append(word)
    

my_grammar = {
        "S": ["VP the JJ NP"],
        "JJ": adjective1,                              
        "NP": ["NN", "NNS"], 
        "VP": ['A NN VBZ','NNS VBP'],                                     
        "NN": noun_s1,
        "NNS": noun_p1,
        "VBZ": verb_s1,
        "VBP": verb_p1,
        }


def write_a_sentence(grammar, axiom):

    sentence1 = list()                                               

    if axiom in grammar:                                           
        expansion1 = random.choice(grammar[axiom])                  

        for token in expansion1.split():                             
            sentence1.extend(write_a_sentence(grammar, token))      
    else:
        sentence1.append(axiom)                                     

    return sentence1                                                


                                            
words1 = write_a_sentence(my_grammar, "S")                       
line1 = " ".join(words1)                                  
print(line1)

present_poem = TextBlob(explanation[present_number])
verb_present2 = []
noun_s2 = [] 
noun_p2 = []                            
verb_s2 = []  
verb_p2 = []                        
adjective2 = []      


for word, tag in present_poem.tags:
    #print("%s ||%s" % (word, tag))
    if tag == "NN":           
        noun_s2.append(word)     
    elif tag == "NNS":       
        noun_p2.append(word)
    elif tag == "JJ":          
        adjective2.append(word)
    elif tag == "VBP":          
        verb_p2.append(word)
    elif tag == "VBZ":          
        verb_s2.append(word)
    

my_grammar = {
        "S": ["VP the JJ NP"],
        "JJ": adjective2,                              
        "NP": ["NN", "NNS"], 
        "VP": ['A NN VBZ','NNS VBP'],                                     
        "NN": noun_s2,
        "NNS": noun_p2,
        "VBZ": verb_s2,
        "VBP": verb_p2,
        }


def write_a_sentence(grammar, axiom):

    sentence2 = list()                                               

    if axiom in grammar:                                           
        expansion2 = random.choice(grammar[axiom])                  

        for token in expansion2.split():                             
            sentence2.extend(write_a_sentence(grammar, token))      
    else:
        sentence2.append(axiom)                                     

    return sentence2                                                


                                            
words2 = write_a_sentence(my_grammar, "S")                       
line2 = " ".join(words2)                                  
#print(line2)

future_poem = TextBlob(explanation[future_number])
verb_present3 = []
noun_s3 = [] 
noun_p3 = []                            
verb_s3 = []  
verb_p3 = []                        
adjective3 = []      


for word, tag in future_poem.tags:
    #print("%s ||%s" % (word, tag))
    if tag == "NN":           
        noun_s3.append(word)     
    elif tag == "NNS":       
        noun_p3.append(word)
    elif tag == "JJ":          
        adjective3.append(word)
    elif tag == "VBP":          
        verb_p3.append(word)
    elif tag == "VBZ":          
        verb_s3.append(word)
    


my_grammar = {
        "S": ["VP the JJ NP"],
        "JJ": adjective3,                              
        "NP": ["NN", "NNS"], 
        "VP": ['A NN VBZ','NNS VBP'],                                     
        "NN": noun_s3,
        "NNS": noun_p3,
        "VBZ": verb_s3,
        "VBP": verb_p3,
        }


def write_a_sentence(grammar, axiom):

    sentence3 = list()                                               

    if axiom in grammar:                                           
        expansion3 = random.choice(grammar[axiom])                  

        for token in expansion3.split():                             
            sentence3.extend(write_a_sentence(grammar, token))      
    else:
        sentence3.append(axiom)                                     

    return sentence3                                                


                                            
words3 = write_a_sentence(my_grammar, "S")                       
line3 = " ".join(words3)                                  
#print(line3)

poem = soup2.find_all('p')
#for i in range(0,len(poem)-4):
  #print(poem[i].text)

initial_sentence1 = r'^.*[fF]ate.*\w'
initial_sentence2 = r'^.*[fF]ortune.*\w'
matches_1 = []
matches_2 = []
for i in poem:
  matches_1 += re.findall(initial_sentence1, i.text, re.MULTILINE)
for i in poem:
  matches_2 += re.findall(initial_sentence2, i.text, re.MULTILINE)

initial_sentence = matches_1 + matches_2
for i in range(0,len(initial_sentence)):
  print(initial_sentence[i])

interpret_list_past = re.split('[:,]', interpret_elements[past_number].text)
interpret_list_present = re.split('[:,]', interpret_elements[present_number].text)
interpret_list_future = re.split('[:,]', interpret_elements[future_number].text)

direction = ['upright','reversed']

tarot_past = matches[past_number]
direction_choice_past = random.choice(direction)
if (direction_choice_past == direction[0]):
    list_number_past = 1
else:
  list_number_past = interpret_list_past.index(' Reversed')+1

tarot_present = matches[present_number]
direction_choice_present = random.choice(direction)
if (direction_choice_present == direction[0]):
    list_number_present = 1
else:
  list_number_present = interpret_list_present.index(' Reversed')+1

tarot_future = matches[future_number]
direction_choice_future = random.choice(direction)
if (direction_choice_future == direction[0]):
    list_number_future = 1
else:
  list_number_future = interpret_list_future.index(' Reversed')+1



print('%s represents your Past'%tarot_past)
sleep(2)
print('The card goes %s, a sign of%s and%s'%(direction_choice_past,interpret_list_past[list_number_past],interpret_list_past[list_number_past+1]))
sleep(2)
print(line1.capitalize())
sleep(2)
print(initial_sentence[random.randint(0,len(initial_sentence)-1)])
sleep(2)
print('\n')
sleep(2)
print('%s represents your Present'%tarot_present)
sleep(2)
print('The card goes %s, a sign of%s and%s'%(direction_choice_present,interpret_list_present[list_number_present],interpret_list_present[list_number_present+1]))
sleep(2)
print(line2.capitalize())
sleep(2)
print(initial_sentence[random.randint(0,len(initial_sentence)-1)])
sleep(2)
print('\n')
sleep(2)
print('%s represents your Future'%tarot_future)
sleep(2)
print('The card goes %s, a sign of%s and%s'%(direction_choice_future,interpret_list_future[list_number_future],interpret_list_future[list_number_future+1]))
sleep(2)
print(line3.capitalize())
sleep(2)
print(initial_sentence[random.randint(0,len(initial_sentence)-1)])
sleep(2)
print('\n')