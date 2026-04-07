import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os

# ─── BACKEND (unchanged) ────────────────────────────────────────────────────

def garis20():
    pass  # tidak diperlukan di GUI

def clear():
    pass  # tidak diperlukan di GUI

alert = None
uang = 0
member = False
users = {}
user_data = {}
current_user = None

def set_alert(pesan):
    global alert
    alert = pesan

def show_alert():
    global alert
    if alert:
        msg = alert
        alert = None
        return msg
    return None

def sync_data():
    global current_user, uang, member
    if current_user:
        user_data[current_user]["uang"] = uang
        user_data[current_user]["member"] = member

def top_up(saldo_saat_ini, jumlah_str):
    try:
        jumlah = int(jumlah_str)
        if jumlah <= 0:
            set_alert("⚠️ Jumlah top up harus lebih dari 0!")
            return saldo_saat_ini
        set_alert(f"✅ Top up berhasil! Saldo Rp {jumlah:,} telah ditambahkan.")
        hasil = saldo_saat_ini + jumlah
        sync_data()
        return hasil
    except:
        set_alert("⚠️ Input top up tidak valid!")
        return saldo_saat_ini

def pilih_member():
    global uang, member
    harga_member = 20000
    if uang >= harga_member:
        uang -= harga_member
        member = True
        set_alert(f"✅ Berhasil join member! Sisa saldo: Rp {uang:,}")
        sync_data()
        return True
    else:
        set_alert(f"⚠️ Saldo tidak cukup. Harga: Rp {harga_member:,}, Saldo: Rp {uang:,}")
        return False

stasiun = [
    "Jakarta Kota", "Tangerang", "Bogor", "Bekasi", "Duri",
    "Rangkasbitung", "Cikarang", "Depok", "Serpong", "Cilebut"
]

def hitung_rute(stasiunAwal, stasiunTujuan):
    stasiun_lower = [s.lower() for s in stasiun]
    if stasiunAwal.lower() not in stasiun_lower or stasiunTujuan.lower() not in stasiun_lower:
        set_alert("⚠️ Stasiun tidak valid!")
        return None
    indexAwal = stasiun_lower.index(stasiunAwal.lower())
    indexTujuan = stasiun_lower.index(stasiunTujuan.lower())
    jarak = abs(indexTujuan - indexAwal)
    hargaPerStasiun = 5000
    if member:
        hargaPerStasiun *= 0.70
    harga = int(jarak * hargaPerStasiun)
    return {
        "awal": stasiun[indexAwal],
        "tujuan": stasiun[indexTujuan],
        "jarak": jarak,
        "harga": harga,
        "diskon": member
    }

def konfirmasi_rute(rute_info):
    global uang
    harga = rute_info["harga"]
    if uang >= harga:
        uang -= harga
        set_alert(f"✅ Tiket berhasil dibeli! Sisa saldo: Rp {uang:,}")
        sync_data()
        return True
    else:
        set_alert("⚠️ Saldo tidak cukup!")
        return False

def do_register(username, password):
    if not username or not password:
        set_alert("⚠️ Username dan password tidak boleh kosong!")
        return False
    if username in users:
        set_alert("⚠️ Username sudah terdaftar!")
        return False
    users[username] = password
    user_data[username] = {"uang": 0, "member": False}
    set_alert("✅ Registrasi berhasil!")
    return True

def do_login(username, password):
    global current_user, uang, member
    if username in users and users[username] == password:
        current_user = username
        uang = user_data[username]["uang"]
        member = user_data[username]["member"]
        set_alert("✅ Login berhasil!")
        return True
    else:
        set_alert("⚠️ Username atau password salah!")
        return False

def do_logout():
    global current_user, uang, member
    sync_data()
    current_user = None
    uang = 0
    member = False
    set_alert("✅ Logout berhasil!")

# ─── GUI ─────────────────────────────────────────────────────────────────────

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Warna tema
BG_DARK    = "#0A0F1E"
BG_CARD    = "#111827"
BG_FIELD   = "#1C2333"
ACCENT     = "#3B82F6"
ACCENT2    = "#6366F1"
SUCCESS    = "#10B981"
WARNING    = "#F59E0B"
TEXT_PRI   = "#F1F5F9"
TEXT_SEC   = "#94A3B8"
BORDER     = "#1E293B"


class CommuterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KRL Commuter Line")
        self.geometry("420x680")
        self.minsize(420, 680)
        self.configure(fg_color=BG_DARK)
        self.resizable(True, True)

        self._pending_rute = None
        self._show_landing()

    # ─── Helpers ─────────────────────────────────────────────────────────

    def _clear_frame(self):
        for w in self.winfo_children():
            w.destroy()

    def _toast(self, msg, color=SUCCESS):
        """Floating toast notification."""
        toast = ctk.CTkFrame(self, fg_color=color, corner_radius=10)
        toast.place(relx=0.5, rely=0.97, anchor="s", relwidth=0.88)
        ctk.CTkLabel(toast, text=msg, text_color="#FFFFFF",
                     font=("Helvetica", 12), wraplength=330).pack(pady=8, padx=10)
        self.after(2500, toast.destroy)

    def _check_alert(self):
        msg = show_alert()
        if msg:
            color = SUCCESS if "✅" in msg else WARNING
            self._toast(msg, color)

    def _header(self, parent, title, subtitle=None):
        ctk.CTkLabel(parent, text=title,
                     font=("Helvetica", 26, "bold"),
                     text_color=TEXT_PRI).pack(pady=(0, 2))
        if subtitle:
            ctk.CTkLabel(parent, text=subtitle,
                         font=("Helvetica", 13),
                         text_color=TEXT_SEC).pack(pady=(0, 18))

    def _card(self, parent, **kw):
        return ctk.CTkFrame(parent, fg_color=BG_CARD, corner_radius=16,
                            border_width=1, border_color=BORDER, **kw)

    def _btn(self, parent, text, cmd, full=True, color=ACCENT, hover=None, **kw):
        hover = hover or self._darken(color)
        b = ctk.CTkButton(parent, text=text, command=cmd,
                          fg_color=color, hover_color=hover,
                          font=("Helvetica", 13, "bold"),
                          corner_radius=10, height=44, **kw)
        if full:
            b.pack(fill="x", pady=4)
        return b

    def _entry(self, parent, placeholder, show=None):
        e = ctk.CTkEntry(parent, placeholder_text=placeholder,
                         fg_color=BG_FIELD, border_color=BORDER,
                         text_color=TEXT_PRI, placeholder_text_color=TEXT_SEC,
                         corner_radius=10, height=44, show=show or "")
        e.pack(fill="x", pady=4)
        return e

    def _divider(self, parent):
        ctk.CTkFrame(parent, height=1, fg_color=BORDER).pack(fill="x", pady=10)

    @staticmethod
    def _darken(hex_color):
        # simple darken for hover
        mapping = {
            ACCENT: "#2563EB", ACCENT2: "#4F46E5",
            SUCCESS: "#059669", WARNING: "#D97706",
            "#374151": "#1F2937"
        }
        return mapping.get(hex_color, "#1e3a5f")

    # ─── LANDING ─────────────────────────────────────────────────────────

    def _show_landing(self):
        self._clear_frame()

        # top stripe
        stripe = ctk.CTkFrame(self, height=4, fg_color=ACCENT, corner_radius=0)
        stripe.pack(fill="x")

        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(expand=True, fill="both", padx=30)

        # logo area
        ctk.CTkLabel(main, text="🚆", font=("Helvetica", 56)).pack(pady=(50, 0))
        ctk.CTkLabel(main, text="KRL Commuter Line",
                     font=("Helvetica", 24, "bold"),
                     text_color=TEXT_PRI).pack(pady=(6, 2))
        ctk.CTkLabel(main, text="Sistem Tiket Digital",
                     font=("Helvetica", 13),
                     text_color=TEXT_SEC).pack(pady=(0, 40))

        card = self._card(main)
        card.pack(fill="x", pady=4)
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=20)

        self._btn(inner, "Login", self._show_login)
        self._btn(inner, "Register", self._show_register, color=ACCENT2)

        ctk.CTkLabel(main, text="© 2025 KRL Digital System",
                     font=("Helvetica", 10),
                     text_color=TEXT_SEC).pack(pady=(30, 0))
        self._check_alert()

    # ─── REGISTER ────────────────────────────────────────────────────────

    def _show_register(self):
        self._clear_frame()
        main = ctk.CTkScrollableFrame(self, fg_color=BG_DARK)
        main.pack(expand=True, fill="both", padx=30, pady=30)

        self._header(main, "Buat Akun", "Daftar untuk memulai perjalanan")

        card = self._card(main)
        card.pack(fill="x")
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(inner, text="Username", font=("Helvetica", 12),
                     text_color=TEXT_SEC).pack(anchor="w")
        e_user = self._entry(inner, "Masukkan username")

        ctk.CTkLabel(inner, text="Password", font=("Helvetica", 12),
                     text_color=TEXT_SEC).pack(anchor="w", pady=(8, 0))
        e_pass = self._entry(inner, "Masukkan password", show="●")

        self._divider(inner)

        def do():
            if do_register(e_user.get(), e_pass.get()):
                self._check_alert()
                self.after(800, self._show_landing)
            else:
                self._check_alert()

        self._btn(inner, "Daftar Sekarang", do)
        self._btn(inner, "← Kembali", self._show_landing,
                  color="#374151", hover="#1F2937")

    # ─── LOGIN ───────────────────────────────────────────────────────────

    def _show_login(self):
        self._clear_frame()
        main = ctk.CTkScrollableFrame(self, fg_color=BG_DARK)
        main.pack(expand=True, fill="both", padx=30, pady=30)

        self._header(main, "Selamat Datang", "Masuk ke akun Anda")

        card = self._card(main)
        card.pack(fill="x")
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(inner, text="Username", font=("Helvetica", 12),
                     text_color=TEXT_SEC).pack(anchor="w")
        e_user = self._entry(inner, "Masukkan username")

        ctk.CTkLabel(inner, text="Password", font=("Helvetica", 12),
                     text_color=TEXT_SEC).pack(anchor="w", pady=(8, 0))
        e_pass = self._entry(inner, "Masukkan password", show="●")

        self._divider(inner)

        def do():
            if do_login(e_user.get(), e_pass.get()):
                self._check_alert()
                self.after(600, self._show_dashboard)
            else:
                self._check_alert()

        self._btn(inner, "Login", do)
        self._btn(inner, "← Kembali", self._show_landing,
                  color="#374151", hover="#1F2937")

    # ─── DASHBOARD ───────────────────────────────────────────────────────

    def _show_dashboard(self):
        self._clear_frame()
        main = ctk.CTkScrollableFrame(self, fg_color=BG_DARK)
        main.pack(expand=True, fill="both", padx=24, pady=24)

        # Greeting
        ctk.CTkLabel(main, text=f"Halo, {current_user} 👋",
                     font=("Helvetica", 22, "bold"),
                     text_color=TEXT_PRI).pack(anchor="w", pady=(0, 4))
        ctk.CTkLabel(main, text="Mau pergi ke mana hari ini?",
                     font=("Helvetica", 13), text_color=TEXT_SEC).pack(anchor="w")

        # Saldo card
        saldo_card = ctk.CTkFrame(main, fg_color=ACCENT, corner_radius=16, height=90)
        saldo_card.pack(fill="x", pady=(18, 6))
        saldo_card.pack_propagate(False)

        sc_inner = ctk.CTkFrame(saldo_card, fg_color="transparent")
        sc_inner.place(relx=0.05, rely=0.5, anchor="w")
        ctk.CTkLabel(sc_inner, text="SALDO ANDA", font=("Helvetica", 10, "bold"),
                     text_color="#BFD4FF").pack(anchor="w")
        ctk.CTkLabel(sc_inner, text=f"Rp {uang:,}",
                     font=("Helvetica", 26, "bold"),
                     text_color="#FFFFFF").pack(anchor="w")

        # Badge member
        if member:
            badge = ctk.CTkFrame(saldo_card, fg_color="#1D4ED8", corner_radius=8)
            badge.place(relx=0.95, rely=0.5, anchor="e", x=-14)
            ctk.CTkLabel(badge, text="✦ MEMBER", font=("Helvetica", 10, "bold"),
                         text_color="#FFFFFF").pack(padx=10, pady=4)

        # Menu grid
        ctk.CTkLabel(main, text="Menu", font=("Helvetica", 14, "bold"),
                     text_color=TEXT_SEC).pack(anchor="w", pady=(20, 8))

        grid = ctk.CTkFrame(main, fg_color="transparent")
        grid.pack(fill="x")
        grid.columnconfigure((0, 1), weight=1)

        menus = [
            ("🗺️", "Pilih Rute", self._show_pilih_rute, ACCENT),
            ("🚉", "Daftar Stasiun", self._show_stasiun, ACCENT2),
            ("💳", "Isi Saldo", self._show_top_up, SUCCESS),
            ("👑", "Member", self._show_member, WARNING),
        ]

        for i, (icon, label, cmd, color) in enumerate(menus):
            btn_card = ctk.CTkFrame(grid, fg_color=BG_CARD, corner_radius=14,
                                    border_width=1, border_color=BORDER)
            btn_card.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")
            btn_card.configure(cursor="hand2")

            inner = ctk.CTkFrame(btn_card, fg_color="transparent")
            inner.pack(expand=True, padx=14, pady=16)

            dot = ctk.CTkFrame(inner, fg_color=color, width=40, height=40,
                               corner_radius=12)
            dot.pack(pady=(0, 8))
            dot.pack_propagate(False)
            ctk.CTkLabel(dot, text=icon, font=("Helvetica", 18)).pack(expand=True)

            ctk.CTkLabel(inner, text=label, font=("Helvetica", 12, "bold"),
                         text_color=TEXT_PRI).pack()

            btn_card.bind("<Button-1>", lambda e, c=cmd: c())
            for child in btn_card.winfo_children():
                child.bind("<Button-1>", lambda e, c=cmd: c())
                for gc in child.winfo_children():
                    gc.bind("<Button-1>", lambda e, c=cmd: c())

        # Logout
        self._divider(main)
        self._btn(main, "Logout", self._do_logout, color="#374151", hover="#1F2937")
        self._check_alert()

    # ─── DAFTAR STASIUN ──────────────────────────────────────────────────

    def _show_stasiun(self):
        self._clear_frame()
        main = ctk.CTkScrollableFrame(self, fg_color=BG_DARK)
        main.pack(expand=True, fill="both", padx=24, pady=24)

        self._header(main, "Daftar Stasiun", f"{len(stasiun)} stasiun tersedia")

        for i, s in enumerate(stasiun):
            row = ctk.CTkFrame(main, fg_color=BG_CARD, corner_radius=12,
                               border_width=1, border_color=BORDER)
            row.pack(fill="x", pady=3)
            inner = ctk.CTkFrame(row, fg_color="transparent")
            inner.pack(fill="x", padx=16, pady=12)

            num = ctk.CTkFrame(inner, fg_color=ACCENT, width=30, height=30,
                               corner_radius=8)
            num.pack(side="left", padx=(0, 12))
            num.pack_propagate(False)
            ctk.CTkLabel(num, text=str(i+1), font=("Helvetica", 11, "bold"),
                         text_color="#FFF").pack(expand=True)

            ctk.CTkLabel(inner, text=s, font=("Helvetica", 13),
                         text_color=TEXT_PRI).pack(side="left")

        self._divider(main)
        self._btn(main, "← Kembali ke Dashboard", self._show_dashboard,
                  color="#374151", hover="#1F2937")

    # ─── PILIH RUTE ──────────────────────────────────────────────────────

    def _show_pilih_rute(self):
        self._clear_frame()
        main = ctk.CTkScrollableFrame(self, fg_color=BG_DARK)
        main.pack(expand=True, fill="both", padx=24, pady=24)

        self._header(main, "Pilih Rute", "Tentukan perjalanan Anda")

        card = self._card(main)
        card.pack(fill="x")
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=20)

        # Stasiun dropdown
        ctk.CTkLabel(inner, text="Stasiun Asal", font=("Helvetica", 12),
                     text_color=TEXT_SEC).pack(anchor="w")
        var_awal = ctk.StringVar(value=stasiun[0])
        dd_awal = ctk.CTkOptionMenu(inner, values=stasiun, variable=var_awal,
                                    fg_color=BG_FIELD, button_color=ACCENT,
                                    button_hover_color="#2563EB",
                                    text_color=TEXT_PRI, corner_radius=10,
                                    dropdown_fg_color=BG_CARD,
                                    dropdown_text_color=TEXT_PRI)
        dd_awal.pack(fill="x", pady=4)

        ctk.CTkLabel(inner, text="Stasiun Tujuan", font=("Helvetica", 12),
                     text_color=TEXT_SEC).pack(anchor="w", pady=(8, 0))
        var_tujuan = ctk.StringVar(value=stasiun[1])
        dd_tujuan = ctk.CTkOptionMenu(inner, values=stasiun, variable=var_tujuan,
                                      fg_color=BG_FIELD, button_color=ACCENT,
                                      button_hover_color="#2563EB",
                                      text_color=TEXT_PRI, corner_radius=10,
                                      dropdown_fg_color=BG_CARD,
                                      dropdown_text_color=TEXT_PRI)
        dd_tujuan.pack(fill="x", pady=4)

        # Result area
        result_frame = ctk.CTkFrame(inner, fg_color="transparent")
        result_frame.pack(fill="x")

        def cari():
            for w in result_frame.winfo_children():
                w.destroy()
            awal = var_awal.get()
            tujuan = var_tujuan.get()
            if awal == tujuan:
                self._toast("⚠️ Stasiun asal dan tujuan sama!", WARNING)
                return
            info = hitung_rute(awal, tujuan)
            if not info:
                self._check_alert()
                return

            self._divider(result_frame)

            def row_info(lbl, val, accent=False):
                r = ctk.CTkFrame(result_frame, fg_color="transparent")
                r.pack(fill="x", pady=2)
                ctk.CTkLabel(r, text=lbl, font=("Helvetica", 12),
                             text_color=TEXT_SEC, width=90, anchor="w").pack(side="left")
                ctk.CTkLabel(r, text=val,
                             font=("Helvetica", 13, "bold" if accent else "normal"),
                             text_color=ACCENT if accent else TEXT_PRI).pack(side="left")

            row_info("Dari", info["awal"])
            row_info("Ke", info["tujuan"])
            row_info("Jarak", f"{info['jarak']} stasiun")
            row_info("Harga", f"Rp {info['harga']:,}", accent=True)

            if info["diskon"]:
                disc = ctk.CTkFrame(result_frame, fg_color="#064E3B", corner_radius=8)
                disc.pack(fill="x", pady=6)
                ctk.CTkLabel(disc, text="✦ Diskon 30% member aktif",
                             font=("Helvetica", 11, "bold"),
                             text_color=SUCCESS).pack(pady=6)

            def beli():
                if konfirmasi_rute(info):
                    self._check_alert()
                    self.after(600, self._show_dashboard)
                else:
                    self._check_alert()

            self._btn(result_frame, f"Beli Tiket  •  Rp {info['harga']:,}", beli)

        self._divider(inner)
        self._btn(inner, "Cari Rute", cari)
        self._btn(inner, "← Kembali", self._show_dashboard,
                  color="#374151", hover="#1F2937")

    # ─── TOP UP ──────────────────────────────────────────────────────────

    def _show_top_up(self):
        self._clear_frame()
        main = ctk.CTkScrollableFrame(self, fg_color=BG_DARK)
        main.pack(expand=True, fill="both", padx=24, pady=24)

        self._header(main, "Isi Saldo", "Tambah saldo untuk perjalanan")

        # Saldo card
        sc = ctk.CTkFrame(main, fg_color=ACCENT, corner_radius=14)
        sc.pack(fill="x", pady=(0, 16))
        ctk.CTkLabel(sc, text="SALDO SAAT INI", font=("Helvetica", 10, "bold"),
                     text_color="#BFD4FF").pack(pady=(14, 0))
        ctk.CTkLabel(sc, text=f"Rp {uang:,}",
                     font=("Helvetica", 28, "bold"),
                     text_color="#FFF").pack(pady=(0, 14))

        card = self._card(main)
        card.pack(fill="x")
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(inner, text="Jumlah Top Up", font=("Helvetica", 12),
                     text_color=TEXT_SEC).pack(anchor="w")
        e_jumlah = self._entry(inner, "Contoh: 50000")

        # Quick select
        ctk.CTkLabel(inner, text="Pilih Cepat", font=("Helvetica", 12),
                     text_color=TEXT_SEC).pack(anchor="w", pady=(10, 4))
        quick = ctk.CTkFrame(inner, fg_color="transparent")
        quick.pack(fill="x")
        quick.columnconfigure((0, 1, 2), weight=1)
        for i, nominal in enumerate([20000, 50000, 100000]):
            def fill(n=nominal):
                e_jumlah.delete(0, "end")
                e_jumlah.insert(0, str(n))
            ctk.CTkButton(quick, text=f"Rp {nominal:,}", command=fill,
                          fg_color=BG_FIELD, hover_color=BORDER,
                          text_color=TEXT_PRI, font=("Helvetica", 11),
                          corner_radius=8, height=36).grid(row=0, column=i,
                          padx=3, pady=2, sticky="ew")

        self._divider(inner)

        def do():
            global uang
            uang = top_up(uang, e_jumlah.get())
            self._check_alert()
            self.after(600, self._show_top_up)

        self._btn(inner, "Top Up Sekarang", do)
        self._btn(inner, "← Kembali", self._show_dashboard,
                  color="#374151", hover="#1F2937")

    # ─── MEMBER ──────────────────────────────────────────────────────────

    def _show_member(self):
        self._clear_frame()
        main = ctk.CTkScrollableFrame(self, fg_color=BG_DARK)
        main.pack(expand=True, fill="both", padx=24, pady=24)

        self._header(main, "Membership", "Nikmati keuntungan lebih")

        # Status card
        status_color = SUCCESS if member else BG_CARD
        status_card = ctk.CTkFrame(main, fg_color=status_color, corner_radius=14,
                                   border_width=1,
                                   border_color=SUCCESS if member else BORDER)
        status_card.pack(fill="x", pady=(0, 16))
        inner_s = ctk.CTkFrame(status_card, fg_color="transparent")
        inner_s.pack(padx=20, pady=16)

        if member:
            ctk.CTkLabel(inner_s, text="✦ MEMBER AKTIF", font=("Helvetica", 16, "bold"),
                         text_color="#FFFFFF").pack()
            ctk.CTkLabel(inner_s, text="Anda menikmati diskon 30% setiap perjalanan",
                         font=("Helvetica", 12), text_color="#D1FAE5").pack(pady=(4, 0))
        else:
            ctk.CTkLabel(inner_s, text="Belum jadi member",
                         font=("Helvetica", 15, "bold"),
                         text_color=TEXT_PRI).pack()
            ctk.CTkLabel(inner_s, text="Bergabung dan hemat lebih banyak!",
                         font=("Helvetica", 12), text_color=TEXT_SEC).pack(pady=(4, 0))

        # Benefits
        card = self._card(main)
        card.pack(fill="x")
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=20)

        ctk.CTkLabel(inner, text="Keuntungan Member", font=("Helvetica", 14, "bold"),
                     text_color=TEXT_PRI).pack(anchor="w", pady=(0, 10))

        benefits = [
            ("🎫", "Diskon 30% semua rute"),
            ("⚡", "Akses prioritas layanan"),
            ("💰", "Hemat lebih banyak setiap perjalanan"),
        ]
        for icon, text in benefits:
            row = ctk.CTkFrame(inner, fg_color=BG_FIELD, corner_radius=10)
            row.pack(fill="x", pady=3)
            ri = ctk.CTkFrame(row, fg_color="transparent")
            ri.pack(fill="x", padx=14, pady=10)
            ctk.CTkLabel(ri, text=icon, font=("Helvetica", 16)).pack(side="left",
                         padx=(0, 10))
            ctk.CTkLabel(ri, text=text, font=("Helvetica", 12),
                         text_color=TEXT_PRI).pack(side="left")

        self._divider(inner)

        if not member:
            # Price info
            price_row = ctk.CTkFrame(inner, fg_color="transparent")
            price_row.pack(fill="x", pady=(0, 6))
            ctk.CTkLabel(price_row, text="Biaya bergabung:",
                         font=("Helvetica", 12), text_color=TEXT_SEC).pack(side="left")
            ctk.CTkLabel(price_row, text="Rp 20,000",
                         font=("Helvetica", 14, "bold"),
                         text_color=ACCENT).pack(side="right")

            def do():
                if pilih_member():
                    self._check_alert()
                    self.after(600, self._show_member)
                else:
                    self._check_alert()

            self._btn(inner, "Bergabung Sekarang  •  Rp 20,000", do, color=SUCCESS,
                      hover="#059669")
        
        self._btn(inner, "← Kembali", self._show_dashboard,
                  color="#374151", hover="#1F2937")
        self._check_alert()

    # ─── LOGOUT ──────────────────────────────────────────────────────────

    def _do_logout(self):
        do_logout()
        self._check_alert()
        self.after(600, self._show_landing)


if __name__ == "__main__":
    app = CommuterApp()
    app.mainloop()
