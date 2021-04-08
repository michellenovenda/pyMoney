import sys
from pyrecord import *
from pycategory import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import date

categories = Categories()
records = Records()
acc = []
init = records.get_initial()
cat = categories.get_categories()
master = tk.Tk()
master.title("PyMoney")

frame = tk.Frame(master, width=700, height=350, bg="bisque3")
frame.pack_propagate(0)
frame.pack()

_listbox = tk.Listbox(master, bg="AntiqueWhite2", width=65, height=17)
_listbox.pack()
_listbox.place(x=0, y=33)

for i, ele in enumerate (records.get_records(), 0):
    ins = f"{ele[0]:<20s} {ele[1]:<20s} {ele[2]:<20s} {ele[3]:<20s}"
    _listbox.insert(i, ins)

def flatten(L):
    if type(L) == list:
        result = []
        for child in L:
            result.extend(flatten(child))
        return result
    else:
        return [L]

def ret(*args):
    return choose_category.get()

def retidx():
    return combobox.current()

def retfind(*args):
    return select_category.get()

def retidxfind():
    return comboboxfind.current()

initial_money = tk.StringVar()
cur_amount = tk.StringVar()
txt = tk.StringVar()
input_date = tk.StringVar()
input_category = tk.StringVar()
input_description = tk.StringVar()
input_amount = tk.StringVar()
input_find = tk.StringVar()
choose_category = tk.StringVar()
select_category = tk.StringVar()
flat_cat = flatten(cat)
choose_category.set("Select category")
choose_category.trace('w', ret)
select_category.set("Select category to find")
select_category.trace('w', retfind)
input_date.set(date.today())
cur_amount.set(records.get_money())
txt.set("Now you have ")

def update():
    """
    This is an update function.
    Its purpose is to update user's initial value of money.
    The input should be integer type.
    """
    try:
        initial = int(initial_money.get())
        records.set_money(initial)
        cur_amount.set(records.get_money())
        initial_money.set("")
    except ValueError:
        messagebox.showerror("Error", "Invalid value for money.")
        cur_amount.set(records.get_money())
        initial_money.set("")

def add():
    """
    This is an add function.
    Its purpose is to add user's input to the records.
    The syntax for record input: <date (YYYY-MM-DD, optional)> <category> <description> <amount>
    category should be in the list of categories.
    """
    today = input_date.get()
    try:
        date.fromisoformat(today)
        isdate = today
        idx = retidx()
        category = flat_cat[idx]
        if categories.is_category_valid(category) == True:
            try:
                description = input_description.get()
                getamount = input_amount.get()
                amount = int(getamount)
                rec = '{} {} {} {}'.format(str(isdate), category, description, str(amount))
                ins = f"{isdate:<20s} {category:<20s} {description:<20s} {str(amount):<20s}"
                acc.append(rec)
                records.add(rec, categories)
                _listbox.insert(tk.END, ins)
                cur_amount.set(records.get_money())
                input_date.set("")
                input_category.set("")
                input_description.set("")
                input_amount.set("")
                choose_category.set("")
            except ValueError:
                messagebox.showerror("Error", "Invalid value for money.")
                input_date.set("")
                input_category.set("")
                input_description.set("")
                input_amount.set("")
                choose_category.set("")
        else:
            messagebox.showerror("Error", "No category matches your input.")

    except ValueError:
        messagebox.showwarning("Warning", "Invalid format for date.\nCorrect format is YYYY-MM-DD.\nSet to today's date by default")
        isdate = str(date.today())
        idx = retidx()
        category = flat_cat[idx]
        if categories.is_category_valid(category) == True:
            try:
                description = input_description.get()
                getamount = input_amount.get()
                amount = int(getamount)
                rec = '{} {} {} {}'.format(str(isdate), category, description, str(amount))
                ins = f"{isdate:<20s} {category:<20s} {description:<20s} {str(amount):<20s}"
                acc.append(rec)
                records.add(rec, categories)
                _listbox.insert(tk.END, ins)
                cur_amount.set(records.get_money())
                input_date.set("")
                input_category.set("")
                input_description.set("")
                input_amount.set("")
                choose_category.set("")
            except ValueError:
                messagebox.showerror("Error", "Invalid value for money.")
                input_date.set("")
                input_category.set("")
                input_description.set("")
                input_amount.set("")
                choose_category.set("")
        else:
            messagebox.showerror("Error", "No category matches your input.")

def delete():
    """
    This is a delete function.
    Its purpose is to delete a record from the list of records.
    User selects a specific record to delete.
    """
    try:
        index = _listbox.curselection()[0]
        records.delete(index)
        _listbox.delete(tk.ANCHOR)
        cur_amount.set(records.get_money())
    except IndexError:
        messagebox.showerror("Error", "Select a record to delete!")

def change():
    """
    This is a change function.
    Its purpose is to change a record from the list of records.
    User selects a specific record to change and enter the new value.
    """
    try:
        index = _listbox.curselection()[0]
        today = input_date.get()
        try:
            date.fromisoformat(today)
            isdate = today
            idx = retidx()
            category = flat_cat[idx]
            if categories.is_category_valid(category) == True:
                try:
                    description = input_description.get()
                    getamount = input_amount.get()
                    amount = int(getamount)
                    rec = '{} {} {} {}'.format(str(isdate), category, description, str(amount))
                    ins = f"{isdate:<20s} {category:<20s} {description:<20s} {str(amount):<20s}"
                    acc.append(rec)
                    records.change(index, rec, categories)
                    _listbox.delete(tk.ANCHOR)
                    _listbox.insert(tk.ANCHOR, ins)
                    cur_amount.set(records.get_money())
                    input_date.set("")
                    input_category.set("")
                    input_description.set("")
                    input_amount.set("")
                    choose_category.set("")
                except ValueError:
                    messagebox.showerror("Error", "Invalid value for money.")
                    input_date.set("")
                    input_category.set("")
                    input_description.set("")
                    input_amount.set("")
                    choose_category.set("")
            else:
                messagebox.showerror("Error", "No category matches your input.")

        except ValueError:
            messagebox.showwarning("Warning", "Invalid format for date.\nCorrect format is YYYY-MM-DD.\nSet to today's date by default")
            isdate = str(date.today())
            idx = retidx()
            category = flat_cat[idx]
            if categories.is_category_valid(category) == True:
                try:
                    description = input_description.get()
                    getamount = int(input_amount.get())
                    amount = int(getamount)
                    rec = '{} {} {} {}'.format(str(isdate), category, description, str(amount))
                    ins = f"{isdate:<20s} {category:<20s} {description:<20s} {str(amount):<20s}"
                    acc.append(rec)
                    records.change(index, rec, categories)
                    _listbox.delete(tk.ANCHOR)
                    _listbox.insert(tk.ANCHOR, ins)
                    cur_amount.set(records.get_money())
                    input_date.set("")
                    input_category.set("")
                    input_description.set("")
                    input_amount.set("")
                    choose_category.set("")
                except ValueError:
                    messagebox.showerror("Error", "Invalid value for money.")
                    input_date.set("")
                    input_category.set("")
                    input_description.set("")
                    input_amount.set("")
                    choose_category.set("")
            else:
                messagebox.showerror("Error", "No category matches your input.")
    
    except IndexError:
        messagebox.showerror("Error", "Select a record to change!")

def find():
    """
    This is a find function.
    Its purpose is to find records under a category.
    User types in the category that wants to be displayed.
    """
    idx = retidxfind()
    category = flat_cat[idx]
    if categories.is_category_valid(category):
        _listbox.delete(0, tk.END)
        target_categories = categories.find_subcategories(category)
        ds = list(records.get_records())
        found_in_list = filter(lambda N: N[1] in target_categories, ds)
        lst_found = list(found_in_list)
        ttl = [int(tpl[3]) for tpl in lst_found]
        ttl_str = [str(tpl[3]) for tpl in lst_found]
        dscrptn = [tpl[2] for tpl in lst_found]
        ctgry = [tpl[1] for tpl in lst_found]
        isdate = [tpl[0] for tpl in lst_found]
    
        ttl_int = sum(ttl)
        sum_ttl = str(ttl_int)
        cur_amount.set(sum_ttl)

        for i in range(len(ctgry)):
            ins = f"{isdate[i]:<20s} {ctgry[i]:<20s} {dscrptn[i]:<20s} {ttl_str[i]:<20s}"
            _listbox.insert(i, ins)

        txt.set("In this category, you have ")
        input_find.set("")
    else:
        messagebox.showerror("Error", "No category matches your input")
        input_find.set("")

def reset():
    """
    This is a reset function.
    Its purpose is to find reset the content of the listbox.
    User clicks the reset button and the listbox will be reset automatically.
    """
    _listbox.delete(0, tk.END)
    for i, ele in enumerate (records.get_records(), 0):
        ins = f"{ele[0]:<20s} {ele[1]:<20s} {ele[2]:<20s} {ele[3]:<20s}"
        _listbox.insert(i, ins)
    cur_amount.set(records.get_money())
    select_category.set("")
    txt.set("Now you have ")

def save():
    """
    This is a save function.
    Its purpose is to save all the records.
    User clicks the save button and the records will be saved.
    """
    records.save()
    
lbl_findcat = tk.Label(text="Find Category", bg="bisque3", fg="brown4")
lbl_findcat.pack()
lbl_findcat.place(x=0, y=0)

lbl_value = tk.Label(textvariable="Now you have 100 dollars.", bg="bisque3", fg="brown4")
lbl_value.pack()
lbl_value.place(x=0, y=325)

lbl_init = tk.Label(text="Initial Money", bg="bisque3", fg="brown4")
lbl_init.pack()
lbl_init.place(x=400, y=33)

lbl_date = tk.Label(text="Date", bg="bisque3", fg="brown4")
lbl_date.pack()
lbl_date.place(x=400, y=180)

lbl_cat = tk.Label(text="Category", bg="bisque3", fg="brown4")
lbl_cat.pack()
lbl_cat.place(x=400, y=210)

lbl_description = tk.Label(text="Description", bg="bisque3", fg="brown4")
lbl_description.pack()
lbl_description.place(x=400, y=240)

lbl_amount = tk.Label(text="Amount", bg="bisque3", fg="brown4")
lbl_amount.pack()
lbl_amount.place(x=400, y=270)

lbl_printamount = tk.Label(textvariable=txt, bg="bisque3", fg="brown4")
lbl_printamount.pack()
lbl_printamount.place(x=0, y=320)

lbl_curamount = tk.Label(textvariable=cur_amount, bg="bisque3", fg="brown4")
lbl_curamount.pack()
lbl_curamount.place(x=150, y=320)

ent_init = tk.Entry(master, textvariable=initial_money, bg="AntiqueWhite2", width=33)
ent_init.pack()
ent_init.place(x=480, y=33)

ent_date = tk.Entry(master, textvariable=input_date, bg="AntiqueWhite2", width=33)
ent_date.pack()
ent_date.place(x=480, y=180)

ent_description = tk.Entry(master, textvariable=input_description, bg="AntiqueWhite2", width=33)
ent_description.pack()
ent_description.place(x=480, y=240)

ent_amount = tk.Entry(master, textvariable=input_amount, bg="AntiqueWhite2", width=33)
ent_amount.pack()
ent_amount.place(x=480, y=270)

btn_add = tk.Button(master, text="Add a record", command=add, bg="MistyRose2", fg="sienna4", activebackground="MistyRose3", activeforeground="sienna4", width=10, height=1)
btn_add.pack()
btn_add.place(x=600, y=300)

btn_save = tk.Button(master, text="Save", command=save, bg="MistyRose2", fg="sienna4", activebackground="MistyRose3", activeforeground="sienna4", width=5, height=1)
btn_save.pack()
btn_save.place(x=550, y=300)

btn_change = tk.Button(master, text="Change", command=change, bg="MistyRose2", fg="sienna4", activebackground="MistyRose3", activeforeground="sienna4", width=5, height=1)
btn_change.pack()
btn_change.place(x=500, y=300)

btn_del = tk.Button(master, text="Delete", command=delete, bg="MistyRose2", fg="sienna4", activebackground="MistyRose3", activeforeground="sienna4", width=5, height=1)
btn_del.pack()
btn_del.place(x=350, y=320)

btn_find = tk.Button(master, text="Find", command=find, bg="MistyRose2", fg="sienna4", activebackground="MistyRose3", activeforeground="sienna4", width=5, height=1)
btn_find.pack()
btn_find.place(x=300, y=1)

btn_rst = tk.Button(master, text="Reset", command=reset, bg="MistyRose2", fg="sienna4", activebackground="MistyRose3", activeforeground="sienna4", width=5, height=1)
btn_rst.pack()
btn_rst.place(x=350, y=1)

btn_update = tk.Button(master, text="Update", command=update, bg="MistyRose2", fg="sienna4", activebackground="MistyRose3", activeforeground="sienna4", width=7, height=1)
btn_update.pack()
btn_update.place(x=623, y=58)

style = ttk.Style()
style.theme_create('custom_style', parent='alt', settings={'TCombobox':
                                                            {'configure':
                                                                {'fieldforeground': 'black',
                                                                    'selectforeground': 'black',
                                                                    'selectbackground': 'AntiqueWhite2',
                                                                    'fieldbackground': 'AntiqueWhite2',
                                                                    'background': 'AntiqueWhite2'
                                                                    }}})
style.theme_use('custom_style')

combobox = ttk.Combobox(master, textvariable=choose_category, values=['• Expense',
                                            '   • Food',
                                                '       • meal',
                                                '       • drink',
                                                '       • snack',
                                                '       • cafe',
                                                '       • groceries',
                                            '   • Transportation',
                                                '       • taxi',
                                                '       • bus',
                                                '       • railway',
                                            '   • Shopping',
                                                '       • stationery',
                                                '       • health',
                                                '       • beauty',
                                                '       • electronics',
                                                '       • accessories',
                                                '       • clothing',
                                            '   • Communication',
                                                '       • internet',
                                                '       • phone',
                                            '   • Finance',
                                                '       • taxes',
                                                '       • fines',
                                                '       • insurance',
                                        '   • Income',
                                            '   • salary',
                                            '   • bonus',
                                            '   • lottery'], width=31)
combobox['state'] = 'readonly'
combobox.pack()
combobox.place(x=480,y=210)

comboboxfind = ttk.Combobox(master, textvariable=select_category, values=['• Expense',
                                            '   • Food',
                                                '       • meal',
                                                '       • drink',
                                                '       • snack',
                                                '       • cafe',
                                                '       • groceries',
                                            '   • Transportation',
                                                '       • taxi',
                                                '       • bus',
                                                '       • railway',
                                            '   • Shopping',
                                                '       • stationery',
                                                '       • health',
                                                '       • beauty',
                                                '       • electronics',
                                                '       • accessories',
                                                '       • clothing',
                                            '   • Communication',
                                                '       • internet',
                                                '       • phone',
                                            '   • Finance',
                                                '       • taxes',
                                                '       • fines',
                                                '       • insurance',
                                        '   • Income',
                                            '   • salary',
                                            '   • bonus',
                                            '   • lottery'], width=31)
comboboxfind['state'] = 'readonly'
comboboxfind.pack()
comboboxfind.place(x=85,y=1)

master.mainloop()
records.save()


#while True:
#    cmd = input("What do you want to do (add / view / delete / change / view categories / find / save / exit)? ")

#    if cmd == "add":
#      record = input("Add an expense or income records with date (YYYY-MM-DD, optional), categories, description, and amount:\n")
#      records.add(record, categories)

#    elif cmd == "view":
#        records.view()

#    elif cmd == "delete":
#        records.view()
#        delete_record = input("Which record do you want to delete? Enter the date (YYYY-MM-DD), category, description, and the amount you want to delete.\n")
#        records.delete(delete_record)

#    elif cmd == "change":
#        records.view()
#        change_record = input("Which record do you want to change? Enter the date (YYYY-MM-DD), category, description, and the amount you want to change.\n")
#        records.change(change_record)

#    elif cmd == "view categories":
#        categories.view()

#    elif cmd == "check categories":
#        in_cat = input("Input category: ")
#        if categories.is_category_valid(in_cat) == True:
#            print("True")
#        else:
#            print("False")

#    elif cmd == "find":
#        category = input("Which category do you want to find? ")
#        target_categories = categories.find_subcategories(category)
#        records.find(target_categories)

#    elif cmd == "find cat":
#        ct = input("Input: ")
#        print(categories.find_subcategories(ct))

#    elif cmd == "save":
#        records.save_record()

#    elif cmd == "exit":
#        records.save()
#        break

#    else:
#        prRed("Invalid command. Try again.")






