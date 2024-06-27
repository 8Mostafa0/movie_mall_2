import customtkinter as ct

# Assuming your theme file exists in the same directory
ct.set_appearance_mode("dark")
ct.set_default_color_theme("./theme.json")

content_list2 = [
  {"type": "button", "text": "Button 2", "command": lambda:print("1")},
  {"type": "label", "text": "This is content 2"},
]

content_list1 = [
  {"type": "button", "text": "Button 1", "command": lambda: DynamicContentFrame(root).set_content(content_list2)},
  {"type": "label", "text": "This is content 1"},
]

content_list2 = [
  {"type": "button", "text": "Button 2", "command": lambda:DynamicContentFrame(root).set_content(content_list1)},
  {"type": "label", "text": "This is content 2"},
]


root =  ct.CTk()
class DynamicContentFrame(ct.CTkFrame):
  def __init__(self, parent):
    super().__init__(parent)
    self.widgets = []

  def set_content(self, content_list):
    self.clear_widgets()

    for content in content_list:
      widget_class = content['type']  # Check for class (button or label)
      if widget_class == "button":  # Assuming button class is CTkButton
        button = ct.CTkButton(self, text=content['text'], command=content['command'])  # Create button with other attributes
        button.pack()
        self.widgets.append(button)
      elif widget_class == "label":  # Assuming label class is CTkLabel
        label = ct.CTkLabel(self, text=content['text'])
        label.pack()
        self.widgets.append(label)
      else:
        print(f"Invalid widget class: {widget_class}")

  def clear_widgets(self):
    """
    Removes all existing widgets from the frame.
    """
    for widget in self.widgets:
      widget.pack_forget()
      widget.destroy()
    self.widgets = []  # Empty the list of widgets

# Create the frame instance
content_frame = DynamicContentFrame(root)
content_frame.pack()  # Pack the frame on the main window

# Define example content lists for different scenarios


# Update the frame content with different content lists
content_frame.set_content(content_list1)

root.mainloop()
