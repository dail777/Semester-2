import customtkinter as ctk
class ShoppingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Shopping App")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Welcome to the Shopping App!")
        self.label.pack(pady=20)

        self.button = ctk.CTkButton(self, text="Start Shopping", command=self.start_shopping)
        self.button.pack(pady=10)

    def start_shopping(self):
        # This function will be called when the button is clicked
        print("Shopping started!")