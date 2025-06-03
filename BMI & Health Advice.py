import tkinter as tk
from tkinter import ttk, messagebox

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_suggestions(category):
    suggestions = {
        "Underweight": "Your BMI indicates you are underweight. Please consider eating a balanced, nutritious diet and consult a healthcare professional for guidance.",
        "Normal weight": "Your BMI is within the normal range. Keep up your healthy lifestyle to maintain your well-being.",
        "Overweight": "Your BMI indicates you are overweight. Consider adopting a healthier diet and regular exercise to improve your health.",
        "Obesity": "Your BMI indicates obesity, which can increase health risks. It’s important to consult a healthcare professional for guidance on lifestyle changes and support."
    }
    return suggestions.get(category, "No suggestion available")

def on_calculate_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Height and Weight cannot be zero or negative")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values")
        return

    weight_unit = weight_unit_var.get()
    height_unit = height_unit_var.get()

    # Convert weight to kg
    if weight_unit == "lbs":
        weight = weight * 0.453592
    elif weight_unit == "g":
        weight = weight / 1000
    elif weight_unit == "st":
        weight = weight * 6.35029

    # Convert height to meters
    if height_unit == "inches":
        height = height * 0.0254
    elif height_unit == "cm":
        height = height / 100
    elif height_unit == "feet":
        height = height * 0.3048

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)
    suggestion = get_suggestions(category)
    result_label.config(text=f"BMI: {bmi:.2f} ({category})")
    suggestions_label.config(text=f"Suggestion: {suggestion}")

# GUI setup
app = tk.Tk()
app.title("Health Checker")

entry_frame = ttk.Frame(app)
entry_frame.pack(pady=20, padx=20)

# Weight Entry
weight_label = ttk.Label(entry_frame, text="Weight:")
weight_label.grid(row=0, column=0, pady=5, padx=5)
weight_entry = ttk.Entry(entry_frame, width=15)
weight_entry.grid(row=0, column=1, pady=5, padx=5)

weight_unit_var = tk.StringVar(value="kg")
weight_unit_menu = ttk.Combobox(entry_frame, textvariable=weight_unit_var,
                                 values=["kg", "lbs", "g", "st"], state="readonly", width=5)
weight_unit_menu.grid(row=0, column=2, pady=5, padx=5)

# Height Entry
height_label = ttk.Label(entry_frame, text="Height:")
height_label.grid(row=1, column=0, pady=5, padx=5)
height_entry = ttk.Entry(entry_frame, width=15)
height_entry.grid(row=1, column=1, pady=5, padx=5)

height_unit_var = tk.StringVar(value="m")
height_unit_menu = ttk.Combobox(entry_frame, textvariable=height_unit_var,
                                 values=["m", "inches", "cm", "feet"], state="readonly", width=5)
height_unit_menu.grid(row=1, column=2, pady=5, padx=5)

# Calculate Button
calculate_button = ttk.Button(entry_frame, text="Calculate BMI", command=on_calculate_clicked)
calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

# Result Label
result_label = ttk.Label(entry_frame, text="Enter your details above:")
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Suggestions Label
suggestions_label = ttk.Label(entry_frame, text="Suggestions will appear here:")
suggestions_label.grid(row=4, column=0, columnspan=3, pady=10)

app.mainloop()
