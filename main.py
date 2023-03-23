import tkinter as tk
from tkinter import ttk
from transformer import transform_text

def on_convert_button_click():
    input_text = input_text_box.get("1.0", tk.END).strip()
    output_text = transform_text(input_text)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, output_text)

root = tk.Tk()
root.title("한글 변환기")

input_label = ttk.Label(root, text="입력 텍스트:")
input_label.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

input_text_box = tk.Text(root, width=40, height=10)
input_text_box.grid(column=0, row=1, padx=10, pady=10)

convert_button = ttk.Button(root, text="변환", command=on_convert_button_click)
convert_button.grid(column=0, row=2, padx=10, pady=10)

output_label = ttk.Label(root, text="출력 텍스트:")
output_label.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)

output_text_box = tk.Text(root, width=40, height=10)
output_text_box.grid(column=1, row=1, padx=10, pady=10)

root.mainloop()
