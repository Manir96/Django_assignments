subject = [ 'computer', 'science', 'chamesty', 'physics',  'bangla', 'ialam', 'math', ]

while True:
    subject_list = input("What do you want? Enter Choice : read / add / update / delete / quite: ")
    if subject_list == "quite":
        print("You exist from program")
        break

#read your list
    elif subject_list == 'read':
        print("Congratulations! This is your list: ",subject)

#add your list
    elif subject_list == 'add':
        subject.append(input("Please add element to your list : "))
        print("This is your added list",subject)

#delete element from your list
    elif subject_list == 'delete':
        dl = input("Enter deleted item: ",)
        if dl in subject:
            subject.remove(dl)
        else:
            print("Not matched item")
        print("This is your deleted list",subject)

# update element from your list
    elif subject_list == 'update':
        up_wrong = input("Enter  wrong item: ", )
        up_right = input("Enter right item: ", )
        if up_wrong in subject:
            wr = subject.index(up_wrong)
            subject[wr] = up_right
        else:
            print("Not matched item")
        print("This is your updated list", subject)

#for right command
    else:
        print("Please enter right command.")