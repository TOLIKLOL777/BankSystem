def filter_by_state(list_of_dicts,state='EXECUTED'):
    correct_list = []
    for i in range(0,len(list_of_dicts)-1):
        if list_of_dicts[i]['state'] == state:
            correct_list.append(list_of_dicts[i])
    return correct_list
