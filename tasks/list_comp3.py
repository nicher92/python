
#test
def list_comp3(input_list):
    """
    make this into a list comprehension

    example:
    >> list_comp3( [
                    ["this is sentence 1", "this is sentence 2"],
                    ["this is sentence 2", "this is sentence 3"],
                    ])
    >> ['this', 'is', 'sentence', '1', 'this', 'is', 'sentence', '2', 'this', 'is', 'sentence', '2', 'this', 'is', 'sentence', '3']
    """
    all_words = []
    for sublist in input_list:
        for string in sublist:
            for word in string.split():
                all_words.append(word)
                
     
    
    return all_words
