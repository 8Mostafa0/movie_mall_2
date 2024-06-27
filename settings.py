import customtkinter as ct
import requests
from PIL import Image
from io import BytesIO
import json
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import threading

def get_data():
    res = requests.get("https://api.watchmode.com/v1/releases/?apiKey=UlaSHoMz8hPfNZvDogdU8M3cRsBKYMhHPCjaJBdg")
    data = json.loads(res.content)
    
    return data['releases']


class settings(ct.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Create the scrollable frame
        self.scrollable_frame = ct.CTkScrollableFrame(self, height=400)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.loading_thread = threading.Thread(target=self.load_cards)
        self.loading_thread.start()
        self.current_progress = 0.0



    def load_cards(self):
        data = get_data()
        for i in data:
            self.show_loading_card()
            self.add_card(i['title'], i['poster_url'])
            self.current_progress = 1.0
            self.remove_loading()
            self.current_progress = 0.0

        # Remove the loading card
    def remove_loading(self):
        for child in self.scrollable_frame.winfo_children():
            if isinstance(child, ct.CTkFrame) and any(widget.cget("text") == "Loading..." for widget in child.winfo_children()):
                child.destroy()

    def show_loading_card(self):
        # Create the loading card frame
        self.loading_card_frame = ct.CTkFrame(self.scrollable_frame, corner_radius=10)
        self.loading_card_frame.pack(side=ct.BOTTOM,fill="x", padx=10, pady=10)

        # Add the loading label
        self.loading_label = ct.CTkLabel(self.loading_card_frame, text="Loading...", font=("Arial", 16, "bold"))
        self.loading_label.pack(side="left", padx=10, pady=10)

        # Add the loading progress bar
        self.loading_progress_bar = ct.CTkProgressBar(self.loading_card_frame, orientation="horizontal", width=200)
        self.loading_progress_bar.pack(side="right", padx=10, pady=10)
        self.update_loading_progress()

    def update_loading_progress(self):
        self.loading_progress_bar.set(self.current_progress)
        self.current_progress += 0.01

        if self.current_progress <= 1.0:
            self.after(100, self.update_loading_progress)
        else:
            self.loading_card_frame.destroy()
            self.loading_complete = True



    def add_card(self, title, image_path):
        retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retries)

        session = requests.Session()
        session.mount('https://', adapter)
        
        response = session.get(image_path)
        image = Image.open(BytesIO(response.content))
        # Create a card frame
        card_frame = ct.CTkFrame(self.scrollable_frame, corner_radius=10)
        card_frame.pack(fill="x", padx=10, pady=10)
        image = ct.CTkImage(light_image=image, size=(150, 150))
        image_label = ct.CTkLabel(card_frame, image=image,text="")
        image_label.pack(side="left", padx=10, pady=10)

        # Add the title
        title_label = ct.CTkLabel(card_frame, text=title, font=("Arial", 16, "bold"))
        title_label.pack(side="left", padx=10, pady=10)

        # Add the download button
        download_button = ct.CTkButton(card_frame, text="Download",command=get_data)
        download_button.pack(side="right", padx=10, pady=10)

