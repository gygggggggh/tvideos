import sqlite3
import customtkinter as ctk


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


class FourChoiceFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.radio_var = ctk.IntVar()

        self.titrefont = ctk.CTkFont(family="Arial", size=12, weight="bold")
        self.titre = ctk.CTkLabel(self, text="Choisissez une table", font=self.titrefont) # noqa: E501
        self.titre.pack(pady=1)

        choices = ["videos", "commentaires", "chaines", "n_com"]
        for i, choice in enumerate(choices, start=1):
            radio_button = ctk.CTkRadioButton(self, text=choice, variable=self.radio_var, value=i)  # noqa: E501
            radio_button.pack(anchor="w")


class App(ctk.CTk):
    TABLES = {
        1: ("Videos", ["titre", "lien", "description", "like", "dislike", "id_chaine", "vue", "timestamp"]),  # noqa: E501
        2: ("Commentaires", ["contenue", "like", "id_chaine", "id_video", "timestamp"]),
        3: ("Chaines", ["pseudo", "abonnes", "description", "bio", "timestamp", "email"]),  # noqa: E501
        4: ("n_com", ["pseudo", "abonnes", "description", "bio", "timestamp", "email"])
    }

    def __init__(self):
        super().__init__()

        self.title("Tvideos")
        self.geometry("300x200")

        self.choice_frame = FourChoiceFrame(self)
        self.choice_frame.pack(pady=20)

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

    def submit(self):
        selected_choice = self.choice_frame.radio_var.get()
        table_name, column_names = self.TABLES[selected_choice]

        sub_window = ctk.CTk()
        sub_window.title(table_name)
        sub_window.geometry("250x300")

        labels = column_names
        entries = []
        for i, label_text in enumerate(labels):
            label = ctk.CTkLabel(sub_window, text=label_text)
            label.grid(row=i, column=0)

            entry = ctk.CTkEntry(sub_window)
            entry.grid(row=i, column=1)
            entries.append(entry)

        confirm_button = ctk.CTkButton(sub_window, text="Submit", command=lambda: self.insert_data(table_name, column_names, entries))  # noqa: E501
        confirm_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

        sub_window.mainloop()

    def insert_data(self, table_name, column_names, entries):
        data = [entry.get() for entry in entries]

        connection = sqlite3.connect("tvideos.db")
        cursor = connection.cursor()

        placeholders = ', '.join(['?'] * len(column_names))
        query = f"INSERT INTO `{table_name}` ({', '.join(column_names)}) VALUES ({placeholders})"  # noqa: E501

        cursor.execute(query, data)
        connection.commit()
        connection.close()


if __name__ == "__main__":
    app = App()
    app.mainloop()
