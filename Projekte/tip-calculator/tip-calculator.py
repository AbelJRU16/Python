import tkinter as tk
from tkinter import ttk

def calculate_tip():
    try:
        total_bill = float(entry_total.get())
        tip_percentage = float(combo_tip.get().replace('%', ''))
        tip_amount = total_bill * (tip_percentage / 100)
        total_with_tip = total_bill + tip_amount

        label_tip_amount.config(text=f'Tip Amount: ${tip_amount:.2f}')
        label_total_with_tip.config(text=f'Total with Tip: ${total_with_tip:.2f}')
    except ValueError:
        label_tip_amount.config(text='Invalid input')
        label_total_with_tip.config(text='')

root = tk.Tk()
root.title("Tip Calculator")
root.geometry("300x260")

# Etiqueta y entrada para el total de la cuenta
label_total = tk.Label(root, text="Total Bill:")
label_total.pack(pady=5)
entry_total = tk.Entry(root)
entry_total.pack(pady=5)

# Etiqueta y combobox para el porcentaje de propina
label_tip = tk.Label(root, text="Tip Percentage:")
label_tip.pack(pady=5)
combo_tip = ttk.Combobox(root, values=["10%", "15%", "20%", "25%", "30%"])
combo_tip.set("15%")  # Valor predeterminado
combo_tip.pack(pady=5)

# Botón para calcular la propina
button_calculate = tk.Button(root, text="Calculate Tip", command=calculate_tip)
button_calculate.pack(pady=10)

# Etiquetas para mostrar el monto de la propina y el total con propina
label_tip_amount = tk.Label(root, text="Tip Amount: $0.00")
label_tip_amount.pack(pady=5)
label_total_with_tip = tk.Label(root, text="Total with Tip: $0.00")
label_total_with_tip.pack(pady=5)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
