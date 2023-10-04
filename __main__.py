from Bot import Bot



class SaveBook():

    def save_avto(self):
        bot.book.save("avto_save")
    

class LoadBook():

    def load_avto(self):
        bot.book.load("avto_save")


class HelloMassage():

    def hello_massage(self):
        print('Hello. I am your contact-assistant. What should I do with your contacts?')


class HelpMassage():
    def help_massage (self):
        print('Type "help" for list of commands or enter your command\n')#.strip().lower()

class InputUser() :
        def input_user(self):
           return input().strip().lower()
        
class ActionList() :
        def action_in_list(self, action):
            if action in ['add', 'remove', 'edit']:
                bot.book.save("avto_save")

class CommandList():
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    def command_list(self):
        format_str = str('{:%s%d}' % ('^',20))
        for command in self.commands:
            print(format_str.format(command))

class MainMenu():

    def action_main(self):
        while True:
            HelpMassage().help_massage()
            action = InputUser().input_user()
            if action == 'exit':
                break
            elif action == 'help':
                CommandList().command_list()
            else:
                bot.handle(action)
                SaveBook.save_avto(action)





if __name__ == "__main__":
    bot = Bot()
    bot.book.load("avto_save")
    HelloMassage().hello_massage()
    main = MainMenu()
    main.action_main()

