import tkinter as tk

def view():
    window = tk.Tk()
    label = tk.Label(window, text="Data Kinder")
    label.pack()

    view_child_button = tk.Button(text="View Child")
    view_child_button.pack()    

    update_child_button = tk.Button(text="Update Child")
    update_child_button.pack()

    add_child_button = tk.Button(text="Add Child")
    add_child_button.pack()



    window.mainloop()