import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

def remove_emails():
    file_path = filedialog.askopenfilename()
    domain = selected_domain.get()
    invert_filter = invert_var.get()
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        if not file_path.endswith('.csv'):
            raise ValueError("The selected file is not a CSV file.")
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError("The CSV file is empty.")
        email_column = 'Email'
        if email_column not in df.columns:
            raise ValueError(f"'{email_column}' column doesn't exist in the CSV file. Please ensure the 'Email' column in your CSV starts with a capital 'E'.")
        total_emails = df[email_column].count()
        progressbar["maximum"] = total_emails
        progressbar["value"] = 0
        for i, row in df.iterrows():
            email = row[email_column]
            if pd.isnull(email):
                continue
            if invert_filter and not email.endswith(domain) or not invert_filter and email.endswith(domain):
                df.at[i, email_column] = float('nan')
            progressbar["value"] = i + 1
            root.update_idletasks()
        df = df.dropna(subset=[email_column])
        remaining_emails = df[email_column].count()
        removed_emails = total_emails - remaining_emails
        df.to_csv('output.csv', index=False)
        progressbar["value"] = 0
        if invert_filter:
            messagebox.showinfo("Success", f"Number of {domain} emails kept: {remaining_emails}\nNumber of other emails removed: {removed_emails}")
        else:
            messagebox.showinfo("Success", f"Number of {domain} emails removed: {removed_emails}\nNumber of emails left in the new file: {remaining_emails}")
    except FileNotFoundError as e:
        messagebox.showerror("File Not Found Error", str(e))
    except ValueError as e:
        messagebox.showerror("Value Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.configure(bg='light blue')
root.title("Email Filter")
domains = ['.gov', 'gmail.com', 'yahoo.com', '.edu', 'hotmail.com', 'outlook.com', 'icloud.com', 'aol.com', 'protonmail.com']
selected_domain = tk.StringVar(root)
selected_domain.set(domains[0])
label = tk.Label(root, text="Select domain to filter:", bg='light blue')
label.pack(pady=10)
dropdown = tk.OptionMenu(root, selected_domain, *domains)
dropdown.pack(pady=10)
invert_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Invert filter (keep selected domain)", variable=invert_var, bg='light blue')
checkbox.pack(pady=10)
progressbar = ttk.Progressbar(root, length=200)
progressbar.pack(pady=10)
button = tk.Button(root, text='Remove Emails', command=remove_emails)
button.pack(pady=10)
root.mainloop()
