import sys
from datetime import date
from pycategory import *

acc = []
ds = []
change = []

categories = Categories()

class Record:
    """
    This is a class of Record. The commands are:
    __init__                initialize the values of categories, descriptions, and amount
    get_category            returns the value of categories
    get_description         returns the value of descriptions
    get_amount              returns the value of amounts

    """
    def __init__(self, date, category, description, amount):
        """
        This is Records initializer.
        Its purpose is to initialize categories, descriptions, and amounts.
        It takes self, category, description, and amount as its parameters.
        """
        self._date = date
        self._category = category
        self._description = description
        self._amount = amount

    @property
    def get_date(self):
        """
        This is the get_date function.
        It takes self as the parameter.
        Returns the date of the record being recorded.
        """
        return self._date


    @property
    def get_category(self):
        """
        This is the get_category function.
        It takes self as the parameter.
        Returns the categories of the record.
        """
        return self._category

    @property
    def get_description(self):
        """
        This is the get_description function.
        It takes self as the parameter.
        Returns the descriptions of the record.
        """
        return self._description

    @property
    def get_amount(self):
        """
        This is the get_amount function.
        It takes self as the parameter.
        Returns the amount of the record.
        """
        return self._amount


class Records:
    """
    Maintain a list of all the 'Record's and the initial amount of money.
    This is a class of Records. The commands are:
    __init__                get the values of records amd initial money
    add                     prompts user to input records
    view                    show the current records to the user
    delete                  delete a specific record
    change                  change a specific record
    find                    print the records under a specific category
    save                    save the current records to 'records.txt' file upon exiting the program
    save_record             save the current records to 'records.txt' file
    """

    def __init__(self):
        """
        This is Records initializer.
        Its purpose is to read the file 'records.txt' if it exists.
        If 'records.txt' does not exist, it will prompt the user to input the initial amount of money.
        It takes self as its parameter.
        """
        self._records = []

        try:
            #try opening records.txt, if there is a valid value for initial_money, store the value to amt
            fh = open('records.txt')
            self._initial_money = int(fh.readline())

            #read the previously saved records and store in acc
            for lines in fh.readlines():
                ln = lines.split(" ")
                acc.append(ln)

            #construct a data structure for description and amount
            self._records = [Record(x[0], x[1], x[2], int(x[3])) for x in acc]
            total = [ls._amount for ls in self._records]
            rm = sum(total) + self._initial_money

        #handles invalid format in records.txt
        #any of the other lines cannot be interpreted as a record
        except IndexError:
            #erase the contents of records.txt
            self._initial_money = 0
            open('records.txt', 'w').close()

        #the first line cannot be interpreted as initial amount of money
        except ValueError:
            self._initial_money = 0
            open('records.txt', 'w').close()

        #first time executing Pymoney, no file was found
        except FileNotFoundError:
            self._initial_money = 0

    def get_records(self):
        return acc

    def get_initial(self):
        print(self._initial_money)
        return self._initial_money

    def get_money(self):
        amt_money = [mon.get_amount for mon in self._records]
        total = sum(amt_money) + self._initial_money
        return total

    def set_money(self, initial):
        self._initial_money = initial
        amt_money = [mon.get_amount for mon in self._records]
        total = sum(amt_money) + self._initial_money
        return total

    def add(self, inquiries, categories):
        """
        This is an add function.
        Its purpose is to add user's input to the records.
        Takes self, user's input (str) and the nested-list of categories and its sub-categories as parameters.
        The syntax for record input: <category> <description> <amount>
        category should be in the list of categories.
        To show the list of categories, type in "view categories".
        """
        lst = inquiries.split(' ')

        if len(lst) == 4:
            try:
                date.fromisoformat(lst[0])
                today = lst[0]
                if categories.is_category_valid(lst[1]) == True:
                    try:
                        self._records.append(Record(str(today), lst[1], lst[2], int(lst[3])))
                        acc.append([str(today), lst[1], lst[2], str(int(lst[3]))])
                    #user inputs string that cannot be converted to integer
                    except ValueError:
                        prRed("Invalid value for money.\n Fail to add a record.")

                else:
                    prRed("No category named " + ls[1] + "! Failed to add record")

            except ValueError:
                today = str(date.today())
                if categories.is_category_valid(lst[1]) == True:
                    try:
                        self._records.append(Record(today, lst[1], lst[2], int(lst[3])))
                        acc.append([str(today), lst[1], lst[2], str(int(lst[3]))])
                    #user inputs string that cannot be converted to integer
                    except ValueError:
                        fail = 1

                else:
                    fail = 1

        elif len(lst) == 3:
            today = str(date.today())
            if categories.is_category_valid(lst[0]) == True:
                self._records.append(Record(today, lst[0], lst[1], int(lst[2])))
                acc.append([str(today), lst[0], lst[1], str(int(lst[2]))])

            else:
                fail = 1

        #invalid format for input
        else:
            fail = 1

    def delete(self, idx):
        del self._records[int(idx)]
        del acc[int(idx)]

        #count the new balance
        total = [ls.get_amount for ls in self._records]
        total_str = [int(ls.get_amount) for ls in self._records]
        ls = [tpl.get_description for tpl in self._records]
        ctg = [tpl.get_category for tpl in self._records]
        dates = [tpl.get_date for tpl in self._records]

        rm = sum(total) + self._initial_money

    def change(self, idx, chg, categories):
        chg_lst = chg.split(' ')

        if len(chg_lst) == 4:
            try:
                date.fromisoformat(chg_lst[0])
                today = chg_lst[0]

                if categories.is_category_valid(chg_lst[1]) == True:
                    change.append(chg.split(' '))
                    chg_del = [('{} {} {} {}'.format(ch[0], ch[1], ch[2], int(ch[3]))) for ch in change]

                    #delete the old value that the user changes
                    del self._records[int(idx)]
                    del acc[int(idx)]
                    
                    #insert new value that the user inputs to where deletion has been performed
                    self._records.insert(int(idx), Record(chg_lst[0], chg_lst[1], chg_lst[2], int(chg_lst[3])))
                    for tup in chg_del:
                        new_lst = tup.split(' ')
                        acc.insert(int(idx), new_lst)

                    #update new balance
                    total = [int(i.get_amount) for i in self._records]
                    total_str = [str(i.get_amount) for i in self._records]
                    ls = [i.get_description for i in self._records]
                    ctg = [i.get_category for i in self._records]
                    dates = [i.get_date for i in self._records]

                    rm = sum(total) + self._initial_money

                    change.pop()
                    chg_del.pop()

                else:
                    done = 1

            except ValueError:
                today = str(date.today())
    
                if categories.is_category_valid(chg_lst[0]) == True:
                    change.append(chg.split(' '))
                    chg_del = [('{} {} {} {}'.format(today, ch[0], ch[1], int(ch[2]))) for ch in change]

                    #delete the old value that the user changes
                    del self._records[int(idx)]
                    del acc[int(idx)]

                    #insert new value that the user inputs to where deletion has been performed
                    self._records.insert(int(idx), Record(chg_lst[0], chg_lst[1], chg_lst[2], int(chg_lst[3])))
                    for tup in chg_del:
                        new_lst = tup.split(' ')
                        acc.insert(int(idx), new_lst)

                    #update new balance
                    total = [int(i.get_amount) for i in self._records]
                    total_str = [str(i.get_amount) for i in self._records]
                    ls = [i.get_description for i in self._records]
                    ctg = [i.get_category for i in self._records]
                    dates = [i.get_date for i in self._records]

                    rm = sum(total) + self._initial_money

                    change.pop()
                    chg_del.pop()

                else:
                    done = 1


        elif len(chg_lst) == 3:
            today = str(date.today())

            if categories.is_category_valid(chg_lst[0]) == True:
                change.append(chg.split(' '))
                chg_del = [('{} {} {} {}'.format(today, ch[0], ch[1], int(ch[2]))) for ch in change]
            
                #delete the old value that the user changes
                del self._records[int(idx)]
                del acc[int(idx)]

                #insert new value that the user inputs to where deletion has been performed
                self._records.insert(int(idx), Record(chg_lst[0], chg_lst[1], chg_lst[2], int(chg_lst[3])))
                for tup in chg_del:
                    new_lst = tup.split(' ')
                    acc.insert(int(idx), new_lst)

                #update new balance
                total = [int(i.get_amount) for i in self._records]
                total_str = [str(i.get_amount) for i in self._records]
                ls = [i.get_description for i in self._records]
                ctg = [i.get_category for i in self._records]
                dates = [i.get_date for i in self._records]

                rm = sum(total) + self._initial_money

                change.pop()
                chg_del.pop()

            else:
                done = 1
        
        else:
            fail = 1

    def save(self):
        """
        This is a save function.
        Its purpose is to save the current record to the file 'records.txt' upon exiting the program.
        Takes self as the parameter.
        """

        #writes user's initial_money
        with open('records.txt', 'w') as fh:
            fh.write(str(self._initial_money) + '\n')

            #join elements by space, then newline, then write to records.txt
            fh.write('\n'.join('{} {} {} {}'.format(i.get_date, i.get_category, i.get_description, i.get_amount) for i in self._records))


