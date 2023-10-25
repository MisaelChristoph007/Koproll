import tkinter as tk
from tkinter import ttk

class LoanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pinjaman Online")
        self.root.geometry("700x600")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        self.user_frame = ttk.Frame(self.notebook)
        self.admin_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.user_frame, text="User")
        self.notebook.add(self.admin_frame, text="Admin")

        self.create_user_page()
        self.create_admin_page()

        # Inisialisasi data hasil inputan dari pengguna
        self.user_data = []

    def create_user_page(self):
        user_label = ttk.Label(self.user_frame, text="Halaman User")
        user_label.pack(pady=20)

        self.nama_var = tk.StringVar()
        self.ktp_var = tk.StringVar()
        self.telp_var = tk.StringVar()
        self.pinjaman_var = tk.StringVar()

        ttk.Label(self.user_frame, text="Nama:").pack()
        nama_entry = ttk.Entry(self.user_frame, textvariable=self.nama_var)
        nama_entry.pack()

        user_label = ttk.Label(self.user_frame, text="")
        user_label.pack(pady=2)

        ttk.Label(self.user_frame, text="No. KTP:").pack()
        ktp_entry = ttk.Entry(self.user_frame, textvariable=self.ktp_var)
        ktp_entry.pack()

        user_label = ttk.Label(self.user_frame, text="")
        user_label.pack(pady=2)

        ttk.Label(self.user_frame, text="No. Telepon:").pack()
        telp_entry = ttk.Entry(self.user_frame, textvariable=self.telp_var)
        telp_entry.pack()

        user_label = ttk.Label(self.user_frame, text="")
        user_label.pack(pady=2)
      
        ttk.Label(self.user_frame, text="Jumlah Pinjaman:").pack()
        pinjaman_entry = ttk.Entry(self.user_frame, textvariable=self.pinjaman_var)
        pinjaman_entry.pack()

        user_label = ttk.Label(self.user_frame, text="")
        user_label.pack(pady=2)

        submit_button = ttk.Button(self.user_frame, text="Kirim Data", command=self.send_data)
        submit_button.pack()

    def send_data(self):
        nama = self.nama_var.get()
        ktp = self.ktp_var.get()
        telp = self.telp_var.get()
        pinjaman = self.pinjaman_var.get()

        # Menambahkan data dari pengguna ke daftar data hasil inputan
        self.user_data.append([nama, ktp, telp, pinjaman])

        # Membersihkan inputan setelah pengiriman
        self.nama_var.set("")
        self.ktp_var.set("")
        self.telp_var.set("")
        self.pinjaman_var.set("")

        # Memperbarui data di halaman Admin
        self.update_admin_tree()

    def create_admin_page(self):
        admin_label = ttk.Label(self.admin_frame, text="Halaman Admin")
        admin_label.pack(pady=20)

        # Treeview untuk menampilkan data hasil inputan dari pengguna
        self.admin_tree = ttk.Treeview(self.admin_frame, columns=("Nama", "No. KTP", "No. Telepon", "Jumlah Pinjaman"), show="headings")
        self.admin_tree.heading("Nama", text="Nama")
        self.admin_tree.heading("No. KTP", text="No. KTP")
        self.admin_tree.heading("No. Telepon", text="No. Telepon")
        self.admin_tree.heading("Jumlah Pinjaman", text="Jumlah Pinjaman")
        self.admin_tree.pack()

        # Tombol Edit dan Hapus
        user_label = ttk.Label(self.user_frame, text="")
        user_label.pack(pady=2)
        edit_button = ttk.Button(self.admin_frame, text="Edit", command=self.edit_data)
        edit_button.pack()
        user_label = ttk.Label(self.user_frame, text="")
        user_label.pack(pady=2)
        delete_button = ttk.Button(self.admin_frame, text="Hapus", command=self.delete_data)
        delete_button.pack()

        # Bind untuk mengatur item terpilih pada Treeview
        self.admin_tree.bind("<ButtonRelease-1>", self.on_select)

    def update_admin_tree(self):
        # Membersihkan Treeview dan menambahkan data hasil inputan pengguna
        self.admin_tree.delete(*self.admin_tree.get_children())
        for data in self.user_data:
            self.admin_tree.insert("", "end", values=data)

    def on_select(self, event):
        # Mengambil data dari item terpilih di Treeview
        selected_item = self.admin_tree.selection()
        if selected_item:
            selected_data = self.admin_tree.item(selected_item, "values")
            if selected_data:
                self.selected_data = selected_data

    def edit_data(self):
      # Mengambil data terpilih dan mengizinkan Admin untuk mengedit
      if hasattr(self, "selected_data"):
          index = self.user_data.index(list(self.selected_data))
          edited_data = self.user_data[index]
          self.nama_var.set(edited_data[0])
          self.ktp_var.set(edited_data[1])
          self.telp_var.set(edited_data[2])
          self.pinjaman_var.set(edited_data[3])

    def delete_data(self):
      # Menghapus data terpilih
      if hasattr(self, "selected_data"):
          index = self.user_data.index(list(self.selected_data))
          self.user_data.pop(index)
          self.update_admin_tree()
          self.clear_inputs()

    def clear_inputs(self):
        self.nama_var.set("")
        self.ktp_var.set("")
        self.telp_var.set("")
        self.pinjaman_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoanApp(root)
    root.mainloop()
