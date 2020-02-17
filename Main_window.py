#      _      __ _      __
#     | | /| / /| | /| / /      GREEN ANALYTICAL INDEX GENERATOR
#     | |/ |/ / | |/ |/ /       W.Wojnowski 2020
#     |__/|__/  |__/|__/        v.0.1.3
#
#

from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import LinearSegmentedColormap
from tkinter import ttk
from tkinter import filedialog
from functools import partial
import tkinter.messagebox
import webbrowser
from math import log

root = Tk()

# app title:
root.title('Analytical Method Green Index Calculator')

# default app size:
root.geometry('800x500')
root.minsize(800, 500)
# root.configure(bg='white')
# create the small icon in the task bar:
root.iconbitmap('PG_favicon.ico')


# *********************** Functions ****************************

def clearFrame(frame):
    frame.destroy()
    global rightFrame
    rightFrame = Frame(root, width=300, height=450, padx=20)
    rightFrame.pack(side=RIGHT)


# Image save dialog:
def saveImage():
    ftypes = [('PNG file', '.png'), ('JPG file', '.jpg'), ('All files', '*')]
    filename = filedialog.asksaveasfilename(filetypes=ftypes, defaultextension='.png')
    plt.savefig(filename,
                bbox_inches='tight')  # save the plot in the specified path; the 'tight' option removes the whitespace from around the figure


# temporary placeholder function:
def doNothing():
    print("ok ok I won't...")


def popup_bonus():
    win = Toplevel()
    win.wm_title("About Green Index")

    # win.iconbitmap('PG_favicon.ico')

    def callback(event):
        webbrowser.open_new(event.widget.cget("text"))

    popup_label1 = Label(win, text='v. 0.1 2020 \n(c) Gdańsk University of Technology', justify=LEFT)
    popup_label1.grid(row=0, column=0, padx=8, pady=8)

    popup_label2 = Label(win, text=r'http://www.chem.pg.edu.pl/kcha', fg='blue', cursor='hand2', justify=LEFT)
    popup_label2.grid(row=1, column=0, padx=8, pady=8)
    popup_label2.bind('<Button-1>', callback)

    popup_label3 = Label(win,
                         text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis non sem ut aliquet. Praesent tempus fringilla suscipit. Phasellus tellus massa, semper et bibendum quis, rhoncus id neque. Sed euismod consectetur elit id tristique. Sed eu nibh id ante malesuada condimentum. Phasellus luctus finibus luctus. Pellentesque mi tellus, condimentum sit amet porta sit amet, ullamcorper quis elit. Pellentesque eu mollis nulla. Quisque vulputate, sem at iaculis vehicula, dui orci aliquet lectus, in facilisis odio dolor ut leo. Vivamus convallis hendrerit est luctus ornare. Nullam augue nisi, aliquam sit amet scelerisque hendrerit, pretium vel dui. Pellentesque sed tortor mollis, imperdiet quam quis, scelerisque erat. Vestibulum quis mollis dolor.',
                         wraplength=300, justify=LEFT, bg='white')
    popup_label3.grid(row=2, column=0, padx=8, pady=8)

    popup_button = Button(win, text="Close", command=win.destroy)
    popup_button.grid(row=3, column=0, padx=8, pady=8)


def colorMapper(value):
    cmap = LinearSegmentedColormap.from_list('rg', ["red", "yellow", "green"], N=256)
    mapped_color = int(value * 255)
    color = cmap(mapped_color)
    return color

def weightChoice(row, column, tab, weightVar):

    chckbxVar = StringVar()
    chckbxVar.set('disabled')

    radioVar = IntVar()
    radioVar.set(1)
    radio_1 = ttk.Radiobutton(tab, text='1', variable=radioVar, value=1)
    radio_2 = ttk.Radiobutton(tab, text='2', variable=radioVar, value=2)
    radio_3 = ttk.Radiobutton(tab, text='3', variable=radioVar, value=3)
    radio_4 = ttk.Radiobutton(tab, text='4', variable=radioVar, value=4)

    radio_1.grid(row=row + 1, column=column, sticky='sw', padx=(70, 0))
    radio_2.grid(row=row + 1, column=column, sticky='sw', padx=(100, 0))
    radio_3.grid(row=row + 1, column=column, sticky='sw', padx=(130, 0))
    radio_4.grid(row=row + 1, column=column, sticky='sw', padx=(160, 0))

    radio_1.config(state = DISABLED)
    radio_2.config(state = DISABLED)
    radio_3.config(state = DISABLED)
    radio_4.config(state = DISABLED)

    def printRadioVar():
        print(radioVar.get())
        weightVar.set(radioVar.get())

    weight_button = ttk.Button(tab, text='Set weight', command=printRadioVar)
    weight_button.grid(row=row + 1, column=column, sticky='sw', padx=(190, 0))
    weight_button.config(state = DISABLED)

    def printCheckbox():
        print(chckbxVar.get())
        radios = (radio_1, radio_2, radio_3, radio_4)
        if chckbxVar.get() == 'disabled':
            radioVar.set(1)
            weightVar.set(1)
        for radio in radios:
            radio.config(state = DISABLED if chckbxVar.get() == 'disabled' else NORMAL)
        weight_button.config(state = DISABLED if chckbxVar.get() == 'disabled' else NORMAL)

    ttk.Checkbutton(tab, text='Modify default weights', command=lambda:[printCheckbox()], variable=chckbxVar, onvalue='enabled', offvalue='disabled').grid(row=row, column=column,
                                                                                                                                                            columnspan=4, sticky='w', padx=8,
                                                                                                                                                           pady=(60, 0))
    Label(tab, text='Weight: ').grid(row=row + 1, column = column, sticky='sw', padx=8)





# ********** Main menu ***********************************************************************************
menu = Menu(root)

# configure the menu:
root.config(menu=menu)

FileMenu = Menu(menu)
editMenu = Menu(menu)

# add drop-down functionality:
menu.add_cascade(label='File', menu=FileMenu)
FileMenu.add_command(label='Save image', command=saveImage)
FileMenu.add_command(label='Generate report', command=doNothing)
FileMenu.add_separator()
FileMenu.add_command(label='Info', command=popup_bonus)
FileMenu.add_separator()
FileMenu.add_command(label='Exit', command=doNothing)

menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Redo', command=doNothing)

# ******** Statusbar *************
status_text = 'Temporary status text'
status = Label(root, text=status_text, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# ******** Two separate frames ******
leftFrame = Frame(root, bd=1, width=300, height=450)
rightFrame = Frame(root, width=300, height=450, padx=20)
bottomFrame = Frame(root, bd=1)

leftFrame.pack(side=LEFT, anchor=N)
rightFrame.pack(side=RIGHT)
bottomFrame.pack(side=BOTTOM, anchor=W)


def destroyCanvas(canvas):
    canvas.destroy()


# ************************* Tabs ***************************
# create tabs:
tab_parent = ttk.Notebook(leftFrame, height=400)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)
tab6 = ttk.Frame(tab_parent)
tab7 = ttk.Frame(tab_parent)
tab8 = ttk.Frame(tab_parent)
tab9 = ttk.Frame(tab_parent)
tab10 = ttk.Frame(tab_parent)
tab11 = ttk.Frame(tab_parent)
tab12 = ttk.Frame(tab_parent)

# add tabs to the tab parent:
tab_parent.add(tab1, text="1")
tab_parent.add(tab2, text="2")
tab_parent.add(tab3, text="3")
tab_parent.add(tab4, text="4")
tab_parent.add(tab5, text="5")
tab_parent.add(tab6, text="6")
tab_parent.add(tab7, text="7")
tab_parent.add(tab8, text="8")
tab_parent.add(tab9, text="9")
tab_parent.add(tab10, text="10")
tab_parent.add(tab11, text="11")
tab_parent.add(tab12, text="12")

# ****** matplotlib figure ********

weight_1 = IntVar()
weight_2 = IntVar()
weight_3 = IntVar()
weight_4 = IntVar()
weight_5 = IntVar()
weight_6 = IntVar()
weight_7 = IntVar()
weight_8 = IntVar()
weight_9 = IntVar()
weight_10 = IntVar()
weight_11 = IntVar()
weight_12 = IntVar()

weight_1.set(1)
weight_2.set(1)
weight_3.set(1)
weight_4.set(1)
weight_5.set(1)
weight_6.set(1)
weight_7.set(1)
weight_8.set(1)
weight_9.set(1)
weight_10.set(1)
weight_11.set(1)
weight_12.set(1)

var_4 = 0.5

# weights = [weight_1.get(), weight_2.get(), weight_3.get(), weight_4.get(), weight_5.get(), weight_6.get(), weight_7.get(), weight_8.get(), weight_9.get(), weight_10.get(), weight_11.get(), weight_12.get()]
# labels = ['1', '2', '3', '4', '5', '6.', '7', '8', '9.', '10', '11', '12']

# colors = []  # remember to map the colors to scores later
# for i in range(0, 10, 1):
#     color = colorMapper(i / 10)
#     colors.append(color)


def pieChart():  #weights, labels, colors

    colors = [colorMapper(var_1), colorMapper(var_2), colorMapper(var_3), colorMapper(var_4), colorMapper(var_5), colorMapper(var_6), colorMapper(var_7), colorMapper(var_8), colorMapper(var_9),
              colorMapper(var_10), colorMapper(var_11), colorMapper(var_12)]

    weights = [weight_1.get(), weight_2.get(), weight_3.get(), weight_4.get(), weight_5.get(), weight_6.get(), weight_7.get(), weight_8.get(), weight_9.get(), weight_10.get(), weight_11.get(),
               weight_12.get()]
    labels = ['1', '2', '3', '4', '5', '6.', '7', '8', '9.', '10', '11', '12']

    index_value = float(entry_text.get())

    fig, ax = plt.subplots(figsize=(3, 3), dpi=150)
    ax.clear()
    ax.axis('equal')
    radius = 1.0
    pie2 = ax.pie(weights, radius=radius, colors=colors, labeldistance=(radius * 0.85), labels=labels,
                  rotatelabels=True, startangle=90, counterclock=False,
                  wedgeprops={"edgecolor": "black", 'linewidth': 1}, textprops={'fontsize': (radius * 10)})

    plt.setp(pie2[1], rotation_mode="anchor", ha="center", va="center")
    for tx in pie2[1]:
        rot = tx.get_rotation()
        tx.set_rotation(rot + 90 + (1 - rot // 180) * 180)

    circle = plt.Circle(xy=(0, 0), radius=(radius * 0.75), facecolor=colorMapper(index_value), edgecolor='black',
                        linewidth=1)
    plt.gca().add_artist(circle)

    ax.text(0.5, 0.5, str(index_value),
            verticalalignment='center', horizontalalignment='center',
            transform=ax.transAxes,
            color='black', fontsize=(radius * 40))

    fig.tight_layout()  # for exporting a compact figure

    # Pack the figure into a canvas:
    canvas = FigureCanvasTkAgg(fig, master=rightFrame)  # A tk.DrawingArea.
    plot_widget = canvas.get_tk_widget()

    plot_widget.pack(side=TOP)
    print(weight_12.get())


# **************************************

# define a temporary function to test the printing of global variables:
def print_variables():
    #variables = (var_1, var_2, var_3, var_6)
    try:
        print ('var_1: ' + str(var_1))
        print('var_2: ' + str(var_2))
        print('var_3: ' + str(var_3))
        print('var_5: ' + str(var_5))
        print('var_6: ' + str(var_6))
        print('var_7: ' + str(var_7))
        print('var_8: ' + str(var_8))
        print('var_9: ' + str(var_9))
        print('var_10: ' + str(var_10))
        print('var_11: ' + str(var_11))
        print('var_12: ' + str(var_12))
        # print('W_12: ' + str(W_12))

    except NameError:
        tkinter.messagebox.showerror(title='Name error',
                                     message='Please fill all the variables')




def tab(tab_no, text1, text2):
    Label(tab_no, text=text1, wraplength=300, justify=LEFT).grid(sticky='w', row=0, column=0, padx=8, pady=8)
    Label(tab_no, text=text2, wraplength=300, justify=LEFT).grid(sticky='w', row=1, column=0, padx=8, pady=8)


# *****************************************************************************************************************
#               TAB 1
# *****************************************************************************************************************
content_1 = tab(tab1, text1='Direct analytical techniques should be applied to avoid sample treatment.',
                text2='Select the sampling procedure:')

# Create a Tkinter variable
var_1_text = StringVar(tab1)
# Dictionary with options
var_1_text_choices = {'Remote sensing without sample damage': 1.0,
                      'Remote sensing with little physical damage': 0.95,
                      'Non-invasive analysis': 0.9,
                      'In-field sampling and direct analysis': 0.85,
                      'In-field sampling and on-line analysis': 0.78,
                      'On-line analysis': 0.70,
                      'At-line analysis': 0.60,
                      'Off-line analysis': 0.48,
                      'External sample pre- and treatment and batch analysis (reduced number of steps)': 0.30,
                      'External sample pre- and treatment and batch analysis (large number of steps)': 0.0}
var_1_text.set('SAMPLING PROCEDURE')

dropDown_1 = OptionMenu(tab1, var_1_text, *var_1_text_choices.keys())
dropDown_1.config(wraplength=250, bg='white', justify=LEFT, width=40, anchor='w')
dropDown_1.grid(sticky='w', row=2, column=0, padx=8, pady=8)


# on change dropdown value, get the dictionary value and modify the global variable
def change_dropdown_1(*args):
    # Define the global variable for Principle 1:
    global var_1
    var_1 = None
    var_1 = var_1_text_choices[var_1_text.get()]
    print('var_1:' + str(var_1))

# link function to change dropdown
# The trace method of the StringVar allows to detect the change in the variable that activate a call to a function
var_1_text.trace('w', change_dropdown_1)

W_1 = weightChoice(10, 0, tab1, weight_1)

# *****************************************************************************************************************
#               TAB 2
# *****************************************************************************************************************

content_2 = tab(tab2, text1='Direct analytical techniques should be applied to avoid sample treatment.',
                text2='Enter the amount of sample in either g or mL:')

amount_var = StringVar()
amount_var.set('input')
sample_amount_entry = ttk.Entry(tab2, textvariable=amount_var, width=15).grid(sticky='w', row=2, column=0, padx=8, pady=8)



def change_entry_2():
    global var_2
    var_2 = None

    try:
        if float(amount_var.get()) > 100:
            var_2 = 0
        elif float(amount_var.get()) < 0.1:
            var_2 = 1.0
        else:
            var_2 = abs(-0.142 * log(float(amount_var.get())) + 0.65)   # absolute value to avoid negative values
        print('var_2:' + str(var_2))

    except ValueError:
        tkinter.messagebox.showerror(title='Value error', message='The amount has to be a float or an intiger, e.g. 0.14 or 21.')

# amount_var.trace('w', change_entry_2())
ttk.Button(tab2, text='Set', command=change_entry_2).grid(row=2, column=0, padx=8, pady=8)

W_2 = weightChoice(10, 0, tab2, weight_2)

# *****************************************************************************************************************
#               TAB 3
# *****************************************************************************************************************

content_3 = tab(tab3, 'If possible, measurements should be performed in situ',
                'What is the positioning of the analytical device?')

# Create a Tkinter variable
var_3_text = StringVar(tab3)
# Dictionary with options
var_3_text_choices = {'off-line': 0,
                      'at-line': 0.33,
                      'on-line': 0.66,
                      'in-line': 1.0}

var_3_text.set('off-line')

dropDown_3 = OptionMenu(tab3, var_3_text, *var_3_text_choices.keys())
dropDown_3.config(wraplength=250, bg='white', justify=LEFT, width=40, anchor='w')
dropDown_3.grid(sticky='w', row=2, column=0, padx=8, pady=8)


# on change dropdown value, get the dictionary value and modify the global variable
def change_dropdown_3(*args):
    global var_3
    var_3 = None
    var_3 = var_3_text_choices[var_3_text.get()]
    print('var_3:' + str(var_3))

# link function to change dropdown
# The trace method of the StringVar allows to detect the change in the variable that activate a call to a function
var_3_text.trace('w', change_dropdown_3)

W_3 = weightChoice(10, 0, tab3, weight_3)


# *************************** TAB 4 ************************************************************************************


W_4 = weightChoice(10, 0, tab4, weight_4)

# *****************************************************************************************************************
#               TAB 5
# *****************************************************************************************************************
content_5 = tab(tab5, text1='Automated and miniaturized methods should be selected.', text2='Degree of automation:')

# Create a Tkinter variable
var_5a_text = StringVar(tab5)
# Dictionary with options
var_5a_text_choices = {'automatic': 1.0,
                      'semi-automatic': 0.5,
                      'manual': 0.0}

var_5a_text.set('select')

dropDown_5a = OptionMenu(tab5, var_5a_text, *var_5a_text_choices.keys())
dropDown_5a.config(wraplength=250, bg='white', justify=LEFT, width=40, anchor='w')
dropDown_5a.grid(sticky='w', row=2, column=0, padx=8, pady=8)

# on change dropdown value, get the dictionary value and modify the global variable
def change_dropdown_5a(*args):
    global var_5a
    var_5a = None
    var_5a = var_5a_text_choices[var_5a_text.get()]
    print('var_5a:' + str(var_5a))

# link function to change dropdown
# The trace method of the StringVar allows to detect the change in the variable that activate a call to a function
var_5a_text.trace('w', change_dropdown_5a)

Label(tab5, text='Sample preparation:', wraplength=300, justify=LEFT).grid(sticky='w', row=3, column=0, padx=8, pady=8)

var_5b_text = StringVar(tab5)
var_5b_text_choices = {'miniaturized': 1.0,
                      'not miniaturized': 0.0}
var_5b_text.set('select')
dropDown_5b = OptionMenu(tab5, var_5b_text, *var_5b_text_choices.keys())
dropDown_5b.config(wraplength=250, bg='white', justify=LEFT, width=40, anchor='w')
dropDown_5b.grid(sticky='w', row=4, column=0, padx=8, pady=8)
def change_dropdown_5b(*args):
    global var_5b
    var_5b = None
    var_5b = var_5b_text_choices[var_5b_text.get()]
    print('var_5b:' + str(var_5b))
    global var_5
    var_5 = var_5a * var_5b
    print('var_5:' + str(var_5))
var_5b_text.trace('w', change_dropdown_5b)

W_5 = weightChoice(10, 0, tab5, weight_5)


# *****************************************************************************************************************
#               TAB 6
# *****************************************************************************************************************
content_6 = tab(tab6, text1='Derivatization should be avoided.', text2='Select the derivatization agents used:')

# combine the selected options into a single string to produce a label caption
def concatenate_text(list_):
    caption = ''
    for i in list_:
        caption = caption + i + '; '
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

    global var_6
    var_6 = 0.0

    for CAS in global_list:
        var_6 += lbox_list[CAS]

    print(var_6)


# update the list box
def update_list(*args):
    search_term = search_var.get()

    # Duplicates in the list!!!


    lbox.delete(0, END)

    for item in lbox_list.keys():
        if search_term.lower() in item.lower():
            lbox.insert(END, item)



# clear the selection and the displayed label caption
def clear_list():
    global v, global_list
    v.set('')
    global_list = []

# create global variables
global_list = []
# remove duplicates!!!
lbox_list = {"None": 1,
             "5950-69-6": 1,
             "30084-90-3": 1,
             "12093-10-6": 1,
             "6283-74-5": 1,
             "119-53-9": 1,
             "126-81-8": 1,
             "24257-93-0": 1,
             "58068-85-2": 0.949158975023003,
             "1273-85-4": 0.949158975023003,
             "4233-33-4": 0.949158975023003,
             "100-10-7": 0.949158975023003,
             "38183-12-9": 0.945068038553621,
             "41468-25-1": 0.937140592655187,
             "1395920-13-4": 0.937140592655187,
             "521-24-4": 0.937140592655187,
             "56606-21-4": 0.935584744799731,
             "65-22-5": 0.925393321432741,
             "68123-33-1": 0.925393321432741,
             "913253-56-2": 0.913914155272091,
             "124522-09-4": 0.913914155272091,
             "223463-14-7": 0.902699986612441,
             "1118-68-9": 0.901394170230429,
             "952102-12-4": 0.901394170230429,
             "536-69-6": 0.901394170230429,
             "203256-20-6": 0.901394170230429,
             "86516-36-1": 0.899210326049394,
             "861881-76-7": 0.886368566581839,
             "56139-74-3": 0.869932201280637,
             "84806-27-9": 0.865490140567591,
             "91366-65-3": 0.865490140567591,
             "67229-93-0": 0.855427480281241,
             "1273-82-1": 0.855042238169516,
             "50632-57-0": 0.846792397075292,
             "10199-89-0": 0.839008465483774,
             "152111-91-6": 0.836037308222637,
             "7149-49-7": 0.830362674910287,
             "3029-19-4": 0.830362674910287,
             "68572-87-2": 0.829473879117877,
             "12152-94-2": 0.829473879117877,
             "29270-56-2": 0.829154698457689,
             "24463-19-2": 0.827803622060042,
             "100-39-0": 0.825375773537705,
             "550-44-7": 0.822230968349539,
             " 49759-20-8": 0.822230968349539,
             "38609-97-1": 0.822230968349539,
             "35661-51-9": 0.822230968349539,
             "10401-59-9": 0.822230968349539,
             "70402-14-1": 0.822230968349539,
             "131076-14-7": 0.822230968349539,
             "214147-22-5": 0.822230968349539,
             "4930-98-7": 0.822230968349539,
             "569355-30-2": 0.822230968349539,
             "53348-04-2": 0.820406195102248,
             "67580-39-6": 0.818423316626862,
             "68133-98-2": 0.814016502590708,
             "81864-15-5": 0.814016502590708,
             "113722-81-9": 0.814016502590708,
             "15537-71-0": 0.809079828950995,
             "33008-06-9": 0.809079828950995,
             "139332-64-2": 0.809079828950995,
             "62642-61-9": 0.806764775754175,
             "100139-54-6": 0.806764775754175,
             "62796-29-6": 0.797901423240715,
             "87-13-8": 0.783298381421747,
             "35231-44-8": 0.778837259389339,
             "88404-25-5": 0.778837259389339,
             "485-47-2": 0.77674392680131,
             "58520-45-9": 0.776282830117383,
             "107-91-5": 0.776282830117383,
             "139332-66-4": 0.776282830117383,
             "89-25-8": 0.776282830117383,
             "18428-76-7": 0.776282830117383,
             "20624-25-3": 0.763216179776723,
             "27072-45-3": 0.762516465156704,
             "1459205-36-7": 0.755628677634781,
             "96483-68-0": 0.747181595887401,
             "132098-76-1": 0.747181595887401,
             "98-59-9": 0.746227267824334,
             "7612-98-8": 0.744246233476037,
             "5415-58-7": 0.742560985030801,
             "76-83-5": 0.740506239181083,
             "1293-79-4": 0.740506239181083,
             "28920-43-6": 0.740506239181083,
             "100-07-2": 0.740506239181083,
             "70-11-1": 0.738962425018157,
             "99-73-0": 0.738962425018157,
             "22265-37-8": 0.737084384687495,
             "3731-51-9": 0.737084384687495,
             "141903-34-6": 0.737084384687495,
             "122-04-3": 0.732376041854033,
             "4755-50-4": 0.732376041854033,
             "99-33-2": 0.732376041854033,
             "100-11-8": 0.729578106327056,
             "605-65-2": 0.723192330411814,
             "56512-49-3": 0.723192330411814,
             "126565-42-2": 0.723192330411814,
             "7693-46-1": 0.721322673837572,
             "1711-06-4": 0.717883414280986,
             "93128-04-2": 0.717798274857161,
             "613-54-7": 0.716357636495872,
             "74367-78-5": 0.710065827927279,
             "107474-79-3": 0.706189691216888,
             "119-26-6": 0.692633685424727,
             "2508-19-2": 0.692425832968952,
             "21614-17-5": 0.682522312223409,
             "80-11-5": 0.681782236352849,
             "100-46-9": 0.679263084173718,
             "55486-13-0": 0.666338980106273,
             "16315-59-6": 0.665281844920184,
             "5102-79-4": 0.664748970983542,
             "70-34-8": 0.664086673111964,
             "132-32-1": 0.659883743356088,
             "36410-81-8": 0.659179085176979,
             "100-16-3": 0.659159320154698,
             "104077-15-8": 0.659091847163412,
             "4083-64-1": 0.649947842697737,
             "21324-39-0": 0.634865149902982,
             "2978-11-2_": 0.629540812510628,
             "456-27-9": 0.628988106517093,
             "98-09-9": 0.628032387327697,
             "103-72-0": 0.606674230911606,
             "504-29-0": 0.587444277328904,
             "86-84-0": 0.566544585073271,
             "36877-69-7": 0.556132009449506,
             "108-24-7": 0.529128889489181,
             "103-71-9": 0.525453097624119,
             "551-06-4": 0.510591749035237,
             "643-79-8": 0.486298449205041,
             "98-88-4": 0.475562851988167,
             "5470-11-1": 0.466906948575218,
             "99-65-0": 0.414382740812551,
             "95-54-5": 0.409876625997181,
             "60-24-2": 0.380580959884422,
             "1118-71-4": 1,
             "4426-47-5": 0.98287765750619,
             "35342-88-2": 0.934408589712128,
             "13435-12-6": 0.934408589712128,
             "122-51-0": 0.90808769546171,
             "17455-13-9": 0.898290310316299,
             "7449-74-3": 0.896162794934563,
             "1188-33-6": 0.873968193624155,
             "1133-63-7": 0.845047181007906,
             "57981-02-9": 0.843544327015115,
             "3449-26-1": 0.831289869514086,
             "54925-64-3": 0.831289869514086,
             "7453-26-1": 0.831289869514086,
             "23231-91-6": 0.82477424558194,
             "423-39-2": 0.821174784952006,
             "3332-29-4": 0.817379220173597,
             "18297-63-7": 0.804205531712304,
             "13257-81-3": 0.796997494513717,
             "73980-71-9": 0.796226219175859,
             "828-73-9": 0.796226219175859,
             "36805-97-7": 0.785921382127458,
             "6006-65-1": 0.785921382127458,
             "4909-78-8": 0.785921382127458,
             "920-68-3": 0.785921382127458,
             "653-37-2": 0.78349900067157,
             "422-05-9": 0.78349900067157,
             "2182-66-3": 0.766534069464941,
             "354-64-3": 0.763789874990475,
             "58479-61-1": 0.763598909336104,
             "13154-24-0": 0.763598909336104,
             "70-11-1": 0.761090045768687,
             "723336-86-5": 0.761090045768687,
             "850418-19-8": 0.761090045768687,
             "850418-20-1": 0.761090045768687,
             "1546-79-8": 0.758242430472499,
             "24589-78-4": 0.758242430472499,
             "53296-64-3": 0.758242430472499,
             "77377-52-7": 0.758242430472499,
             "82112-21-8": 0.757927402509425,
             "375-22-4": 0.756114760094685,
             "336-59-4": 0.756114760094685,
             "356-42-3": 0.756114760094685,
             "420-37-1": 0.75205982910284,
             "77-76-9": 0.750711985826051,
             "20082-71-7": 0.749832128609721,
             "2251-50-5": 0.747481224283863,
             "100-11-8": 0.745015119615777,
             "18162-48-6": 0.743146183479067,
             "425-75-2": 0.742441949845756,
             "1765-40-8": 0.742441949845756,
             "76437-40-6": 0.742441949845756,
             "80522-42-5": 0.742441949845756,
             "1538-75-6": 0.74152936540163,
             "98-03-3": 0.739537905180287,
             "87020-42-6": 0.737007165264001,
             "589-15-1": 0.736264650708209,
             "2857-97-8": 0.736016815715654,
             "17950-40-2": 0.732111366794642,
             "407-25-0": 0.731258587142799,
             "115-20-8": 0.730613289210088,
             "823-96-1": 0.721670319376414,
             "71735-32-5": 0.7183910746808,
             "333-27-7": 0.7183910746808,
             "996-50-9": 0.714539433160182,
             "3768-58-9": 0.714539433160182,
             "685-27-8": 0.713300737795531,
             "25561-30-2": 0.713300737795531,
             "124-41-4": 0.70689269806413,
             "15933-59-2": 0.705803556150421,
             "18156-74-6": 0.705803556150421,
             "123-62-6": 0.703483768736821,
             "2083-91-2": 0.703043095426246,
             "10416-59-8": 0.700353286433786,
             "69739-34-0": 0.696757084764058,
             "107-46-0": 0.696026303459663,
             "541-88-8": 0.680085578563036,
             "994-30-9": 0.659639561940176,
             "75-26-3": 0.65077439166517,
             "543-27-1": 0.643008761928377,
             "6092-54-2": 0.619827404668639,
             "76-02-8": 0.618803077595292,
             "75-77-4": 0.606190113014358,
             "7719-09-7": 0.598432942089881,
             "1066-35-9": 0.590259358282054,
             "4637-24-5": 0.587695662266982,
             "920-66-1": 0.5835440122017,
             "8077-35-8": 0.580905093441462,
             "108-24-7": 0.56539851162607,
             "10294-34-5": 0.546920496297807,
             "999-97-3": 0.539120875551113,
             "7637-07-2": 0.536295783559384,
             "75-89-8": 0.517064147633066,
             "1899-02-1": 0.453968334570473,
             "17287-03-5": 0.450591161239778,
             "7664-93-9": 0.430740368201206,
             "132228-87-6": 0.389860157052623,
             "75-59-2": 0.35207841911058,
             "77-78-1": 0.185707987424391,
             "19132-06-0": 1,
             "1052236-86-8": 1,
             "135806-59-6": 1,
             "139658-04-1": 1,
             "108031-79-4": 1,
             "124529-02-8": 0.789788397239459,
             "124529-07-3": 0.789788397239459,
             "24277-43-8": 0.789788397239459,
             "958300-06-6": 0.789788397239459,
             "5978-70-1": 0.661143997568766,
             "3886-70-2": 0.62276366189702,
             "20445-31-2": 0.616318224518582,
             "17257-71-5": 0.616318224518582,
             "81655-41-6": 0.616318224518582,
             "21451-74-1": 0.616318224518582,
             "14645-24-0": 0.616318224518582,
             "147948-52-5": 0.581990910059596,
             "104371-20-2": 0.581990910059596,
             "132679-61-9": 0.56145194750795,
             "210529-62-7": 0.56145194750795,
             "3347-90-8": 0.550846501071722,
             "104530-16-7": 0.547959104197752,
             "39637-74-6": 0.547959104197752,
             "39262-22-1": 0.52022184149657,
             "1517-69-7": 0.474716248097616,
             "1445-91-6": 0.474716248097616,
             "107474-79-3": 0.437963083473382,
             "14602-86-9": 0.412055011328408,
             "3886-69-9": 0.358144912356212,
             "2627-86-3": 0.326740839342668,
             "24277-44-9": 0.288185973785988,
             "62414-75-9": 0.288185973785988,
             "14152-97-7": 0.288185973785988,
             "42340-98-7": 0.176714727821325,
             "14649-03-7": 0.132441393121765,
             "33375-06-3": 0.116078677380125,
             }
v = StringVar()

# set initial blank value of the StringVar
v.set('')

search_var = StringVar()
search_var.trace("w", update_list)
entry = ttk.Entry(tab6, textvariable=search_var, width=13)
scrollbar = ttk.Scrollbar(tab6, orient='vertical')
scrollbar.grid(row=3, column=2, sticky='w', ipady=30)
lbox = Listbox(tab6, width=34, height=6, yscrollcommand=scrollbar.set)  # selectmode=MULTIPLE

Label(tab6, text='CAS lookup: ').grid(row=2, column=0, padx=8, pady=3, sticky='w')
entry.grid(row=2, column=0, padx=24, pady=3, sticky='e')
lbox.grid(row=3, column=0, padx=8, pady=3, sticky='w')

# link the scrollbar to the list box
scrollbar.config(command=lbox.yview)

ttk.Button(tab6, text="Select", command=Select, width=8).grid(column=3, row=3, padx=4)
# clear the selection and the caption
ttk.Button(tab6, text='Clear', command=lambda:[clear_list(), update_list()], width=8).grid(column=3, row=4, padx=4)

Label(tab6, text='Selected CAS: ').grid(column=0, row=4, sticky='w', padx=8, pady=0)
ttk.Label(tab6, textvariable=v, wraplength=180, width=34, relief='groove').grid(column=0, row=5, sticky='w', padx=8, pady=4)

# call the function to populate the list at the beginning
update_list()

W_6 = weightChoice(10, 0, tab6, weight_6)

# *****************************************************************************************************************
#               TAB 7
# *****************************************************************************************************************
content_7 = tab(tab7, text1='Generation of a large volume of analytical waste should be avoided, and proper management'
                            'of analytical waste should be provided.', text2='Enter the amount of waste in mL or g:')

amount_var7 = StringVar()
amount_var7.set('input')
sample_amount_entry7 = ttk.Entry(tab7, textvariable=amount_var7, width=15).grid(sticky='w', row=2, column=0, padx=8, pady=8)

def change_entry_7():
    global var_7
    var_7 = None

    try:
        if float(amount_var7.get()) > 150:
            var_7 = 0
        elif float(amount_var7.get()) < 0.1:
            var_7 = 1.0
        else:
            var_7 = abs(-0.134 * log(float(amount_var7.get())) + 0.6946)   # absolute value to avoid negative values
        print('var_7:' + str(var_7))

    except ValueError:
        tkinter.messagebox.showerror(title='Value error', message='The amount has to be a float or an intiger, e.g. 0.14 or 21.')

# amount_var.trace('w', change_entry_7())
ttk.Button(tab7, text='Set', command=change_entry_7).grid(row=2, column=0, padx=8, pady=8)

W_7 = weightChoice(10, 0, tab7, weight_7)


# *****************************************************************************************************************
#               TAB 8
# *****************************************************************************************************************
content_8 = tab(tab8, text1='Multi-analyte or multi-parameter methods are preferred '
                            'versus methods using one analyte at a time.',
                      text2='Number of analytes determined in a single run:')

amount_var8a = StringVar()
amount_var8a.set('input')
sample_amount_entry8a = ttk.Entry(tab8, textvariable=amount_var8a, width=15).grid(sticky='w', row=2, column=0, padx=8, pady=8)

Label(tab8, text='Sample throughput (samples analysed per hour):', wraplength=300, justify=LEFT).grid(sticky='w', row=3, column=0, padx=8, pady=8)

amount_var8b = StringVar()
amount_var8b.set('input')
sample_amount_entry8b = ttk.Entry(tab8, textvariable=amount_var8b, width=15).grid(sticky='w', row=4, column=0, padx=8, pady=8)

def change_entry_8():
    global var_8
    var_8 = None

    try:
        if (float(amount_var8a.get()) * float(amount_var8b.get()) )< 1.0:
            var_8 = 0.0
        elif (float(amount_var8a.get()) * float(amount_var8b.get())) > 70.0:
            var_8 = 1.0
        else:
            var_8 = abs(0.2429 * log(float(amount_var8a.get()) * float(amount_var8b.get())) - 0.0517)   # absolute value to avoid negative values
        print('var_8:' + str(var_8))

    except ValueError:
        tkinter.messagebox.showerror(title='Value error', message='The amount has to be a float or an intiger, e.g. 0.14 or 21.')

# amount_var.trace('w', change_entry_7())
ttk.Button(tab8, text='Set', command=change_entry_8).grid(row=5, column=0, padx=8, pady=8)

W_8 = weightChoice(10, 0, tab8, weight_8)

# *****************************************************************************************************************
#               TAB 9
# *****************************************************************************************************************
content_9 = tab(tab9, text1='The use of energy should ba minimized',
                      text2='Select the most energy-intensive technique used in the method:')

var_9_text = StringVar(tab9)
# Dictionary with options
var_9_text_choices = { 'FTIR': 1.0,           # what about vortexing, incubation, etc.? Mineralization?
                       'Immunoassay': 1.0,
                       'Spectrofluorometry': 1.0,
                       'Titration': 1.0,
                       'UPLC': 1.0,
                       'UV-Vis Spectrometry': 1.0,
                       'AAS': 0.5,
                       'GC': 0.5,
                       'ICP-MS': 0.5, # naprawdę? plazma indukowana argonem i MS
                       'LC': 0.5,
                       'NMR': 0.0,
                       'GC-MS': 0.0,
                       'LC-MS': 0.0,
                       'X-ray diffractometry': 0.0}

var_9_text.set('select')

dropDown_9 = OptionMenu(tab9, var_9_text, *var_9_text_choices.keys())
dropDown_9.config(wraplength=250, bg='white', justify=LEFT, width=40, anchor='w')
dropDown_9.grid(sticky='w', row=2, column=0, padx=8, pady=8)

def change_dropdown_9(*args):
    global var_9
    var_9 = None
    var_9 = var_9_text_choices[var_9_text.get()]
    print('var_9:' + str(var_9))

var_9_text.trace('w', change_dropdown_9)

W_9 = weightChoice(10, 0, tab9, weight_9)

# *****************************************************************************************************************
#               TAB 10
# *****************************************************************************************************************
content_10 = tab(tab10, text1='Reagents obtained from renewable sources should be preferred.',
                      text2='Select the type of reagents:')

var_10_text = StringVar(tab10)
# Dictionary with options
var_10_text_choices = {'No reagents': 1.0,
                       'All reagents are bio-based': 1.0,
                       'Some reagents are bio-based': 0.5,
                       'None of the reagents are from bio-based sources': 0.0
                       }

var_10_text.set('select')

dropDown_10 = OptionMenu(tab10, var_10_text, *var_10_text_choices.keys())
dropDown_10.config(wraplength=250, bg='white', justify=LEFT, width=40, anchor='w')
dropDown_10.grid(sticky='w', row=2, column=0, padx=8, pady=8)

def change_dropdown_10(*args):
    global var_10
    var_10 = None
    var_10 = var_10_text_choices[var_10_text.get()]
    print('var_10:' + str(var_10))

var_10_text.trace('w', change_dropdown_10)

W_10 = weightChoice(10, 0, tab10, weight_10)

# *****************************************************************************************************************
#               TAB 11
# *****************************************************************************************************************
content_11 = tab(tab11, text1='Toxic reagents should be eliminated or replaced.',
                      text2='Does the method involve the use of toxic reagents?')

var_11a_text = StringVar(tab11)
# Dictionary with options
var_11a_text_choices = {'No': 1.0,
                        'Yes': 0.0}
var_11a_text.set('Select')



dropDown_11a = OptionMenu(tab11, var_11a_text, *var_11a_text_choices.keys())
dropDown_11a.config(wraplength=250, bg='white', justify=LEFT, width=40, anchor='w')
dropDown_11a.grid(sticky='w', row=2, column=0, padx=8, pady=8)

def enabler_11b():
    if float(var_11a_text_choices[var_11a_text.get()]) == 0.0:
        return 'enabled'
    else:
        return 'disabled'

amount_var11b = StringVar(tab11)
amount_var11b.set(0.0)

def change_dropdown_11a(*args):

    global var_11
    var_11 = 1.0
    var_11 = var_11a_text_choices[var_11a_text.get()]
    Label(tab11, text='Amount of toxic reagents in g or mL:', wraplength=300, justify=LEFT).grid(sticky='w', row=3, column=0, padx=8, pady=8)
    ttk.Entry(tab11, textvariable=amount_var11b, width=15, state=enabler_11b()).grid(sticky='w', row=4, column=0, padx=8, pady=8)
    ttk.Button(tab11, text='Set', command=change_dropdown_11a).grid(row=5, column=0, padx=8, pady=8)

    if float(var_11a_text_choices[var_11a_text.get()]) != 1.0:
        try:

            if float(amount_var11b.get()) < 0.1:
                var_11 = 0.8
            elif float(amount_var11b.get()) > 50.0:
                var_11 = 0.0
            else:
                var_11 = abs(-0.129 * log(float(amount_var11b.get())) + 0.5012)  # absolute value to avoid negative

        except ValueError:
            tkinter.messagebox.showerror(title='Value error', message='The amount has to be a float or an intiger, e.g. 0.14 or 21.')
    else:
        pass

    print(var_11)


var_11a_text.trace('w', change_dropdown_11a)

W_11 = weightChoice(10, 0, tab11, weight_11)

# *****************************************************************************************************************
#               TAB 12
# *****************************************************************************************************************
content_12 = tab(tab12, text1='Operator\'s safety should be increased.',
                      text2='Select the threats which are not avoided:')

varA = IntVar()
varB = IntVar()
varC = IntVar()
varD = IntVar()
varE = IntVar()
varF = IntVar()
varG = IntVar()

ttk.Checkbutton(tab12, text='toxic to aquatic life', variable=varA).grid(row=2, sticky='w', padx=8)
ttk.Checkbutton(tab12, text='bioacumulative', variable=varB).grid(row=3, sticky='w', padx=8)
ttk.Checkbutton(tab12, text='persistent', variable=varC).grid(row=4, sticky='w', padx=8)
ttk.Checkbutton(tab12, text='highly flammable', variable=varD).grid(row=5, sticky='w', padx=8)
ttk.Checkbutton(tab12, text='highly oxidizable', variable=varE).grid(row=6, sticky='w', padx=8)
ttk.Checkbutton(tab12, text='exposive', variable=varF).grid(row=7, sticky='w', padx=8)
ttk.Checkbutton(tab12, text='corrosive', variable=varG).grid(row=8, sticky='w', padx=8)

def testPrint():
    # print(varA.get(), varB.get(), varC.get(), varD.get(), varE.get(), varF.get(), varG.get())
    global var_12a
    var_12a = (varA.get() + varB.get() + varC.get() + varD.get() + varE.get() + varF.get() + varG.get())
    # print(var_12a)
    global var_12
    if var_12a == 0:
        var_12 = 1.0
    elif var_12a == 1:
        var_12 = 0.8
    elif var_12a == 2:
        var_12 = 0.6
    elif var_12a == 3:
        var_12 = 0.4
    elif var_12a == 4:
        var_12 = 0.2
    else:
        var_12 = 0.0
    print ('var_12: %f' % var_12)

ttk.Button(tab12, text='Set', command=testPrint).grid(row=9, column=0, padx=8, pady=8)

W_12 = weightChoice(10, 0, tab12, weight_12)



##################################################################################################

# pack the tab parent and its tabs:
tab_parent.pack(expand=1, fill='both')

# add a temporary value window for testing:

# green_index = '0.50'
entry_text = StringVar()
# index_entry = ttk.Entry(leftFrame, textvariable=entry_text)
# index_entry.pack(side=BOTTOM, anchor=SW)
# entry_text.set(green_index)

def printScore():
    try:
        global score
        score = (var_1 * weight_1.get()
                 + var_2 * weight_2.get()
                 + var_3 * weight_3.get()
                 + 0.5 * weight_4.get()
                 + var_5 * weight_5.get()
                 + var_6 * weight_6.get()
                 + var_7 * weight_7.get()
                 + var_8 * weight_8.get()
                 + var_9 * weight_9.get()
                 + var_10 * weight_10.get()
                 + var_11 * weight_11.get()
                 + var_12 * weight_12.get())/(weight_1.get() + weight_2.get() + weight_3.get() + weight_4.get() + weight_5.get() +
                                                                                                             weight_6.get() + weight_7.get() +
                 weight_8.get() + weight_9.get() + weight_10.get() + weight_11.get() + weight_12.get())

        entry_text.set(str(score)[:4])
        print(score)
    except NameError:
        tkinter.messagebox.showerror(title='Name Error', message='Please set all 12 variables.')

refreshButton = ttk.Button(leftFrame, text='GENERATE LABEL',
                           command=lambda: [printScore(),
                                            clearFrame(rightFrame),
                                            pieChart(), #weights, labels, colors
                                            print_variables()
                                            ])
refreshButton.pack(side=BOTTOM, anchor=SW)


# ttk.Button(leftFrame, text='Print score', command=printScore).pack(side=BOTTOM)


##################################################################################################
root.mainloop()  # to keep the window continuously on, otherwise it shall disappear


