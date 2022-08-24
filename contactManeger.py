import json

contacts = []


def add_new_contact():
    name_uesr = input('Please write your name : ')
    tel = input('Please write your a number phone  : ')
    contacts.append({"name": name_uesr, "tel": tel})
    with open('c:/Users/97252/Desktop/File Python Course/HW.jason', 'r+') as add_file:
        json.dump(contacts, add_file, indent=4)
    print("a contact added")


def print_all_contacts():
    with open('c:/Users/97252/Desktop/File Python Course/HW.jason', 'r') as pac:# the full name is print all contacts
        print(json.load(pac))


def del_contact():
    delete_num = input('Which contact you want deleted ?')
    with open('c:/Users/97252/Desktop/File Python Course/HW.jason', 'r+') as dc: #the full name is Delete contact
        data = json.load(dc)
        index_delete = 0
        for i in data:
            if i['name'] == delete_num:
                del data[index_delete]
                print(data)
            index_delete += 1
        with open('c:/Users/97252/Desktop/File Python Course/HW.jason', 'w') as n_dc: #the full name is new Delete contact
            json.dump(data, n_dc, indent=4)


def search_contact():
    search_number = input('Which name you want to see number phone ?')
    with open('c:/Users/97252/Desktop/File Python Course/HW.jason', 'r') as sn: #the full name is search number
        data = json.load(sn)
        for i in data:
            if i['name'] == search_number:
                print(i.values())
            else:
                print('The contact does not exist')


def main():
    user_selection = ""
    while user_selection != "x":
        # menu
        print("a - add new contact")
        print("d - delete a contact")
        print("s - search a  contact")
        print("p - print all  contacts")
        print("x - exit")

        # get the user selection
        user_selection = input("select an option: ")
        print("The user select: "+user_selection)

        # implement the user selection
        if user_selection == "a": add_new_contact()
        if user_selection == "p": print_all_contacts()
        if user_selection == "d": del_contact()
        if user_selection == "s": search_contact()
        # if user_selection == "x": print("make a function that exit from the program")


if __name__ == "__main__":
    main()