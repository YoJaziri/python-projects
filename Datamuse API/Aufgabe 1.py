#datamuse base URL : api.datamuse.com/
#Endpoint 'word': This endpoint returns a list of words (and multiword expressions) 
#from a given vocabulary that match a given set of constraints.
#Endpoint 'sug' : words suggestion

def similar_meaning_string():
    import requests
    string = input('Enter the expression please:\n')
    list_string = string.split()
    url = 'https://api.datamuse.com/words?ml='
    for word in list_string:
        url = url+ f'{word}+'
    url = url [:-1]
    url = url + '&max=5'
    r = requests.get(url)
    requests_list = r.json()
    
    tuple_list = []
    
    for dictt in requests_list:
        paar = []
        paar.append(dictt['word'])
        paar.append(dictt['score'])
        tuplee = tuple(paar)
        tuple_list.append(tuplee)
    
    return tuple_list


test = similar_meaning_string()
print(test)




