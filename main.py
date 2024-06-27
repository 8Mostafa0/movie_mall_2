import customtkinter as ct
from mainscreen import main_screen 
from settings import settings
ct.set_appearance_mode("dark")

ct.set_default_color_theme("./theme.json")

root =  ct.CTk()

root.geometry("500x350")
root.title("Mosi")

frame = ct.CTkFrame(root)
frame.place(x=10, y=10)

frame.pack(side=ct.TOP,fill=ct.X)
frame.pack_propagate(False)
frame.configure(height=50)

main_frame = ct.CTkFrame(root)
main_frame.pack(fill="both",expand=True)

activemenu=0

class DynamicContentFrame(ct.CTkFrame):
  def __init__(self, parent):
    super().__init__(parent)
    self.widgets = []
  def change_to_setting(self):
    self.clear_widgets()
    self.my_custom_frame = settings(self)
    self.my_custom_frame.pack(fill="both", expand=True)
  def change_to_main_screen(self):
    self.clear_widgets()
    self.my_custom_frame = main_screen(self)
    self.my_custom_frame.pack(fill="both", expand=True)


  def clear_widgets(self):
    self.child_widgets = self.winfo_children()
    for widget in self.child_widgets:
      widget.pack_forget()
      widget.destroy()

def t_menu(dc):
    def colaps_menu():
        tg_menu.destroy()
        toggle_bt.configure(text="X")
        toggle_bt.configure(command=lambda:t_menu(dc))
        frame1.pack(side=ct.LEFT,fill="both",expand=True)
    bts = []
    color = "#2E4750"
    hv_color= "#303841"
    active_color = "#F05454"
    def menu_item(name,command):
        def comm():
            command()
            print("jere")
            set_a(len(bts),bt)
        
        bt = ct.CTkButton(tg_menu,text=name,fg_color=color,hover_color=hv_color)
        if name == "Main":
            bt.configure(fg_color=active_color) 
        bt.configure(command=comm)
        bt.pack(side=ct.TOP,padx=10,fill="x",pady=(20, 0))
        bts.append(bt)

    def set_a(i,bot):
        bot.configure(fg_color=active_color)
        print(i)
        for bt in bts:
            if bt != bot:
                bt.configure(fg_color=color)

    size = 150
    tg_menu = ct.CTkFrame(main_frame,width=size)
    tg_menu.pack(befor=frame1, side=ct.LEFT,anchor="w",fill="y")
    menu_item("Main",lambda:dc.change_to_main_screen())
    menu_item("Movies",lambda:dc.change_to_setting())
    menu_item("Close",close_app)

    toggle_bt.configure(text="Y")
    toggle_bt.configure(command=colaps_menu)
def close_app():
   root.destroy()


frame1 = ct.CTkFrame(main_frame)
frame1.pack(fill="both",expand=True)
# frame1.configure(height=50)



dc = DynamicContentFrame(frame1)
dc.pack(fill="both",expand=True)

dc.change_to_main_screen()



toggle_bt = ct.CTkButton(frame,text="X",command=lambda:t_menu(dc))
toggle_bt.pack(side=ct.LEFT,padx=20)



root.mainloop()