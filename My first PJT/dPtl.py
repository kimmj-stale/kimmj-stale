import tkinter as tk

def switch_to_frame1():
    frame1.pack_forget()
    frame2.pack()

def switch_to_frame2():
    frame2.pack_forget()
    frame1.pack()

root = tk.Tk()
root.title('Frame Switching Example')

# Frame 1
frame1 = tk.Frame(root)
label_frame1 = tk.Label(frame1, text="This is Frame 1", font=('Helvetica', 16))
label_frame1.pack(pady=10)

button_switch1 = tk.Button(frame1, text="Switch to Frame 2", command=switch_to_frame2)
button_switch1.pack(pady=10)

# Frame 2
frame2 = tk.Frame(root)
label_frame2 = tk.Label(frame2, text="This is Frame 2", font=('Helvetica', 16))
label_frame2.pack(pady=10)

button_switch2 = tk.Button(frame2, text="Switch to Frame 1", command=switch_to_frame1)
button_switch2.pack(pady=10)

# Initially show Frame 1
frame1.pack()

root.mainloop()
