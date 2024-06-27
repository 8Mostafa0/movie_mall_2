import customtkinter as ct
class main_screen(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Set the frame's background color
        self.configure()

        # Add a label to the frame
        self.label = ct.CTkLabel(self, text="Hello, CustomTkinter!")
        self.label.pack(padx=20, pady=20)

        # Add a button to the frame
        self.button = ct.CTkButton(self, text="Click me!")
        self.button.pack(padx=20, pady=20)