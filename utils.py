import re
import json
import random

def cleanTitle(str) :
    clean = ""
    for x in str : 
        if not re.match('^[\w-]+$', x):
            x = "-"
        clean += x 
    return clean

def related_articles(topic, size) : 
    dict = []
    with open("data.json", 'r') as f :
        file = json.load(f)
        i = 0
        for x in reversed(file) :
            if x['topic'] == topic :
                i += 1
                dict.append(x)
            if i == size :
                return dict
        return dict

def duplicate(title) :
    with open("data.json", 'r') as f :
        data = json.load(f)
        for x in data :
            if title == x['title'] : 
                return True
        return False

def search_matches(keyword, len) :
    dict = []
    i = 0
    with open("data.json", 'r') as f :
        data = json.load(f)
        for x in reversed(data) : 
            if keyword in x['title'] or keyword in x['topic']  :
                i += 1
                dict.append(x)
                if i == len :
                    return dict
        return dict

def home() : 
    dict = []
    i = 0
    with open("data.json", 'r') as f :
        data = json.load(f)
    for i in reversed(data) :
        dict.append(i)
        if i == 15 :
            random.shuffle(dict)
            return dict
    random.shuffle(dict)
    return dict 

