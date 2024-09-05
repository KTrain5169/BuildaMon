import tkinter as tk
from tkinter import ttk
import random

# Original variables
mon_strength = ["Regular", "Convergent", "Starter", "God Pokemon", "Fossil", "Pseudo", "Mythical", "Legendary"]
mon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison",
             "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
mon_gimmick = ["None", "Mega Evolution", "Additional Form", "Signature Move", "Signature Ability", "Fusion", 
               "Gigantamax", "New Mechanic", "Corrupted", "Shining"]
gimmick_method = ["Held Item", "Seasonal", "Key Item", "Move", "Location", "Time", "Weather", "Ability"]

# Mapping gimmicks to specific gimmick methods
gimmick_method_mapping = {
    "Mega Evolution": "Held Item",
    "Fusion": "Key Item",
    "Z-Move": "Held Item",
    "Signature Move": "Move",
    "Signature Ability": "Ability",
}

# Function to center the window
def center_window(window, width=400, height=300):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

# Function to generate random Pokémon with adjusted values
def generate_random_pokemon():
    strength = mon_strength_dropdown.get()
    type_1 = type_1_dropdown.get()
    type_2 = type_2_dropdown.get()
    
    selected_gimmicks = [gimmick for gimmick, var in gimmick_vars.items() if var.get()]
    gimmick = random.choice(selected_gimmicks) if selected_gimmicks else "None"
    
    # Check if the gimmick has a specific method, else choose randomly
    if gimmick in gimmick_method_mapping:
        acquire_method = gimmick_method_mapping[gimmick]
        method_dropdown.set(acquire_method)
        method_dropdown_widget.config(state="disabled")  # Disable if forced method
    else:
        acquire_method = method_dropdown.get()
        method_dropdown_widget.config(state="normal")  # Enable for other methods
    
    # Display generated Pokémon
    output_text.set(f"Generated Pokémon:\nStrength: {strength}\n"
                    f"Type 1: {type_1}\nType 2: {type_2}\n"
                    f"Gimmick: {gimmick}\nGimmick Method: {acquire_method}")

# Function to enforce gimmick method rules
def enforce_gimmick_rules():
    selected_gimmicks = [gimmick for gimmick, var in gimmick_vars.items() if var.get()]
    for gimmick in selected_gimmicks:
        if gimmick in gimmick_method_mapping:
            method_dropdown.set(gimmick_method_mapping[gimmick])
            method_dropdown_widget.config(state="disabled")  # Disable if method is forced
            return  # No need to continue once we enforce the first gimmick's rule
    method_dropdown_widget.config(state="normal")  # Enable method selection otherwise

# Main window
root = tk.Tk()
root.title("Pokémon Randomizer")

# Center the window
center_window(root, 600, 400)

# Dropdown for Mon Strength
ttk.Label(root, text="Select Mon Strength:").grid(row=0, column=0, padx=5, pady=5)
mon_strength_dropdown = ttk.Combobox(root, values=mon_strength, state="readonly")
mon_strength_dropdown.grid(row=0, column=1)
mon_strength_dropdown.set(mon_strength[0])

# Dropdowns for Mon Types
ttk.Label(root, text="Select Type 1:").grid(row=1, column=0, padx=5, pady=5)
type_1_dropdown = ttk.Combobox(root, values=mon_types, state="readonly")
type_1_dropdown.grid(row=1, column=1)
type_1_dropdown.set(mon_types[0])

ttk.Label(root, text="Select Type 2:").grid(row=2, column=0, padx=5, pady=5)
type_2_dropdown = ttk.Combobox(root, values=mon_types, state="readonly")
type_2_dropdown.grid(row=2, column=1)
type_2_dropdown.set(mon_types[0])

# Gimmick Checkboxes
ttk.Label(root, text="Select Gimmicks:").grid(row=3, column=0, padx=5, pady=5)
gimmick_vars = {}
for i, gimmick in enumerate(mon_gimmick):
    var = tk.BooleanVar(value=False)
    gimmick_vars[gimmick] = var
    cb = ttk.Checkbutton(root, text=gimmick, variable=var, command=enforce_gimmick_rules)
    cb.grid(row=3+i//2, column=1+(i % 2), padx=5, pady=5)

# Dropdown for Gimmick Method
ttk.Label(root, text="Select Gimmick Method:").grid(row=7, column=0, padx=5, pady=5)
method_dropdown = tk.StringVar()
method_dropdown_widget = ttk.Combobox(root, textvariable=method_dropdown, values=gimmick_method, state="readonly")
method_dropdown_widget.grid(row=7, column=1)
method_dropdown.set(gimmick_method[0])

# Button to generate Pokémon
generate_button = ttk.Button(root, text="Generate Pokémon", command=generate_random_pokemon)
generate_button.grid(row=8, column=0, columnspan=2, pady=10)

# Label to display the output
output_text = tk.StringVar()
output_label = ttk.Label(root, textvariable=output_text, anchor="w", justify="left")
output_label.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Run the GUI
generate_random_pokemon()  # Initial generation when the app opens
root.mainloop()
