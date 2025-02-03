import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def select_images():
    file_paths = filedialog.askopenfilenames(title="이미지를 선택하세요", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if not file_paths:
        messagebox.showwarning("경고", "이미지를 선택하지 않았습니다.")
        return
    
    save_pdf(file_paths)

def save_pdf(image_files):
    images = []
    
    for img_file in image_files:
        img = Image.open(img_file).convert("RGB")
        images.append(img)
    
    if images:
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], title="PDF 저장")
        
        if save_path:
            images[0].save(save_path, save_all=True, append_images=images[1:])
            messagebox.showinfo("완료", f"PDF 변환이 완료되었습니다!\n저장 위치: {save_path}")
        else:
            messagebox.showwarning("경고", "PDF 저장이 취소되었습니다.")
    else:
        messagebox.showerror("오류", "변환할 이미지가 없습니다.")

def create_gui():
    root = tk.Tk()
    root.title("이미지를 PDF로 변환")
    root.geometry("300x200")
    
    label = tk.Label(root, text="이미지를 PDF로 변환", font=("Arial", 12))
    label.pack(pady=10)
    
    convert_button = tk.Button(root, text="PDF로 변환하기", command=select_images, font=("Arial", 10), padx=10, pady=5)
    convert_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
