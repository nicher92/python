my_list=[["this is sentence 1", "this is sentence 2"],["this is sentence 2", "this is sentence 3"],]



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

    all_words = [word for sublist in input_list for sentence in sublist for word in sentence.split()]
    
    return all_words


print(list_comp3(my_list))