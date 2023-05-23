import customtkinter
import sqlite3
from tkinter import ttk

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

class fourChoiceFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.radio_var = customtkinter.IntVar()

        self.titrefont = customtkinter.CTkFont(family="Arial", size=12, weight="bold")
        self.titre = customtkinter.CTkLabel(self, text="Choisissez une table", font=self.titrefont)   # noqa: E501
        self.titre.pack(pady=1)
        
        self.radio_1 = customtkinter.CTkRadioButton(self, text="videos", variable=self.radio_var, value=1)# noqa: E501
        self.radio_1.pack(anchor="w")
        self.radio_2 = customtkinter.CTkRadioButton(self, text="commentaires", variable=self.radio_var, value=2)# noqa: E501
        self.radio_2.pack(anchor="w")
        self.radio_3 = customtkinter.CTkRadioButton(self, text="chaines", variable=self.radio_var, value=3)# noqa: E501
        self.radio_3.pack(anchor="w")
        self.radio_4 = customtkinter.CTkRadioButton(self, text="n_com", variable=self.radio_var, value=4)# noqa: E501
        self.radio_4.pack(anchor="w")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Tvideos")
        self.geometry("300x200")

        self.choice_frame = fourChoiceFrame(self)
        self.choice_frame.pack(pady=20)

        self.submit_button = customtkinter.CTkButton(self, text="Submit", command=self.choices)# noqa: E501
        self.submit_button.pack(pady=10)


    def choices(self):
        selected_choice = self.choice_frame.radio_var.get()
        match selected_choice:
            case 1:
                # create sub window
                sub_window = customtkinter.CTk()
                sub_window.title("Videos Table")
                sub_window.geometry("250x300")

                #create label for each column
                labels = [ "titre", "lien", "description", "likes", "dislikes", "id_chaine", "vue", "timestamp"]
                label_widgets = []

                for i, label_text in enumerate(labels):
                    label = customtkinter.CTkLabel(sub_window, text=label_text)
                    label.grid(row=i, column=0)
                    label_widgets.append(label)
    
                # create entry for each column
                entries = []
                for i in range(len(labels)):
                    entry = customtkinter.CTkEntry(sub_window)
                    entry.grid(row=i, column=1)
                    entries.append(entry)

                data= [entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get(),entries[5].get(),entries[6].get(),entries[7].get()]# noqa: E501

                # create submit button
                sumbit_button = customtkinter.CTkButton(sub_window, text="Submit" , command=lambda: self.submit(1,data))# noqa: E501
                sumbit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)
                

                # run the mainloop
                sub_window.mainloop()

            case 2:
                # create sub window
                sub_window = customtkinter.CTk()
                sub_window.title("Commentaires Table")
                sub_window.geometry("250x300")

                #create label for each column
                labels = ["contenue","likes","id_chaine","id_video","timestamp"]
                label_widgets = []

                for i, label_text in enumerate(labels):
                    label = customtkinter.CTkLabel(sub_window, text=label_text)
                    label.grid(row=i, column=0)
                    label_widgets.append(label)

                # create entry for each column
                entries = []
                for i in range(len(labels)):
                    entry = customtkinter.CTkEntry(sub_window)
                    entry.grid(row=i, column=1)
                    entries.append(entry)

                data= [entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get()]# noqa: E501

                # create submit button
                sumbit_button = customtkinter.CTkButton(sub_window, text="Submit" , command=lambda: self.submit(2,data))# noqa: E501
                sumbit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

                # run the mainloop
                sub_window.mainloop()

            case 3:
                # create sub window
                sub_window = customtkinter.CTk()    
                sub_window.title("Chaines Table")
                sub_window.geometry("250x300")

                #create label for each column
                labels = ["pseudo","abonnes","bio","timestamp","email"]
                label_widgets = []

                for i, label_text in enumerate(labels):
                    label = customtkinter.CTkLabel(sub_window, text=label_text)
                    label.grid(row=i, column=0)
                    label_widgets.append(label)

                # create entry for each column
                entries = []
                for i in range(len(labels)):
                    entry = customtkinter.CTkEntry(sub_window)
                    entry.grid(row=i, column=1)
                    entries.append(entry)

                data= [entries[0].get(),entries[1].get(),entries[2].get(),entries[3].get(),entries[4].get()]# noqa: E501

                # create submit button
                sumbit_button = customtkinter.CTkButton(sub_window, text="Submit" , command=lambda: self.submit(3,data))# noqa: E501
                sumbit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

                # run the mainloop
                sub_window.mainloop()


            case 4:
                # create sub window
                sub_window = customtkinter.CTk()
                sub_window.title("N_com Table")
                sub_window.geometry("250x300")

                #create label for each column
                labels = ["id_video","id_commentaire"]
                label_widgets = []

                for i, label_text in enumerate(labels):
                    label = customtkinter.CTkLabel(sub_window, text=label_text)
                    label.grid(row=i, column=0)
                    label_widgets.append(label)

                # create entry for each column
                entries = []
                for i in range(len(labels)):
                    entry = customtkinter.CTkEntry(sub_window)
                    entry.grid(row=i, column=1)
                    entries.append(entry)

                data = [entries[0].get(),entries[1].get()]# noqa: E501
                # create submit button
                sumbit_button = customtkinter.CTkButton(sub_window, text="Submit" , command=lambda: self.submit(4,data))# noqa: E501
                sumbit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

                # run the mainloop
                sub_window.mainloop()

            case _:
                print("error")


    def submit(self, n, data):
        # connect to the database
        conn = sqlite3.connect("tvideos.db")  
        c = conn.cursor()
        if n == 1:
            # Submitting to the 'videos' table
            print(data)
            c.execute("INSERT INTO videos (titre, lien, description, like, dislike, id_chaine, vue, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",data)
            conn.commit()
            print("Data submitted to the 'videos' table.")
            conn.close()
        
        elif n == 2:
            # Submitting to the 'commentaires' table
            c.execute("INSERT INTO commentaires (id, contenue, likes, id_chaine, id_video, timestamp) VALUES (?, ?, ?, ?, ?)",data)
            conn.commit()
            print("Data submitted to the 'commentaires' table.")
            conn.close()

        elif n == 3:
            # Submitting to the 'chaines' table
            c.execute("INSERT INTO chaines (id, pseudo, abonnes, bio, timestamp, email) VALUES (?, ?, ?, ?, ?)",data)
            conn.commit()
            print("Data submitted to the 'chaines' table.")
            conn.close()

        elif n == 4:
            # Submitting to the 'n_com' table
            c.execute("INSERT INTO n_com (id_video, id_commentaire) VALUES (?, ?)",data)
            conn.commit()
            print("Data submitted to the 'n_com' table.")
            conn.close()
        
        else:
            print("Invalid choice.")
        conn.close()
        
        


        def get(self,entry_widgets):
            data = []
            for entry in entry_widgets:
                data.append(entry.get())
            print(data)
            return data
        
    



if __name__ == "__main__":
    app = App()
    app.mainloop()


        
