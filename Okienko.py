import tkinter

def my_function():
    result = 42
    return result

root = Tk()

root.title("Function Result")

result_label = tk.Label(root, text="The result is: " + str(my_function()))
result_label.pack()

root.mainloop()