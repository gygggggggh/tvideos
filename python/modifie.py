import sqlite3
import customtkinter as ctk


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


class FourChoiceFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.radio_var = ctk.IntVar()

        self.titrefont = ctk.CTkFont(family="Arial", size=12, weight="bold")
        self.titre = ctk.CTkLabel(self, text="Choisissez une table", font=self.titrefont)  # noqa: E501
        self.titre.pack(pady=1)

        choices = ["videos", "commentaires", "chaines"]
        for i, choice in enumerate(choices, start=1):
            radio_button = ctk.CTkRadioButton(self, text=choice, variable=self.radio_var, value=i)  # noqa: E501
            radio_button.pack(anchor="w")


class App(ctk.CTk):
    TABLES = {
        1: ("Videos", ["id", "titre", "lien", "description", "likes", "dislikes", "id_chaine", "views", "timestamp"]),  # noqa: E501
        2: ("Commentaires", ["id", "contenu", "id_video", "timestamp"]),
        3: ("Chaines", ["id", "pseudo", "abonnes", "bio", "timestamp", "email"]),
    }

    def __init__(self):
        super().__init__()

        self.title("Tvideos")
        self.geometry("300x300")

        self.choice_frame = FourChoiceFrame(self)
        self.choice_frame.pack(pady=20)

        self.label_id = ctk.CTkLabel(self, text="choose id of the table you want to modify")  # noqa: E501
        self.label_id.pack(pady=1)

        self.entry_id = ctk.CTkEntry(self)
        self.entry_id.insert(0, "1")
        self.entry_id.pack(pady=1)

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

    def submit(self):
        selected_choice = self.choice_frame.radio_var.get()
        if selected_choice in self.TABLES:
            table_name, columns = self.TABLES[selected_choice]

            # Connect to the SQLite database
            conn = sqlite3.connect('db/tvideos.db')
            cursor = conn.cursor()

            
            # Query the selected table
            cursor.execute(f"SELECT {', '.join(columns)} FROM {table_name} WHERE id={self.entry_id.get()}")  # noqa: E501
            row = cursor.fetchone()

            if row is not None:
                # Create a subwindow
                subwindow = ctk.CTk()
                subwindow.title(self.TABLES[selected_choice][0])
                subwindow.geometry("300x300")

                entries = []
                for i, label_text in enumerate(columns):
                    label = ctk.CTkLabel(subwindow, text=label_text)
                    label.grid(row=i, column=0)

                    entry = ctk.CTkEntry(subwindow)
                    entry.grid(row=i, column=1)
                    entry.insert(0, row[i])
                    entries.append(entry)

                def update_row():
                    values = [entry.get() for entry in entries]
                    update_query = f"UPDATE {table_name} SET {', '.join(f'{column}=?' for column in columns)} WHERE id={self.entry_id.get()}"  # noqa: E501
                    cursor.execute(update_query, values)
                    conn.commit()
                    subwindow.destroy()

                update_button = ctk.CTkButton(subwindow, text="Update", command=update_row)  # noqa: E501
                update_button.grid(row=len(columns), columnspan=2)

                # Main loop
                subwindow.mainloop()
            else:
                print("No matching record found.")

    
                
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
