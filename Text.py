import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Initialize Translator
translator = Translator()

# Function to translate text
def translate_text():
    source_lang = source_language_combo.get()
    target_lang = target_language_combo.get()
    text = input_text.get("1.0", "end-1c")  # Get text from input box
    
    # Perform translation
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    output_text.delete("1.0", "end")  # Clear previous text
    output_text.insert("end", translated.text)  # Display translated text

# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x400")

# Title Label
title_label = tk.Label(root, text="Language Translator", font=("Helvetica", 16))
title_label.pack(pady=10)

# Input Text
input_label = tk.Label(root, text="Enter Text to Translate:")
input_label.pack()
input_text = tk.Text(root, height=5, width=40)
input_text.pack()

# Source Language Dropdown
source_language_label = tk.Label(root, text="Source Language:")
source_language_label.pack()
source_language_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
source_language_combo.set("english")  # Default language
source_language_combo.pack()

# Target Language Dropdown
target_language_label = tk.Label(root, text="Target Language:")
target_language_label.pack()
target_language_combo = ttk.Combobox(root, values=list(LANGUAGES.values()))
target_language_combo.set("spanish")  # Default target language
target_language_combo.pack()

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Output Text
output_label = tk.Label(root, text="Translated Text:")
output_label.pack()
output_text = tk.Text(root, height=5, width=40)
output_text.pack()

# Run the main event loop
root.mainloop()