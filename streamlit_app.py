import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageWin
import win32ui

generated_image = None

def generate_label():
    global generated_image

    old_code = old_entry.get().strip()
    new_code = new_entry.get().strip()

    if not old_code or not new_code:
        return

    # label size (same as yours)
    w, h = 383, 184
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)

    font_big = ImageFont.truetype("C:\\Windows\\Fonts\\arialbd.ttf", 20)

    # OLD (top)
    draw.text((20, 30), old_code, fill="black", font=font_big)

    # NEW (bottom)
    draw.text((20, 100), new_code, fill="black", font=font_big)

    generated_image = img

def print_label():
    global generated_image

    if generated_image is None:
        return

    printer_name = "M120 Printer"

    try:
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)
        hdc.StartDoc("Label")
        hdc.StartPage()

        dib = ImageWin.Dib(generated_image)
        dib.draw(hdc.GetHandleOutput(), (0, 0, 383, 184))

        hdc.EndPage()
        hdc.EndDoc()
        hdc.DeleteDC()

    except Exception as e:
        print(e)

def generate_and_print():
    generate_label()
    print_label()

# UI
root = tk.Tk()
root.title("Quick Label")

tk.Label(root, text="OLD").pack()
old_entry = tk.Entry(root, width=30)
old_entry.pack()

tk.Label(root, text="NEW").pack()
new_entry = tk.Entry(root, width=30)
new_entry.pack()

tk.Button(root, text="PRINT", command=generate_and_print).pack(pady=10)

root.mainloop()
