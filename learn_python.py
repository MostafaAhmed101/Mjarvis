def lists_python():

  while True:
    explain_list = {'append':'add an item to the end of the list','extend':'add a group of items to the end of the list','insert':'add an item to the list at the location that the user wants','remove':'delete the first item in the list whose value equals the value specified by the user','pop':'delete the item at the location specified by the user','clear':'delete all list items','index':'locate the item within the list','count':'specifies the frequency of the user-selected item in the list','reverse':'flip the order of the list items into place','copy':'create a superficial copy of the list','sort':'Sort the list in place by comparing list items using the < operator only(Sort the list in order)'}
    list_functions = {
    "len": "my_list = [1, 2, 3, 4, 5]; print(len(my_list)); output : 5",
    "append": "my_list = [1, 2, 3]; my_list.append(4); print(my_list);  output : [1,2,3,4]",
    "clear": "my_list = [1, 2, 3]; my_list.clear(); print(my_list)  output : []",
    "copy": "my_list = [1, 2, 3]; new_list = my_list.copy(); print(new_list)  output : [1, 2, 3]",
    "count": "my_list = [1, 2, 3, 1, 1]; count = my_list.count(1); print(count)  output : 3",
    "extend": "my_list = [1, 2, 3]; my_list.extend([4, 5]); print(my_list)  output : [1, 2, 3, 4, 5]",
    "index": "my_list = [1, 2, 3]; index = my_list.index(2); print(index)  output : 1",
    "insert": "my_list = [1, 2, 3]; my_list.insert(1, 4); print(my_list)  output : [1, 4, 2, 3]",
    "pop": "my_list = [1, 2, 3]; popped_item = my_list.pop(); print(popped_item)  output : 3",
    "remove": "my_list = [1, 2, 3]; my_list.remove(2); print(my_list)  output : [1 ,3]",
    "reverse": "my_list = [1, 2, 3]; my_list.reverse(); print(my_list)  output : [3, 2, 1]",
    "sort": "my_list = [3, 2, 1]; my_list.sort(); print(my_list)  output : [1, 2, 3]",
}

    answer = input('enter the the list function that you want me to explain to you :')
    if answer in explain_list:
      print(answer,'used to',explain_list[answer])
      answer3 = input('Do you want an example ? ')
      if answer3 == 'yes':
        print(list_functions[answer])
      elif answer3 == 'no':
        print('okay')
      else:
        print('something wrong')
    elif answer not in explain_list:
      print('the word you entered is incorrect')

    answer2 = input('------do you want any other explanation? :')
    if answer2 == 'yes':
      pass
    else:
      print('okay....bye')
      break