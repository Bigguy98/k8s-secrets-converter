import tkinter as tk
from tkinter import messagebox, scrolledtext
import yaml
import base64

def convert_to_stringdata():
    try:
        secret = yaml.safe_load(input_text.get("1.0", tk.END))
        string_data = {}
        for key, value in secret['data'].items():
            decoded_value = base64.b64decode(value).decode('utf-8')
            string_data[key] = decoded_value

        secret['stringData'] = string_data
        del secret['data']

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, yaml.dump(secret))
        messagebox.showinfo("Success", "Conversion to stringData completed!")
    except Exception as e:
        messagebox.showerror("Error", "Please ensure your input data is valid \nIt should include base64 encoded data")

def convert_to_encoded():
    try:
        secret = yaml.safe_load(input_text.get("1.0", tk.END))
        encoded_data = {}
        for key, value in secret['stringData'].items():
            encoded_value = base64.b64encode(value.encode('utf-8')).decode('utf-8')
            encoded_data[key] = encoded_value

        secret['data'] = encoded_data
        del secret['stringData']

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, yaml.dump(secret))
        messagebox.showinfo("Success", "Conversion to encoded data completed!")
    except Exception as e:
        messagebox.showerror("Error", "Please ensure your input data is valid \nIt should include string data")

# Create the main window
root = tk.Tk()
root.title("K8s Secret Converter")

# Create input and output text fields
input_label = tk.Label(root, text="Input YAML")
input_label.pack()
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
input_text.pack(pady=10)

output_label = tk.Label(root, text="Output YAML")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
output_text.pack(pady=10)

# Add buttons to the window
btn_stringdata = tk.Button(root, text="Convert to stringData", command=convert_to_stringdata)
btn_stringdata.pack(pady=10)

btn_encoded = tk.Button(root, text="Convert to encoded data", command=convert_to_encoded)
btn_encoded.pack(pady=10)

# Run the application
root.mainloop()