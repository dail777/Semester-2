import customtkinter as ctk
from tkinter import messagebox

# ─────────────────────────────────────────────
#  BACKEND (tidak diubah sama sekali)
# ─────────────────────────────────────────────

alert = None
uang = 0
member = False

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

def top_up(saldo_saat_ini, jumlah_str):
    try:
        jumlah = int(jumlah_str)
        set_alert(f"✅ Top up berhasil! Saldo {jumlah} telah ditambahkan.")
        return saldo_saat_ini + jumlah
    except:
        set_alert("⚠️ Input top up tidak valid!")
        return saldo_saat_ini

def pilih_member_logic():
    global uang, member
    harga_member = 20000
    if uang >= harga_member:
        uang -= harga_member
        member = True
        set_alert(f"✅ Berhasil join member! Sisa saldo: {uang}")
    else:
        set_alert(f"⚠️ Saldo tidak cukup. Harga: {harga_member}, Saldo: {uang}")

stasiun = [
    "Jakarta Kota", "Tanggerang", "Bogor", "Bekasi", "Duri",
    "Rangkasbitung", "Cikarang", "Depok", "Serpong", "Cilebut"
]

def hitung_rute(stasiunAwal, stasiunTujuan):
    stasiun_lower = [s.lower() for s in stasiun]
    if stasiunAwal.lower() not in stasiun_lower or stasiunTujuan.lower() not in stasiun_lower:
        set_alert("⚠️ Stasiun tidak valid!")
        return None
    indexAwal   = stasiun_lower.index(stasiunAwal.lower())
    indexTujuan = stasiun_lower.index(stasiunTujuan.lower())
    jarak = abs(indexTujuan - indexAwal)
    hargaPerStasiun = 5000
    if member:
        hargaPerStasiun *= 0.7
    harga = int(jarak * hargaPerStasiun)
    return {"dari": stasiun[indexAwal], "ke": stasiun[indexTujuan],
            "jarak": jarak, "harga": harga, "diskon": member}

def bayar_rute(harga):
    global uang
    if uang >= harga:
        uang -= harga
        set_alert(f"✅ Rute berhasil dipilih! Sisa saldo: {uang}")
        return True
    else:
        set_alert("⚠️ Saldo tidak cukup!")
        return False

users = {}

def register_logic(username, password):
    if username in users:
        set_alert("⚠️ Username sudah terdaftar!")
        return False
    users[username] = password
    set_alert("✅ Registrasi berhasil!")
    return True

def login_logic(username, password):
    if username in users and users[username] == password:
        set_alert("✅ Login berhasil!")
        return True
    set_alert("⚠️ Username atau password salah!")
    return False

# ─────────────────────────────────────────────
#  TAMPILAN / UI
# ─────────────────────────────────────────────

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FONT_TITLE  = ("Segoe UI", 22, "bold")
FONT_SUB    = ("Segoe UI", 13)
FONT_BODY   = ("Segoe UI", 14)
FONT_SMALL  = ("Segoe UI", 12)
FONT_MONO   = ("Consolas",  13)

CLR_BG      = "#1a1a2e"
CLR_CARD    = "#16213e"
CLR_ACCENT  = "#0f3460"
CLR_BLUE    = "#4a9eff"
CLR_GREEN   = "#4caf7d"
CLR_AMBER   = "#ffb347"
CLR_RED     = "#ff6b6b"
CLR_TEXT    = "#e0e0e0"
CLR_MUTED   = "#8a8a9a"
CLR_BORDER  = "#2a2a4e"


class CommuterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Commuter Line — Sistem Tiket Digital")
        self.geometry("460x640")
        self.resizable(False, False)
        self.configure(fg_color=CLR_BG)

        self.current_user = None
        self._frames = {}
        self._route_data = None

        container = ctk.CTkFrame(self, fg_color=CLR_BG)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (MainScreen, RegisterScreen, LoginScreen, MenuScreen,
                  StationsScreen, RouteScreen, RouteConfirmScreen,
                  SaldoScreen, TopupScreen, MemberScreen):
            frame = F(container, self)
            self._frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show(MainScreen)

    def show(self, screen_class):
        frame = self._frames[screen_class]
        frame.on_show()
        frame.tkraise()

    def popup(self, msg, kind="info"):
        color = CLR_GREEN if "✅" in msg else CLR_AMBER if "⚠️" in msg else CLR_BLUE
        win = ctk.CTkToplevel(self)
        win.title("")
        win.geometry("340x140")
        win.resizable(False, False)
        win.configure(fg_color=CLR_CARD)
        win.grab_set()
        ctk.CTkLabel(win, text=msg, font=FONT_SMALL, text_color=color,
                     wraplength=300).pack(expand=True, pady=20, padx=20)
        ctk.CTkButton(win, text="OK", width=100, fg_color=CLR_ACCENT,
                      hover_color=CLR_BLUE, command=win.destroy).pack(pady=(0, 16))

    def flush_alert(self):
        msg = show_alert()
        if msg:
            self.popup(msg)


# ── helpers ──────────────────────────────────

def make_card(parent, **kw):
    return ctk.CTkFrame(parent, fg_color=CLR_CARD, corner_radius=14,
                        border_width=1, border_color=CLR_BORDER, **kw)

def make_label(parent, text, font=FONT_BODY, color=CLR_TEXT, **kw):
    return ctk.CTkLabel(parent, text=text, font=font, text_color=color, **kw)

def make_entry(parent, placeholder="", show=""):
    return ctk.CTkEntry(parent, placeholder_text=placeholder,
                        fg_color=CLR_ACCENT, border_color=CLR_BORDER,
                        text_color=CLR_TEXT, placeholder_text_color=CLR_MUTED,
                        corner_radius=8, height=40, show=show)

def make_btn(parent, text, cmd, color=CLR_BLUE, hover=None, **kw):
    hover = hover or color
    return ctk.CTkButton(parent, text=text, command=cmd,
                         fg_color=color, hover_color=hover,
                         text_color="#ffffff", corner_radius=10,
                         font=FONT_BODY, height=42, **kw)

def make_ghost_btn(parent, text, cmd, color=CLR_MUTED, **kw):
    return ctk.CTkButton(parent, text=text, command=cmd,
                         fg_color="transparent", hover_color=CLR_ACCENT,
                         text_color=color, corner_radius=8,
                         font=FONT_SMALL, height=36, **kw)

def divider(parent):
    ctk.CTkFrame(parent, height=1, fg_color=CLR_BORDER).pack(fill="x", pady=8)

def info_row(parent, label, value, val_color=CLR_TEXT):
    row = ctk.CTkFrame(parent, fg_color="transparent")
    row.pack(fill="x", pady=3)
    make_label(row, label, font=FONT_SMALL, color=CLR_MUTED, anchor="w").pack(side="left")
    make_label(row, value, font=FONT_SMALL, color=val_color, anchor="e").pack(side="right")


# ── screens ───────────────────────────────────

class BaseScreen(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color=CLR_BG)
        self.app = app
    def on_show(self): pass


class MainScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)

        card = make_card(self)
        card.pack(fill="both", expand=True)

        # header
        head = ctk.CTkFrame(card, fg_color=CLR_ACCENT, corner_radius=12)
        head.pack(fill="x", padx=16, pady=(16, 12))
        make_label(head, "🚆", font=("Segoe UI", 40)).pack(pady=(14, 2))
        make_label(head, "Commuter Line", font=FONT_TITLE).pack()
        make_label(head, "Sistem Tiket Digital", font=FONT_SMALL, color=CLR_MUTED).pack(pady=(0, 14))

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=16, pady=8)

        make_btn(body, "👤  Register", lambda: app.show(RegisterScreen),
                 color="#1e3a5f", hover=CLR_BLUE).pack(fill="x", pady=6)
        make_btn(body, "🔐  Login", lambda: app.show(LoginScreen),
                 color="#1a3d2b", hover=CLR_GREEN).pack(fill="x", pady=6)
        make_btn(body, "✖  Keluar", self._keluar,
                 color="#3d1a1a", hover=CLR_RED).pack(fill="x", pady=6)

    def _keluar(self):
        if messagebox.askyesno("Keluar", "Yakin ingin keluar?"):
            self.app.destroy()


class RegisterScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        make_ghost_btn(card, "← Kembali", lambda: app.show(MainScreen),
                       anchor="w").pack(anchor="w", padx=16, pady=(14, 0))
        make_label(card, "Register Akun", font=FONT_TITLE).pack(pady=(4, 14))

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="x", padx=20)

        make_label(body, "Username", font=FONT_SMALL, color=CLR_MUTED, anchor="w").pack(fill="x")
        self.ent_user = make_entry(body, "Masukkan username")
        self.ent_user.pack(fill="x", pady=(2, 10))

        make_label(body, "Password", font=FONT_SMALL, color=CLR_MUTED, anchor="w").pack(fill="x")
        self.ent_pass = make_entry(body, "Masukkan password", show="●")
        self.ent_pass.pack(fill="x", pady=(2, 16))

        make_btn(body, "Daftar Sekarang", self._register,
                 color=CLR_BLUE).pack(fill="x")

    def on_show(self):
        self.ent_user.delete(0, "end")
        self.ent_pass.delete(0, "end")

    def _register(self):
        u = self.ent_user.get().strip()
        p = self.ent_pass.get().strip()
        if not u or not p:
            self.app.popup("⚠️ Username dan password wajib diisi!")
            return
        ok = register_logic(u, p)
        self.app.flush_alert()
        if ok:
            self.app.show(MainScreen)


class LoginScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        make_ghost_btn(card, "← Kembali", lambda: app.show(MainScreen),
                       anchor="w").pack(anchor="w", padx=16, pady=(14, 0))
        make_label(card, "Login", font=FONT_TITLE).pack(pady=(4, 14))

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="x", padx=20)

        make_label(body, "Username", font=FONT_SMALL, color=CLR_MUTED, anchor="w").pack(fill="x")
        self.ent_user = make_entry(body, "Masukkan username")
        self.ent_user.pack(fill="x", pady=(2, 10))

        make_label(body, "Password", font=FONT_SMALL, color=CLR_MUTED, anchor="w").pack(fill="x")
        self.ent_pass = make_entry(body, "Masukkan password", show="●")
        self.ent_pass.pack(fill="x", pady=(2, 16))

        make_btn(body, "Masuk", self._login, color=CLR_GREEN).pack(fill="x")

    def on_show(self):
        self.ent_user.delete(0, "end")
        self.ent_pass.delete(0, "end")

    def _login(self):
        u = self.ent_user.get().strip()
        p = self.ent_pass.get().strip()
        ok = login_logic(u, p)
        self.app.flush_alert()
        if ok:
            self.app.current_user = u
            self.app.show(MenuScreen)


class MenuScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        # header user
        self.head = ctk.CTkFrame(card, fg_color=CLR_ACCENT, corner_radius=10)
        self.head.pack(fill="x", padx=16, pady=(16, 10))
        self.lbl_user   = make_label(self.head, "", font=FONT_TITLE)
        self.lbl_user.pack(pady=(12, 0))
        self.lbl_saldo  = make_label(self.head, "", font=FONT_BODY, color=CLR_AMBER)
        self.lbl_saldo.pack()
        self.lbl_member = make_label(self.head, "", font=FONT_SMALL, color=CLR_MUTED)
        self.lbl_member.pack(pady=(0, 12))

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=16, pady=4)

        entries = [
            ("🗺   Daftar Stasiun",  StationsScreen, "#1e3a5f", CLR_BLUE),
            ("🎫   Pilih Rute",       RouteScreen,    "#1a3d2b", CLR_GREEN),
            ("💳   Isi Saldo / Member", SaldoScreen,  "#3d3010", CLR_AMBER),
        ]
        for txt, scr, bg, hv in entries:
            make_btn(body, txt, lambda s=scr: app.show(s),
                     color=bg, hover=hv).pack(fill="x", pady=5)

        divider(body)
        make_btn(body, "↩  Logout", self._logout,
                 color="#3d1a1a", hover=CLR_RED).pack(fill="x", pady=5)

    def on_show(self):
        self.lbl_user.configure(text=f"Halo, {self.app.current_user} 👋")
        self.lbl_saldo.configure(text=f"Saldo: Rp {uang:,.0f}".replace(",", "."))
        self.lbl_member.configure(
            text="⭐ Member Aktif" if member else "Member: Tidak Aktif",
            text_color=CLR_AMBER if member else CLR_MUTED)

    def _logout(self):
        set_alert("✅ Logout berhasil!")
        self.app.flush_alert()
        self.app.current_user = None
        self.app.show(MainScreen)


class StationsScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        make_ghost_btn(card, "← Kembali", lambda: app.show(MenuScreen)).pack(
            anchor="w", padx=16, pady=(14, 0))
        make_label(card, "Daftar Stasiun", font=FONT_TITLE).pack(pady=(4, 10))

        scroll = ctk.CTkScrollableFrame(card, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=16, pady=(0, 12))

        for i, s in enumerate(stasiun, 1):
            row = ctk.CTkFrame(scroll, fg_color=CLR_ACCENT, corner_radius=8)
            row.pack(fill="x", pady=4)
            badge = ctk.CTkFrame(row, fg_color=CLR_BLUE, corner_radius=6,
                                 width=28, height=28)
            badge.pack(side="left", padx=(10, 8), pady=8)
            badge.pack_propagate(False)
            make_label(badge, str(i), font=FONT_SMALL).pack(expand=True)
            make_label(row, s, font=FONT_BODY, anchor="w").pack(
                side="left", pady=8)

        make_btn(card, "Pilih Rute →",
                 lambda: app.show(RouteScreen),
                 color=CLR_GREEN).pack(fill="x", padx=16, pady=(0, 14))


class RouteScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        make_ghost_btn(card, "← Kembali", lambda: app.show(MenuScreen)).pack(
            anchor="w", padx=16, pady=(14, 0))
        make_label(card, "Pilih Rute", font=FONT_TITLE).pack(pady=(4, 14))

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="x", padx=20)

        make_label(body, "Stasiun Asal", font=FONT_SMALL, color=CLR_MUTED,
                   anchor="w").pack(fill="x")
        self.cb_from = ctk.CTkComboBox(
            body, values=stasiun,
            fg_color=CLR_ACCENT, border_color=CLR_BORDER,
            button_color=CLR_BLUE, dropdown_fg_color=CLR_CARD,
            text_color=CLR_TEXT, dropdown_text_color=CLR_TEXT,
            corner_radius=8, height=40, state="readonly")
        self.cb_from.set("-- Pilih --")
        self.cb_from.pack(fill="x", pady=(2, 12))

        make_label(body, "Stasiun Tujuan", font=FONT_SMALL, color=CLR_MUTED,
                   anchor="w").pack(fill="x")
        self.cb_to = ctk.CTkComboBox(
            body, values=stasiun,
            fg_color=CLR_ACCENT, border_color=CLR_BORDER,
            button_color=CLR_BLUE, dropdown_fg_color=CLR_CARD,
            text_color=CLR_TEXT, dropdown_text_color=CLR_TEXT,
            corner_radius=8, height=40, state="readonly")
        self.cb_to.set("-- Pilih --")
        self.cb_to.pack(fill="x", pady=(2, 20))

        make_btn(body, "Hitung Harga →", self._hitung, color=CLR_BLUE).pack(fill="x")

    def _hitung(self):
        dari = self.cb_from.get()
        ke   = self.cb_to.get()
        if dari == "-- Pilih --" or ke == "-- Pilih --":
            self.app.popup("⚠️ Pilih stasiun asal dan tujuan!")
            return
        if dari == ke:
            self.app.popup("⚠️ Stasiun asal dan tujuan tidak boleh sama!")
            return
        result = hitung_rute(dari, ke)
        if result is None:
            self.app.flush_alert()
            return
        self.app._route_data = result
        self.app.show(RouteConfirmScreen)


class RouteConfirmScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        make_ghost_btn(card, "← Ubah Rute", lambda: app.show(RouteScreen)).pack(
            anchor="w", padx=16, pady=(14, 0))
        make_label(card, "Konfirmasi Rute", font=FONT_TITLE).pack(pady=(4, 14))

        self.body = ctk.CTkFrame(card, fg_color="transparent")
        self.body.pack(fill="both", expand=True, padx=20)

        self.detail_card = make_card(self.body)
        self.detail_card.pack(fill="x", pady=(0, 12))

        self.rows_frame = ctk.CTkFrame(self.detail_card, fg_color="transparent")
        self.rows_frame.pack(fill="x", padx=14, pady=14)

        self.lbl_promo = make_label(
            self.body,
            "💡 Jadi member dan hemat 30% setiap perjalanan!",
            font=FONT_SMALL, color=CLR_AMBER, wraplength=360)

        self.lbl_saldo_now = make_label(
            self.body, "", font=FONT_SMALL, color=CLR_MUTED)
        self.lbl_saldo_now.pack(pady=(0, 10))

        make_btn(self.body, "✅  Bayar Sekarang", self._bayar,
                 color=CLR_GREEN).pack(fill="x", pady=(0, 8))
        make_btn(self.body, "Batal", self._batal,
                 color="#3d1a1a", hover=CLR_RED).pack(fill="x")

    def on_show(self):
        r = self.app._route_data
        for w in self.rows_frame.winfo_children():
            w.destroy()

        info_row(self.rows_frame, "Dari", r["dari"], CLR_TEXT)
        info_row(self.rows_frame, "Ke",   r["ke"],   CLR_TEXT)
        info_row(self.rows_frame, "Jarak", f"{r['jarak']} stasiun", CLR_TEXT)
        info_row(self.rows_frame, "Harga",
                 f"Rp {r['harga']:,.0f}".replace(",", "."), CLR_AMBER)
        if r["diskon"]:
            info_row(self.rows_frame, "Diskon", "30% Member ⭐", CLR_GREEN)

        if r["diskon"]:
            self.lbl_promo.pack_forget()
        else:
            self.lbl_promo.pack(pady=(0, 8))

        self.lbl_saldo_now.configure(
            text=f"Saldo saat ini: Rp {uang:,.0f}".replace(",", "."))

    def _bayar(self):
        r = self.app._route_data
        ok = bayar_rute(r["harga"])
        self.app.flush_alert()
        if ok:
            self.app.show(MenuScreen)

    def _batal(self):
        set_alert("⚠️ Pembelian dibatalkan.")
        self.app.flush_alert()
        self.app.show(RouteScreen)


class SaldoScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        make_ghost_btn(card, "← Kembali", lambda: app.show(MenuScreen)).pack(
            anchor="w", padx=16, pady=(14, 0))
        make_label(card, "Saldo & Member", font=FONT_TITLE).pack(pady=(4, 14))

        info = make_card(card)
        info.pack(fill="x", padx=16, pady=(0, 14))
        inf = ctk.CTkFrame(info, fg_color="transparent")
        inf.pack(fill="x", padx=14, pady=14)

        self.lbl_saldo  = make_label(inf, "", font=("Segoe UI", 26, "bold"),
                                     color=CLR_AMBER)
        self.lbl_saldo.pack(pady=(0, 4))
        self.lbl_member = make_label(inf, "", font=FONT_SMALL, color=CLR_MUTED)
        self.lbl_member.pack()

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="x", padx=16)

        make_btn(body, "💰  Isi Saldo", lambda: app.show(TopupScreen),
                 color="#1a3d2b", hover=CLR_GREEN).pack(fill="x", pady=6)
        self.btn_member = make_btn(
            body, "⭐  Beli Member  (Rp 20.000)",
            lambda: app.show(MemberScreen), color="#3d3010", hover=CLR_AMBER)
        self.btn_member.pack(fill="x", pady=6)

    def on_show(self):
        self.lbl_saldo.configure(
            text=f"Rp {uang:,.0f}".replace(",", "."))
        self.lbl_member.configure(
            text="⭐ Member Aktif" if member else "Member: Tidak Aktif",
            text_color=CLR_AMBER if member else CLR_MUTED)
        if member:
            self.btn_member.pack_forget()
        else:
            self.btn_member.pack(fill="x", pady=6)


class TopupScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        make_ghost_btn(card, "← Kembali", lambda: app.show(SaldoScreen)).pack(
            anchor="w", padx=16, pady=(14, 0))
        make_label(card, "Isi Saldo", font=FONT_TITLE).pack(pady=(4, 14))

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="x", padx=20)

        make_label(body, "Pilih Nominal Cepat", font=FONT_SMALL,
                   color=CLR_MUTED, anchor="w").pack(fill="x", pady=(0, 6))

        grid = ctk.CTkFrame(body, fg_color="transparent")
        grid.pack(fill="x", pady=(0, 14))
        grid.columnconfigure((0, 1), weight=1)

        nominals = [20_000, 50_000, 100_000, 200_000]
        self.ent_amount = None  # akan dibuat di bawah

        def set_nominal(n):
            self.ent_amount.delete(0, "end")
            self.ent_amount.insert(0, str(n))

        for idx, n in enumerate(nominals):
            r, c = divmod(idx, 2)
            ctk.CTkButton(
                grid, text=f"Rp {n:,.0f}".replace(",", "."),
                command=lambda x=n: set_nominal(x),
                fg_color=CLR_ACCENT, hover_color=CLR_BLUE,
                text_color=CLR_TEXT, corner_radius=8,
                font=FONT_SMALL, height=38
            ).grid(row=r, column=c, padx=4, pady=4, sticky="ew")

        make_label(body, "Atau masukkan nominal lain",
                   font=FONT_SMALL, color=CLR_MUTED, anchor="w").pack(fill="x")
        self.ent_amount = make_entry(body, "Contoh: 75000")
        self.ent_amount.pack(fill="x", pady=(4, 16))

        make_btn(body, "Tambah Saldo", self._topup, color=CLR_GREEN).pack(fill="x")

    def on_show(self):
        if self.ent_amount:
            self.ent_amount.delete(0, "end")

    def _topup(self):
        global uang
        raw = self.ent_amount.get().replace(".", "").replace(",", "").strip()
        uang = top_up(uang, raw)
        self.app.flush_alert()
        self.app.show(SaldoScreen)


class MemberScreen(BaseScreen):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        card = make_card(self)
        card.pack(fill="both", expand=True)

        make_ghost_btn(card, "← Kembali", lambda: app.show(SaldoScreen)).pack(
            anchor="w", padx=16, pady=(14, 0))
        make_label(card, "Beli Member", font=FONT_TITLE).pack(pady=(4, 14))

        info = make_card(card)
        info.pack(fill="x", padx=16, pady=(0, 16))
        inf = ctk.CTkFrame(info, fg_color="transparent")
        inf.pack(fill="x", padx=14, pady=14)

        info_row(inf, "Harga Member", "Rp 20.000", CLR_TEXT)
        info_row(inf, "Keuntungan",   "Diskon 30% setiap rute", CLR_GREEN)
        self.lbl_saldo = make_label(inf, "", font=FONT_SMALL, color=CLR_MUTED)
        self.lbl_saldo.pack(anchor="w", pady=(6, 0))

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="x", padx=16)

        make_btn(body, "⭐  Beli Member", self._beli,
                 color="#3d3010", hover=CLR_AMBER).pack(fill="x", pady=6)
        make_btn(body, "Batal", lambda: app.show(SaldoScreen),
                 color="#3d1a1a", hover=CLR_RED).pack(fill="x")

    def on_show(self):
        self.lbl_saldo.configure(
            text=f"Saldo Anda: Rp {uang:,.0f}".replace(",", "."))

    def _beli(self):
        pilih_member_logic()
        self.app.flush_alert()
        self.app.show(SaldoScreen)


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    app = CommuterApp()
    app.mainloop()