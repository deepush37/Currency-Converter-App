import requests
import tkinter as tk
from tkinter import messagebox

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency_entry.get().upper()
        to_curr = to_currency_entry.get().upper()

        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
        response = requests.get(url)
        data = response.json()

        if "rates" not in data:
            messagebox.showerror("Error", "Invalid currency code or API issue.")
            return

        converted = data["rates"][to_curr]
        result_label.config(text=f"{amount} {from_curr} = {round(converted, 2)} {to_curr}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

tk.Label(root, text="Amount:").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="From Currency (e.g., USD):").pack(pady=5)
from_currency_entry = tk.Entry(root)
from_currency_entry.pack()

tk.Label(root, text="To Currency (e.g., INR):").pack(pady=5)
to_currency_entry = tk.Entry(root)
to_currency_entry.pack()

tk.Button(root, text="Convert", command=convert_currency, bg="lightgreen").pack(pady=15)

result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
