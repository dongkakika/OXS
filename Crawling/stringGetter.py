import requests

def getPageString(url) :
    data = requests.get(url)
    return data.content
