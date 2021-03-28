def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

acc = []
ds = []

_dsc = "DESCRIPTION"
_amt = "AMOUNT"
_blc = "BALANCE"
_init = "INITIAL"
_cat = "CATEGORY"
_blk = " "
block = "||"

class Record:
    """
    This is a class of Record. The commands are:
    __init__                initialize the values of categories, descriptions, and amount
    get_category            returns the value of categories
    get_description         returns the value of descriptions
    get_amount              returns the value of amounts

    """
    def __init__(self, category, description, amount):
        """
        This is Records initializer.
        Its purpose is to initialize categories, descriptions, and amounts.
        It takes self, category, description, and amount as its parameters.
        """
        self._category = category
        self._description = description
        self._amount = amount

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
            self._records = [Record(x[0], x[1], int(x[2])) for x in acc]
            ds = [(ls[0], ls[1], str(int(ls[2]))) for ls in acc]

            total = [ls._amount for ls in self._records]

            rm = sum(total) + self._initial_money
            prLightPurple("Welcome back! You now have " + str(rm) + " in your account.")

        #handles invalid format in records.txt
        #any of the other lines cannot be interpreted as a record
        except IndexError:
            #erase the contents of records.txt
            open('records.txt', 'w').close()

            prRed("Invalid format in records.txt. Deleting the contents.")

            #prompt user to input initial value
            try:
                self._initial_money = int(input("How much money do you have? "))
            
            #user inputs invalid value for money
            except ValueError:
                self._initial_money = 0
                prRed("Invalid value for money. Set to 0 by default.")

        #the first line cannot be interpreted as initial amount of money
        except ValueError:
            open('records.txt', 'w').close()
            prRed("Invalid format in records.txt. Deleting the contents.")
            try:
                self._initial_money = input("How much money do you have? ")
            
            except ValueError:
                self._initial_money = 0
                prRed("Invalid value for money. Set to 0 by default.")

        #first time executing Pymoney, no file was found
        except FileNotFoundError:
            try:
                self._initial_money = int(input("How much money do you have? "))
                
            except ValueError:
                self._initial_money = 0
                prRed("Invalid value for money. Set to 0 by default.")

    def add(self, inquiries, categories):
        """
        This is an add function.
        Its purpose is to add user's input to the records.
        Takes self, user's input (str) and the nested-list of categories and its sub-categories as parameters.
        The syntax for record input: <category> <description> <amount>
        category should be in the list of categories.
        To show the list of categories, type in "view categories".
        """
        try:
            acc.append(inquiries.split(' '))

            lst = inquiries.split(' ')
            pr1 = lst[0]
            pr2 = lst[1]
            pr3 = lst[2]
            category = pr1
            
            int_pr3 = int(pr3)

            if categories.is_category_valid(category) == True:
                self._records.append(Record(pr1, pr2, int(pr3)))
                ds = [(ls[0], ls[1], str(int(ls[2]))) for ls in acc]
                prGreen("Successfully added " + "'" + pr1 + " " + pr2 + " " + pr3 + "'" + " to your account!")

            else:
                acc.pop()
                prRed("No category named " + pr1 + "! Failed to add record")

        #user inputs string that cannot be converted to integer
        except ValueError:
            #pop user's invalid input
            acc.pop()
            prRed("Invalid value for money.\n Fail to add a record.")

        #invalid format for input
        except IndexError:
            acc.pop()
            prRed("The format of a record should be <category> <description> <amount>.\n Fail to add a record.")

    def view(self):
        """
        This is a view function.
        Its purpose is to show the currrent records to the user.
        It takes self as the parameter.
        Prints the current records.
        """
        output = ""

        #from the data structure created, take the amounts then sum them along with user's initial money
        total = [ls.get_amount for ls in self._records]
        total_str = [str(ls.get_amount) for ls in self._records]
        rm = sum(total) + self._initial_money

        #take description from the data structure
        ls = [tpl.get_description for tpl in self._records]
        ctg = [tpl.get_category for tpl in self._records]
        
        #prints the records table
        output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
        output = '\n'.join(output_list)

        print("\nHere's your expense and income records:")
        print(71*'=')
        print(f"|| {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
        print(71*'=')
        print(f"|| {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")
        print(output)
        print(71*'-')
        print(f"|| {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
        print(71*'=')
        print("Now you have " + str(rm) + " dollars.\n")


    def delete(self, dlt):
        """
        This is a delete function.
        Its purpose is to delete a record from the list of records.
        User can choose a specific record to delete if there exists multiple records of the same value.
        The syntax for record deletion: <category> <description> <amount>
        Takes self and user's input of record (str) to be deleted as a parameter.
        """
        delete = []
        output = ""

        total = [ls.get_amount for ls in self._records]
        total_str = [str(ls.get_amount) for ls in self._records]
        rm = sum(total) + self._initial_money

        ls = [tpl.get_description for tpl in self._records]
        ctg = [tpl.get_category for tpl in self._records]

        ds = [('{} {} {}'.format(i.get_category, i.get_description, i.get_amount)) for i in self._records]

        output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
        output = '\n'.join(output_list)

        #takes user's input and split by space, store in a data structure for deletion
        try:
            delete.append(dlt.split(' '))
            ds_del = [('{} {} {}'.format(dt[0], dt[1], dt[2])) for dt in delete]

            #flag to indicate that deletion has been done
            done = 0

            #to count the amount of duplicates and the value of duplicates from user's input
            ent = ds.count(ds_del[0])
            
            for dt in delete:
                cy = dt[0]
                dc = dt[1]
                am = dt[2]

            #duplicates exist
            if ent > 1:
                #let the user choose by index which specific entry the user wants to delete
                print("\nYou have " + str(ent) + " entries of " + "'" + str(cy) + " " + str(dc) + " " + str(am) + "'")

                print(75*'=')
                print(f"{block:>6s} {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
                print(75*'=')
                print(f"{block:>6s} {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")

                #shows the index
                for cnt, ele in enumerate(output_list, 1):
                    print(f"{str(cnt):<3s}", ele)

                print(75*'-')
                print(f"{block:>6s} {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
                print(75*'=')

                idx = input("\nPlease specify the entry you want to delete by entering the index of the entry: ")

                try:
                    #avoid accessing ls[-1]
                    if int(idx) == 0:
                        prRed("Index should be a number greater than 0! Fail to delete record.")

                    #index should be greater than 0 to be valid
                    elif int(idx) > 0:
                        #index input by user is out of range
                        while int(idx) > len(output_list):
                            idx = input("Entry out of range! Re-enter entry: ")

                        else:
                            #find the index that matches user's input using enumerate starting from 1
                            for cnt, ele in enumerate(output_list, 1):
                                while cnt != len(output_list):
                                    #while the entry has not been deleted
                                    if done == 0:
                                        if int(idx) == len(output_list):
                                            if ctg[int(idx)-1] != cy or ls[int(idx)-1] != dc or total_str[int(idx)-1] != am:
                                                print("Does not match the entry you want to delete! Fail to delete record")
                                                done = 1
                                                
                                            else:
                                                #delete element with corresponding index in the data structure
                                                del self._records[int(idx)-1]
                                                del ds[int(idx)-1]
                                                del acc[int(idx)-1]

                                                #count the new balance
                                                total = [ls.get_amount for ls in self._records]
                                                total_str = [int(ls.get_amount) for ls in self._records]
                                                ls = [tpl.get_description for tpl in self._records]
                                                ctg = [tpl.get_category for tpl in self._records]

                                                rm = sum(total) + self._initial_money
    
                                                output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
                                                output = '\n'.join(output_list)

                                                #empty the list
                                                delete.pop()
                                                ds_del.pop()
    
                                                #shows new record
                                                prGreen("Successfully deleted " + dc + " " + am + "!")

                                                print("\nHere's your expense and income records:")
                                                print(71*'=')
                                                print(f"|| {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
                                                print(71*'=')
                                                print(f"|| {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")
                                                print(output)
                                                print(71*'-')
                                                print(f"|| {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
                                                print(71*'=')
                                                print("Now you have " + str(rm) + " dollars.\n")
    
                                                done = 1
    
    
                                        #user's index input is found
                                        elif int(idx) == cnt:
                                            #user's index input is greater than the last index
                                            if int(idx) > len(output_list):
                                                cnt = 0
                                                prRed("Index out of range! Fail to delete record.")
                                                break
    
                                            else:
                                                if int(idx) > len(output_list):
                                                    prRed("Index out of range! Fail to delete record")
                                                    break
    
                                                #user's index input is in the range
                                                elif int(idx) <= len(output_list):
                                                    #user's index entry does not match the entry user wants to delete
                                                    while ctg[int(idx)-1] != cy or ls[int(idx)-1] != dc or total_str[int(idx)-1] != am:
                                                        cnt = 0
                                                        idx = input("Does not match the entry you want to delete! Re-enter entry: ")
    
                                                        if int(idx) == 0:
                                                            prRed("Index should be a number greater than 0! Fail to delete record.")
                                                            break

                                                        elif int(idx) > len(output_list):
                                                            prRed("Index out of range! Fail to delete record")
                                                            break

                                                    #entry and index match, deletion can be performed
                                                    else:
                                                        #delete element with corresponding index in the data structure
                                                        del self._records[int(idx)-1]
                                                        del ds[int(idx)-1]
                                                        del acc[int(idx)-1]

                                                        #count the new balance
                                                        total = [ls.get_amount for ls in self._records]
                                                        total_str = [str(ls.get_amount) for ls in self._records]
                                                        ls = [tpl.get_description for tpl in self._records]
                                                        ctg = [tpl.get_category for tpl in self._records]

                                                        rm = sum(total) + self._initial_money

                                                        output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
                                                        output = '\n'.join(output_list)

                                                        #empty the list
                                                        delete.pop()
                                                        ds_del.pop()

                                                        #shows new record
                                                        prGreen("Successfully deleted " + cy + " " + dc + " " + am + "!")
                                                        print("Here is your new record:")
                                                        print(71*'=')
                                                        print(f"|| {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
                                                        print(71*'=')
                                                        print(f"|| {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")
                                                        print(output)
                                                        print(71*'-')
                                                        print(f"|| {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
                                                        print(71*'=')
                                                        print("Now you have " + str(rm) + " dollars.\n")

                                                        done = 1

                                                else:
                                                    prRed("Attempting to delete a non-existing entry!")
                                                    done = 1

                                    elif done == 1:
                                        break

                                    cnt = cnt+1

                except ValueError:
                    prRed("Index should be a number! Fail to delete record.")


            #no duplicates, directly delete without asking for index
            elif ent == 1:
                #get the index of element to be deleted, then delete by using index
                indx = ds.index(('{} {} {}'.format(cy, dc, am)))
                del self._records[indx]
                del ds[indx]
                del acc[indx]

                #count new balance
                total = [ls.get_amount for ls in self._records]
                total_str = [str(ls.get_amount) for ls in self._records]
                ls = [tpl.get_description for tpl in self._records]
                ctg = [tpl.get_category for tpl in self._records]

                rm = sum(total) + self._initial_money

                output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
                output = '\n'.join(output_list)

                #empty the list
                delete.pop()
                ds_del.pop()

                #print new record
                prGreen("Successfully deleted " + cy + " " + dc + " " + am + "!")
                print("Here is your new record:")
                print(71*'=')
                print(f"|| {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
                print(71*'=')
                print(f"|| {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")
                print(output)
                print(71*'-')
                print(f"|| {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
                print(71*'=')
                print("Now you have " + str(rm) + " dollars.\n")
            
            #user's input does not exist
            elif ent == 0:
                #empty the list
                delete.pop()
                ds_del.pop()
                prRed("There's no record with " + cy + " " + dc + " " + am + ". Fail to delete a record.")

        #user enters wrong format
        except IndexError:
            delete.pop()
            prRed("Invalid format. Format should be <category> <description> <amount>.\n Fail to delete a record.")
                            
        
    def change(self, dlt):
        """
        This is a change function.
        Its purpose is to change a record from the list of records.
        User can choose a specific record to be changed if there exists multiple records of the same value.
        The syntax for record change: <category> <description> <amount>
        Returns the updated data structure if the record was successfully changed.
        Takes self and user's input of record (str) to be changed as a parameter.
        """

        #method is similar to deletion
        delete = []
        change = []
        output = ""
        done = 0

        total = [lis.get_amount for lis in self._records]
        total_str = [str(lis.get_amount) for lis in self._records]
        rm = sum(total) + int(self._initial_money)

        ls = [tpl.get_description for tpl in self._records]
        ctg = [tpl.get_category for tpl in self._records]

        ds = [('{} {} {}'.format(i.get_category, i.get_description, i.get_amount)) for i in self._records]
        
        output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
        output = '\n'.join(output_list)

        try:
            delete.append(dlt.split(' '))
            ds_del = [('{} {} {}'.format(dt[0], dt[1], dt[2])) for dt in delete]

            #flag to indicate that deletion has been done
            done = 0

            #to count the amount of duplicates and the value
            ent = ds.count(ds_del[0])
            for dt in delete:
                cy = dt[0]
                dc = dt[1]
                am = dt[2]

            #duplicates exist
            if ent > 1:
                #let the user choose by index which specific entry the user wants to change
                print("\nYou have " + str(ent) + " entries of " + "'" + str(cy) + " " + str(dc) + " " + str(am) + "'")

                print(75*'=')
                print(f"{block:>6s} {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
                print(75*'=')
                print(f"{block:>6s} {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")

                for cnt, ele in enumerate(output_list, 1):
                    print(f"{str(cnt):<3s}", ele)

                print(75*'-')
                print(f"{block:>6s} {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
                print(75*'=')

                idx = input("\nPlease specify the entry you want to change by entering the index of the entry: ")
            
                try:
                    if int(idx) == 0:
                        prRed("Index should be a number greater than 0! Fail to change record.")

                    elif int(idx) > 0:
                        #index input by user is out of range
                        while int(idx) > len(output_list):
                            idx = input("Entry out of range! Re-enter entry: ")

                        else:
                            #find the index that matches user's input using enumerate starting from 1
                            for cnt, ele in enumerate(output_list, 1):
                                while cnt != len(output_list):
                                    #while the entry has not been deleted
                                    if done == 0:
                                        if int(idx) == len(output_list):
                                            if ctg[int(idx)-1] != cy or ls[int(idx)-1] != dc or total_str[int(idx)-1] != am:
                                                print("Does not match the entry you want to change! Fail to delete record.")
                                                done = 1
                                            
                                            else:
                                                #ask user's input for what to change
                                                chg = input("What do you want to change " + cy + " " + dc + " " + am + " into? Enter the new category, description and the amount.\n")
                                                ch1, ch2, ch3 = chg.split()

                                                if categories.is_category_valid(ch1) == True:
                                                    change.append(chg.split(' '))
                                                    chg_del = [('{} {} {}'.format(ch[0], ch[1], int(ch[2]))) for ch in change]
                                                    chg_del1 = [(ch[0], ch[1], int(ch[2])) for ch in change]
                                                    
                                                    #delete the old value that the user changes
                                                    del self._records[int(idx)-1]
                                                    del ds[int(idx)-1]
                                                    del acc[int(idx)-1]

                                                    #insert new value that the user inputs to where deletion has been performed
                                                    self._records.insert(int(idx)-1, Record(ch1, ch2, int(ch3)))
                                                    for tup in chg_del:
                                                        ds.insert(int(idx)-1, tup)
                                                        acc.insert(int(idx)-1, tup)
                                                                            
                                                    #update new balance
                                                    total = [int(i.get_amount) for i in self._records]
                                                    total_str = [str(i.get_amount) for i in self._records]
                                                    ls = [i.get_description for i in self._records]
                                                    ctg = [i.get_category for i in self._records]

                                                    rm = sum(total) + self._initial_money

                                                    output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
                                                    output = '\n'.join(output_list)

                                                    #empty the lists
                                                    delete.pop()
                                                    ds_del.pop()

                                                    change.pop()
                                                    chg_del.pop()

                                                    #print new record
                                                    prGreen("Successfully changed " + cy + " " + dc + " " + am + "!")
                                                    print(71*'=')
                                                    print(f"|| {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
                                                    print(71*'=')
                                                    print(f"|| {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")
                                                    print(output)
                                                    print(71*'-')
                                                    print(f"|| {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
                                                    print(71*'=')
                                                    print("Now you have " + str(rm) + " dollars.\n")

                                                    done = 1

                                                else:
                                                    prRed("No category named " + ch1 + "! Failed to change record")
                                                    done = 1


                                        elif int(idx) == cnt:
                                            #user's index input does not match the entry that the user wants to change
                                            if int(idx) > len(output_list):
                                                cnt = 0
                                                prRed("Index out of range! Fail to change record.")
                                                break

                                            else:
                                                if int(idx) > len(output_list):
                                                    prRed("Index out of range! Fail to change record")
                                                    break

                                                elif int(idx) <= len(output_list):
                                                    while ctg[int(idx)-1] != cy or ls[int(idx)-1] != dc or total_str[int(idx)-1] != am:
                                                        cnt = 0
                                                        idx = input("Does not match the entry you want to change! Re-enter entry: ")

                                                        if int(idx) == 0:
                                                            prRed("Index should be a number greater than 0! Fail to change record.")
                                                            break

                                                        elif int(idx) > len(output_list):
                                                            prRed("Index out of range! Fail to change record")
                                                            break

                                                    else:
                                                        #ask user's input for what to change
                                                        chg = input("What do you want to change " + cy + " " + dc + " " + am + " into? Enter the new description and the amount.\n")
                                                        ch1, ch2, ch3 = chg.split()

                                                        if categories.is_category_valid(ch1) == True:
                                                            change.append(chg.split(' '))
                                                            chg_del = [('{} {} {}'.format(ch[0], ch[1], int(ch[2]))) for ch in change]
                                                
                                                            #delete the old value that the user changes
                                                            del self._records[int(idx)-1]
                                                            del ds[int(idx)-1]
                                                            del acc[int(idx)-1]

                                                            #insert new value that the user inputs to where deletion has been performed
                                                            self._records.insert(int(idx)-1, Record(ch1, ch2, int(ch3)))
                                                            for tup in chg_del:
                                                                ds.insert(int(idx)-1, tup)
                                                                acc.insert(int(idx)-1, tup)

                                                            #update new balance
                                                            total = [lis.get_amount for lis in self._records]
                                                            total_str = [str(lis.get_amount) for lis in self._records]
                                                            ls = [tpl.get_description for tpl in self._records]
                                                            ctg = [tpl.get_category for tpl in self._records]

                                                            rm = sum(total) + self._initial_money

                                                            output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
                                                            output = '\n'.join(output_list)

                                                            #empty the lists
                                                            delete.pop()
                                                            ds_del.pop()

                                                            change.pop()
                                                            chg_del.pop()
                                                
                                                            #print new record
                                                            prGreen("Successfully changed " + dc + " " + am + "!")
                                                            print("Here is your new record:")
                                                            print(71*'=')
                                                            print(f"|| {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
                                                            print(71*'=')
                                                            print(f"|| {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")
                                                            print(output)
                                                            print(71*'-')
                                                            print(f"|| {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
                                                            print(71*'=')
                                                            print("Now you have " + str(rm) + " dollars.\n")
                                                    
                                                            done = 1

                                                        else:
                                                            prRed("No category named " + ch1 + "! Failed to change record")
                                                            done = 1

                                                else:
                                                    prRed("Attempting to change a non-existing entry!")
                                                    done = 1

                                    elif done == 1:
                                        break

                                    cnt = cnt+1


                except ValueError:
                    prRed("Index should be a number! Fail to change record.")


            #no duplicates
            elif ent == 1:
                chg = input("What do you want to change " + cy + " " + dc + " " + am + " into? Enter the description and the amount.\n")
                
                ch1, ch2, ch3 = chg.split()

                if categories.is_category_valid(ch1) == True:
                    change.append(chg.split(' '))
                    chg_del = [('{} {} {}'.format(ch[0], ch[1], int(ch[2]))) for ch in change]

                    #gets the index of the element that the user wants to change, then remove the element from the data structure
                    indx = ds.index(('{} {} {}'.format(cy, dc, am)))
                    del self._records[indx]
                    del ds[indx]
                    del acc[indx]

                    #insert new element which is the user's input to the old position
                    self._records.insert(indx, Record(ch1, ch2, int(ch3)))
                    for tup in chg_del:
                        ds.insert(indx, tup)
                        acc.insert(indx, tup)
                   
                    #update the balance
                    total = [s.get_amount for s in self._records]
                    total_str = [str(s.get_amount) for s in self._records]
                    ls = [tpl.get_description for tpl in self._records]
                    ctg = [tpl.get_category for tpl in self._records]

                    rm = sum(total) + self._initial_money

                    output_list = [f"|| {ctg[i]:^20s} | {ls[i]:<20s} | {total_str[i]:<20s}||" for i in range(len(ls))]
                    output = '\n'.join(output_list)

                    #empty the list
                    delete.pop()
                    ds_del.pop()

                    change.pop()
                    chg_del.pop()

                    #print new record
                    prGreen("Successfully changed " + cy + " " + dc + " " + am + "!")
                    print("Here is your new record:")
                    print(71*'=')
                    print(f"|| {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
                    print(71*'=')
                    print(f"|| {_blk:^20s} | {_init:<20s} | {str(self._initial_money):<20s}||")
                    print(output)
                    print(71*'-')
                    print(f"|| {_blk:^20s} | {_blc:>20s} | {str(rm):<20s}||")
                    print(71*'=')
                    print("Now you have " + str(rm) + " dollars.\n")

                else:
                    prRed("No category named " + ch1 + "! Failed to change record")

            #user's input does not exist
            elif ent == 0:
                delete.pop()
                ds_del.pop()
                prRed("There's no record with " + cy + " " + dc + " " + am + ". Fail to change a record.")

        #invalid input by user, empty the lists
        except IndexError:
            #invalid input of new value
            if change == True:
                change.pop()
                chg_del.pop()
                delete.pop()
                ds_del.pop()

            #invalid input of old value
            else:
                delete.pop()

            prRed("Invalid format. Format should be <category> <description> <amount>.\n Fail to change a record.")

    def find(self, found):
        """
        This is a find function.
        Its purpose is to print out the records under the specific category input by the user.
        Takes self and the target category as a parameter.
        Prints the records under the specific category.
        """
        #all categories in the record
        total = [lis.get_amount for lis in self._records]
        total_str = [str(lis.get_amount) for lis in self._records]
        ls = [tpl.get_description for tpl in self._records]
        ctg = [tpl.get_category for tpl in self._records]

        #filter the categories in the record and take the ones inside the subcategories of the prompted category
        ds = [(i.get_category, i.get_description, i.get_amount) for i in self._records]
        
        found_in_list = filter(lambda N: N[0] in found, ds)
        lst_found = list(found_in_list)
        
        #for tpl in lst_found:
        ttl = [tpl[2] for tpl in lst_found]
        ttl_str = [str(tpl[2]) for tpl in lst_found]
        dscrptn = [tpl[1] for tpl in lst_found]
        ctgry = [tpl[0] for tpl in lst_found]

        ttl_int = sum(ttl)
        output_list = [f"|| {ctgry[i]:^20s} | {dscrptn[i]:<20s} | {ttl_str[i]:<20s}||" for i in range(len(ctgry))]
        output = '\n'.join(output_list)

        #print new record
        print("Here's your expense and income records under this category:")
        print(71*'=')
        print(f"|| {_cat:^20s} | {_dsc:^20s} | {_amt:^20s}||")
        print(71*'=')
        print(output)
        print(71*'-')
        print(f"|| {_blk:^20s} | {_blc:>20s} | {str(ttl_int):<20s}||")
        print(71*'=')
        print("The total amount in this category is " + str(ttl_int) + " dollars.\n")

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
            fh.write('\n'.join('{} {} {}'.format(i.get_category, i.get_description, i.get_amount) for i in self._records))

        prYellow("Thank you for using PyMoney! Do not forget to always keep track on your expenses :)")


    def save_record(self):
        """
        This is a save function.
        Its purpose is to save the current record to the file 'records.txt'.
        Takes self as the parameter.
        """

        #writes user's initial_money
        with open('records.txt', 'w') as fh:
            fh.write(str(self._initial_money) + '\n')

            #join elements by space, then newline, then write to records.txt
            fh.write('\n'.join('{} {} {}'.format(i.get_category, i.get_description, i.get_amount) for i in self._records))

        prGreen("Record saved!")


class Categories:
    """
    This is a class of Categories. The commands are:
    __init__                    initialize a nested list of categories and its sub-categories
    view                        shows user the list of categories and its sub-categories
    is_category_valid           check a sub-category's existence in a specific category
    find_subcategories          show all the sub-categories under a specific category
    """
    def __init__(self):
        """
        This is a category initializer.
        Its main purpose is to initialize categories and its sub-categories.
        Takes self as the parameter.
        """
        self._categories = ['Expense',\
                        ['Food',
                            ['meal', 'drink', 'snack', 'cafe', 'groceries']], \
                        ['Transportation',\
                            ['taxi', 'bus', 'railway']],\
                        ['Shopping',\
                            ['stationery', 'health', 'beauty', 'electronics', 'accessories', 'clothing']], \
                        ['Communication',\
                            ['internet', 'phone']], \
                        ['Finance',\
                            ['taxes', 'fines', 'insurance']], \
                    'Income',\
                        ['salary', 'bonus', 'lottery']]

    def view(self, prefix=()):
        """
        This is a category viewer.
        Its purpose is to show the user what categories can be chosen for the record inputs.
        Prints the list of categories and its sub-categories.
        """
        def view_categories(categories, prefix=()):
          if type(categories) in {list, tuple}:
              i = 0
              for elm in categories:
                  view_categories(elm, prefix+(i,))
          else:
              s = ' '*3*(len(prefix)-1)
              s += '•' + categories
              print(s)

        view_categories(self._categories)


    def is_category_valid(self, category):
        """
        This is a sub-category checker.
        Its purpose is to check a subcategory's existence in a list of categories.
        Takes self and the category to be checked as a parameter.
        Returns True if the subcategory is in the category list.
        Returns False if it is not.
        """
        def is_valid(category, categories):
          for thing in categories:
              if type(thing) == list:
                  if is_valid(category, thing):
                      return True
              if thing == category:
                  return True
          return False

        return is_valid(category, self._categories)
        

    def find_subcategories(self, category):
        """
        This is a find subcategory function.
        Its purpose is to show all the sub-categories under a specific category.
        Takes self and a category name to find as a parameter.
        Returns a non-nested list containing the specified category and all the sub-categories under it (if any).
        """
        def find_subcategories_gen(category, categories, found = False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)

                    if child == category and index + 1 < len(categories) and type(categories[index+1]) == list and found == False:
                        yield from find_subcategories_gen(category, categories[index:index+2], found = True)
            else:
                if categories == category or found == True:
                    yield categories

        return [x for x in find_subcategories_gen(category, self._categories)]


#import sys
categories = Categories()
records = Records()

while True:
    cmd = input("What do you want to do (add / view / delete / change / view categories / find / save / exit)? ")

    if cmd == "add":
      record = input("Add an expense or income records with categories, description, and amount:\n")
      records.add(record, categories)

    elif cmd == "view":
        records.view()

    elif cmd == "delete":
        records.view()
        delete_record = input("Which record do you want to delete? Enter the category, description, and the amount you want to delete.\n")
        records.delete(delete_record)

    elif cmd == "change":
        records.view()
        change_record = input("Which record do you want to change? Enter the category, description, and the amount you want to change.\n")
        records.change(change_record)

    elif cmd == "view categories":
        categories.view()

    elif cmd == "check categories":
        in_cat = input("Input category: ")
        if categories.is_category_valid(in_cat) == True:
            print("True")
        else:
            print("False")

    elif cmd == "find":
        category = input("Which category do you want to find? ")
        target_categories = categories.find_subcategories(category)
        records.find(target_categories)

    elif cmd == "find cat":
        ct = input("Input: ")
        print(categories.find_subcategories(ct))

    elif cmd == "save":
        records.save_record()

    elif cmd == "exit":
        records.save()
        break

    else:
        prRed("Invalid command. Try again.")




