import customtkinter as ct
from CTkMessagebox import CTkMessagebox

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

root = ct.CTk()
root.title("Yas Yoxlama")
root.geometry("400x300")

Ad = ct.CTkLabel(root, text="Ad Soyad:", font=("Arial", 16))
Ad.pack(pady=(20, 5))  

Ad = ct.CTkEntry(root, width=250)
Ad.pack(pady=5)

Yas = ct.CTkLabel(root, text="Yas:", font=("Arial", 16))
Yas.pack(pady=(20, 5))

Yas = ct.CTkEntry(root, width=100)
Yas.pack(pady=5)

def yoxla():
    adsoyad = Ad.get()
    yas = Yas.get()

    yas = int(yas)

    if yas >= 18:
        CTkMessagebox(title="Nəticə", message=f"{adsoyad}, siz 18+ yasindasiniz")
    else:
        CTkMessagebox(title="Nəticə", message=f"{adsoyad}, siz hele 18 yasinda deyilsiniz!!!")

button = ct.CTkButton(root, text="Yoxlayin", fg_color="red", font=("Arial",20), corner_radius=15, command=yoxla)
button.pack(pady=20)

root.mainloop()