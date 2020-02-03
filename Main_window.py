from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import LinearSegmentedColormap
from tkinter import ttk
from tkinter import filedialog
from functools import partial
import tkinter.messagebox
import webbrowser


root = Tk()

# app title:
root.title('Analytical Method Green Index Calculator')

# default app size:
root.geometry('800x500')
# root.configure(bg='white')
# create the small icon in the task bar:
root.iconbitmap('PG_favicon.ico')

# *********************** Functions ****************************

def clearFrame(frame):
    frame.destroy()
    global rightFrame
    rightFrame = Frame(root, width=300)
    rightFrame.pack(side=RIGHT)


# Image save dialog:
def saveImage():

    ftypes = [('PNG file', '.png'), ('JPG file', '.jpg'), ('All files', '*')]
    filename = filedialog.asksaveasfilename(filetypes=ftypes, defaultextension='.png')
    plt.savefig(filename, bbox_inches='tight')      # save the plot in the specified path; the 'tight' option removes the whitespace from around the figure

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

    popup_label3 = Label(win, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis non sem ut aliquet. Praesent tempus fringilla suscipit. Phasellus tellus massa, semper et bibendum quis, rhoncus id neque. Sed euismod consectetur elit id tristique. Sed eu nibh id ante malesuada condimentum. Phasellus luctus finibus luctus. Pellentesque mi tellus, condimentum sit amet porta sit amet, ullamcorper quis elit. Pellentesque eu mollis nulla. Quisque vulputate, sem at iaculis vehicula, dui orci aliquet lectus, in facilisis odio dolor ut leo. Vivamus convallis hendrerit est luctus ornare. Nullam augue nisi, aliquam sit amet scelerisque hendrerit, pretium vel dui. Pellentesque sed tortor mollis, imperdiet quam quis, scelerisque erat. Vestibulum quis mollis dolor.', wraplength=300, justify=LEFT, bg='white')
    popup_label3.grid(row=2, column=0, padx=8, pady=8)

    popup_button = Button(win, text="Close", command=win.destroy)
    popup_button.grid(row=3, column=0, padx=8, pady=8)

def colorMapper(value):
    cmap=LinearSegmentedColormap.from_list('rg',["red", "yellow", "green"], N=256)
    mapped_color = int(value * 255)
    color = cmap(mapped_color)
    return color

# ********** Main menu *************
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
leftFrame = Frame(root, bd=1, height=450)
rightFrame = Frame(root, width=300)
bottomFrame = Frame(root, bd=1)

leftFrame.pack(side=LEFT, anchor=N)
rightFrame.pack(side=RIGHT)
bottomFrame.pack(side=BOTTOM, anchor=W)

def destroyCanvas(canvas):
    canvas.destroy()

# ************************* Tabs ***************************
# create tabs:
tab_parent = ttk.Notebook(leftFrame)
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

weights = [12, 52, 47, 9, 10, 47, 21, 11, 10, 10, 69, 13]
labels = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']

colors = []                     # remember to map the colors to scores later
for i in range(0, 10, 1):
    color = colorMapper(i/10)
    colors.append(color)

def pieChart(weights, labels, colors):

    index_value = float(entry_text.get())

    fig, ax = plt.subplots(figsize=(3, 3), dpi=150)
    ax.clear()
    ax.axis('equal')
    radius = 1.0
    pie2 = ax.pie(weights, radius=radius, colors=colors, labeldistance=(radius * 0.85), labels=labels, rotatelabels =True, startangle=90, counterclock=False, wedgeprops={"edgecolor": "black", 'linewidth': 1}, textprops={'fontsize': (radius * 10)})

    plt.setp(pie2[1], rotation_mode="anchor", ha="center", va="center")
    for tx in pie2[1]:
        rot = tx.get_rotation()
        tx.set_rotation(rot+90+(1-rot//180)*180)

    circle = plt.Circle(xy=(0, 0), radius=(radius * 0.75), facecolor=colorMapper(index_value), edgecolor='black', linewidth=1)
    plt.gca().add_artist(circle)

    ax.text(0.5, 0.5, str(index_value),
            verticalalignment='center', horizontalalignment='center',
            transform=ax.transAxes,
            color='black', fontsize=(radius * 40))

    fig.tight_layout()      # for exporting a compact figure

    # Pack the figure into a canvas:
    canvas = FigureCanvasTkAgg(fig, master=rightFrame)  # A tk.DrawingArea.
    plot_widget = canvas.get_tk_widget()

    plot_widget.pack(side=TOP)



# **************************************

# add a temporary value window for testing:

green_index = '0.5'
entry_text = StringVar()
index_entry = ttk.Entry(leftFrame, textvariable=entry_text)
index_entry.pack(side=BOTTOM, anchor=SW)
entry_text.set(green_index)



refreshButton = ttk.Button(leftFrame, text='GENERATE LABEL', command=lambda: [clearFrame(rightFrame), pieChart(weights, labels, colors)])
refreshButton.pack(side=BOTTOM, anchor=SW)


def tab(tab_no, text):
    label = Label(tab_no, text=text, wraplength=300, justify=LEFT)
    label.grid(row=0, column=0, padx=8, pady=8)

# *************************** TAB 1 **************************************
content_1 = tab(tab1, 'Direct analytical techniques should be applied to avoid sample treatment.')


# *************************** TAB 2 **************************************
first_label_tab2 = Label(tab2, text='Minimal sample size and minimal number of samples are goals.', wraplength=300, justify=LEFT)
first_label_tab2.grid(row=0, column=0, padx=8, pady=8)


# *************************** TAB 3 **************************************
first_label_tab3 = Label(tab3, text='In situ measurements should be performed.', wraplength=300, justify=LEFT)
first_label_tab3.grid(row=0, column=0, padx=8, pady=8)


# *************************** TAB 4 **************************************
first_label_tab4 = Label(tab4, text='Integration of analytical processes and operations saves energy and reduces the use of reagents.', wraplength=300, justify=LEFT)
first_label_tab4.grid(row=0, column=0, padx=8, pady=8)




# pack the tab parent and its tabs:
tab_parent.pack(expand=1, fill='both')







root.mainloop()                                     #to keep the window continuously on, otherwise it shall disappear