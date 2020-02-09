from tkinter import *
from tkinter import ttk

# combine the selected options into a single string to produce a label caption
def concatenate_text(list_):
    caption = ''
    for i in list_:
        caption = caption + i + ', '
    return caption

def Select():
    reslist = list()
    selecion = lbox.curselection()

    for i in selecion:
        entered = lbox.get(i)
        reslist.append(entered)
        global_list.append(entered)

    # for testing, remove later:
    print(reslist)
    print(global_list)
    v.set(concatenate_text(global_list))

# update the list box
def update_list(*args):
    search_term = search_var.get()

    # Just a generic list to populate the listbox
    lbox_list = ['Adam', 'Lucy', 'Barry', 'Bob',
                 'James', 'Frank', 'Susan', 'Amanda', 'Christie']

    lbox.delete(0, END)

    for item in lbox_list:
        if search_term.lower() in item.lower():
            lbox.insert(END, item)

# clear the selection and the displayed label caption
def clear_list():
    global v, global_list
    v.set('')
    global_list = []



root = Tk()

# create global variables
global_list = []
v = StringVar()
# set initial blank value of the StringVar
v.set('')

search_var = StringVar()
search_var.trace("w", update_list)
entry = Entry(root, textvariable=search_var, width=13)
scrollbar = ttk.Scrollbar(root, orient='vertical')
scrollbar.grid(row=1, column=1, sticky='w', ipady=30)
lbox = Listbox(root, width=45, height=6, yscrollcommand=scrollbar.set)  # selectmode=MULTIPLE

entry.grid(row=0, column=0, padx=10, pady=3)
lbox.grid(row=1, column=0, padx=10, pady=3)

# link the scrollbar to the list box
scrollbar.config(command=lbox.yview)

Button(root, text="Select", command=Select).grid(column=2, row=1)
# clear the selection and the caption
Button(root, text='clear', command=lambda:[clear_list(), update_list()]).grid(column=2, row=2)

Label(root, textvariable=v).grid(column=0, row=2)

# call the function to populate the list at the beginning
update_list()

root.mainloop()
