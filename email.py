from tkinter import *

def show_entry_fields():
    print("To: %s\nFrom: %s" % (entry0.get(), entry1.get()))

root = Tk()

root.wm_title("Email Web Gui - Thomas Nguyen")

Label(root, text = "To:").grid(row = 0)
Label(root, text = "From:").grid(row = 1)
Label(root, text = "Subject:").grid(row = 2)
Label(root, text = "Message:").grid(row = 3)

entry0= Entry(root)
entry1= Entry(root)
entry2= Entry(root)
entry3= Entry(root)

entry0.grid(row = 0, column = 1)
entry1.grid(row = 1, column = 1)
entry2.grid(row = 2, column = 1)
entry3.grid(row = 3, column = 1)

Button(root, text = 'Send', command = show_entry_fields).grid(row = 4, column = 1, sticky = W, pady = 4)
Button(root, text = 'Cancel', command = root.quit).grid(row = 4, column = 0, sticky = W, pady = 4)

root.mainloop()

