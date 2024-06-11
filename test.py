import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("TreeView Focus Event Example")
root.geometry("400x300")

# Function to fetch values from the selected item in the TreeView
def on_treeview_focus(event):
    selected_item = tree.selection()
    if selected_item:
        item_values = tree.item(selected_item, 'values')
        print(f"Selected Item Values: {item_values[0]}")

# Create a TreeView widget
tree = ttk.Treeview(root, columns=("Name", "Age", "City"), show="headings")

# Define the column headings
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("City", text="City")

# Insert some sample data into the TreeView
data = [
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 35, "Chicago"),
    ("David", 40, "Houston"),
    ("Eve", 28, "Philadelphia")
]

for person in data:
    tree.insert("", "end", values=person)

# Bind the focus event to the TreeView
tree.bind("<FocusIn>", on_treeview_focus)

# Pack the TreeView widget into the main window
tree.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
