import pickle

def display_menu():
    print('')
    print('Electronic Phone Book')
    print('=====================')
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delete an entry')
    print('4. List all entries')
    print('5. Save entries')
    print('6. Restore saved entries')
    print('7. Quit')
    action = input('What do you want to do (1-7)? ')
    if action == '1':
        get_entry()
    elif action == '2':
        set_entry()
    elif action == '3':
        del_entry()
    elif action == '4':
        list_entries()
    elif action == '5':
        save_entries()
    elif action == '6':
        load_entries()
    elif action == '7':
        print('Bye')
        exit()

def get_entry():
    name = input('Name: ')
    for key, value in contacts.items():
        if name == contacts[key].get('name'):
        print('Found entry for {}:\n Phone: {}, Email: {}, URL: {}'.format(contacts[key].get('name'),contacts[key].get('number'),contacts[key].get('email'), contacts[key].get('website')))
    display_menu()


def set_entry():
    name = input('Name: ')
    number = input('Phone Number: ')
    email = input('Email :')
    website = input('Website URL :')
    entry = 'entry{}'.format(entry_num + 1)
    contacts[entry] = {'name': name, 'number': number}
    display_menu()


def del_entry():
    del_name = input('Name: ')
    for key in contacts:
        if contacts[key]['name'] == del_name:
            delete_entry = key
            #print(key)
            
    del contacts[delete_entry]
    print('Deleted entry for', del_name)
    
    display_menu()


def list_entries():
    print('')
    for key, value in contacts.items():
        print('Found entry for {}:\n Phone: {}, Email: {}, URL: {}'.format(contacts[key].get('name'),contacts[key].get('number'),contacts[key].get('email'), contacts[key].get('website')))
    display_menu()
    
    
def save_entries():
    myfile = open('phonebook.pickle', 'wb')
    pickle.dump(contacts, myfile)
    myfile.close()
    print('Entries saved to phonebook.pickle')
    display_menu()
    
def load_entries():
    myfile = open('phonebook.pickle', 'rb')
    global contacts
    contacts = pickle.load(myfile)
    print('Restored save entries.')
    display_menu()


if __name__ == "__main__":
    contacts = {}

    entry_num = 0
    for key in contacts:
        entry_num += 1
    print(entry_num)

    display_menu()

