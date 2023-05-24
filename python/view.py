import customtkinter as ctk
import sqlite3
from tkinter import ttk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


class FourChoiceFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.radio_var = ctk.IntVar()

        self.titrefont = ctk.CTkFont(family="Arial", size=12, weight="bold")
        self.titre = ctk.CTkLabel(self, text="Choisissez une table", font=self.titrefont)  # noqa: E501
        self.titre.pack(pady=1)

        table_choices = {
            1: "videos",
            2: "commentaires",
            3: "chaines",
            4: "n_com"
        }

        for choice, table_name in table_choices.items():
            radio_button = ctk.CTkRadioButton(self, text=table_name, variable=self.radio_var, value=choice)  # noqa: E501
            radio_button.pack(anchor="w")


class App(ctk.CTk):
    TABLES= {
        1: ("Videos", ["id", "titre", "lien", "description", "likes", "dislikes", "id_chaine", "views", "timestamp"]),  # noqa: E501
        2: ("Commentaires", ["id", "contenu", "id_video", "timestamp"]),
        3: ("Chaines", ["id", "pseudo", "abonnes", "bio", "timestamp", "email"]),
        4: ("N_com", ["id_video", "id_commentaire"])
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
        if selected_choice in self.TABLES:
            table_name, columns = self.TABLES[selected_choice]

            # Connect to the SQLite database
            conn = sqlite3.connect('db/tvideos.db')
            cursor = conn.cursor()

            # Query the selected table
            cursor.execute(f"SELECT {', '.join(columns)} FROM {table_name}")
            rows = cursor.fetchall()

            # Create a new sub-window to display the results
            sub_window = ctk.CTk()
            sub_window.title(table_name)
            sub_window.geometry("700x500")

            # Create a Treeview to display the results
            tree = ttk.Treeview(sub_window, columns=columns, show="headings")
            for col in columns:
                tree.heading(col, text=col)
            for row in rows:
                tree.insert("", "end", values=row)
            tree.pack(fill='both', expand=True)

            # Close the database connection
            cursor.close()
            conn.close()

            # Run the sub-window in a loop
            sub_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()