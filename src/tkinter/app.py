import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('NoteMind')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.sidebar = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky='nsew')

        self.entry = customtkinter.CTkEntry(
            self, 
            font=('Arial', 16),
            ipady=16
        )
        self.entry.grid(row=1, column=1, padx=16, pady=32, sticky='nsew')

        self.message_box = customtkinter.CTkFrame(self, fg_color='transparent', corner_radius=0)
        self.message_box.grid(row=0, column=1, sticky='nsew')
        self.message_box.columnconfigure(0, weight=1)
        
        self.messages = [
            'hello',
            'hello how are you',
            'Im good and you?',
            'Im good too'
        ]
        for i, message in enumerate(self.messages):
            label = customtkinter.CTkLabel(
                self.message_box, 
                fg_color='gray',
                text=message, 
                text_color='black',
                font=('Arial', 16),
                corner_radius=8
            )
            label.grid(row=i, column=0, ipadx=16, ipady=16, padx=16, pady=16, sticky='nsew')

if __name__ == '__main__':
    app = App()
    app.mainloop()
    

