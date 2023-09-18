def rhyme_words(word, num_results = 3):
    import requests
    import sys
    
    ''' the except funktion does not stop the exectution of the code'''
    try:
        num_results = int(num_results)
    except ValueError:
        print('Der Parameter num_results muss ein int sein. Try again')
        sys.exit()
        
    
    if isinstance(word, str) and word.isalpha():
        pass
    else:
        raise TypeError('Der Parameter word muss nur aus ein einziges Wort und alphabetic Chars sein.')
    
    
    
    url = 'https://api.datamuse.com/words?rel_rhy='+ f'{word}'
    r = requests.get(url)
    r_list = r.json()
    
    
    
    if num_results > len(r_list):
        print(f'Leider könnten nur {len(r_list)} Rhy gefunden werden:')
    elif num_results == len(r_list):
        pass
    else:
        r_list = r_list[:num_results]
        
    tuple_list = []
    
    for dictt in r_list:
        paar = []
        paar.append(dictt['word'])
        paar.append(dictt['score'])
        tuplee = tuple(paar)
        tuple_list.append(tuplee)
    
    return tuple_list
    

    
    
test = rhyme_words('grape', 30)
print(test)