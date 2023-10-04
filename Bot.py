from AddressBook import *
from abc import ABC, abstractmethod

class ActionAbstract(ABC):

    @abstractmethod
    def action():
        pass

class Abstract(ABC):
    def __init__(self, abstract: ActionAbstract):
        self.abstract = abstract


    @abstractmethod
    def action():
        pass

class Add(ActionAbstract):

    def action(self, book):        
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        print(type(book))
        book.add(record)

class Search(ActionAbstract):
    def action(self, book):    
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = (book.search(pattern, category))
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)

class Edit(ActionAbstract):
    def action(self, book): 
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        return book.edit(contact_name, parameter, new_value)
    
class Remove(ActionAbstract):
    def action(self, book):
            pattern = input("Remove (contact name or phone): ")
            return book.remove(pattern)
    
class Save(ActionAbstract):
    def action(self, book): 
            file_name = input("File name: ")
            return book.save(file_name)
    

class Load(ActionAbstract):
    def action(self, book): 
        file_name = input("File name: ")
        return book.load(file_name)
    
class Congratulate(ActionAbstract):
    def action(self, book):     
        print(book.congratulate())


    
class View(ActionAbstract):
   
    def action(self, book):
        return print(book)


class Commands():
    OPERATIONS = {
            'add': Add,
            'search': Search,
            'edit': Edit,
            'remove': Remove,
            'save': Save,
            'load': Load,
            'congratulate': Congratulate,
            'view': View,
        }

    def __init__ (self, operator):
        self.operator = operator


    def get_operation(self, operator):
        return self.OPERATIONS[operator]

class Bot(Commands, Abstract):
    def __init__(self):
        self.book = AddressBook()
  
    def handle(self, action):
        if action in Commands.OPERATIONS:
          self.action(self.get_operation(action))
        else:
            print("There is no such command!") 

    def action(self, action_dict: ActionAbstract):
        action_dict().action(self.book)