def create_list(row,column):
    global list_of_lists
    list_of_lists = []
    for p in range(0,row):
        list = []
        for s in range(0,column):
            list.append(0)
        list_of_lists.append(list)
create_list(15,15)
while True:
    for p in list_of_lists:
        print(p)
    break
        
    
