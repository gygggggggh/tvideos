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

        self.submit_button = customtkinter.CTkButton(self, text="Submit", command=self.submit)# noqa: E501
        self.submit_button.pack(pady=10)

        

    
    def submit(self):
        selected_choice = self.choice_frame.radio_var.get()
        if selected_choice == 1:
            # Connect to the SQLite database
            conn = sqlite3.connect('tvideos.db')
            cursor = conn.cursor()

            # Query the videos table
            cursor.execute("SELECT id , titre, lien, description, like, dislike, id_chaine, vue, timestamp FROM videos")  # noqa: E501
            rows = cursor.fetchall()

            # Create a new sub-window to display the results
            sub_window = customtkinter.CTk()
            sub_window.title("Videos Table")
            sub_window.geometry("700x500")

            # Create a Treeview to display the results
            columns = ("id", "titre", "lien", "description", "like", "dislike", "id_chaine", "vue", "timestamp")# noqa: E501
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
        elif selected_choice == 2:
            # Connect to the SQLite database
            conn = sqlite3.connect('tvideos.db')
            cursor = conn.cursor()

            # Query the commentaires table
            cursor.execute("SELECT id, contenue, id_video, timestamp FROM commentaires")
            rows = cursor.fetchall()

            # Create a new sub-window to display the results
            sub_window = customtkinter.CTk()
            sub_window.title("Commentaires Table")
            sub_window.geometry("700x500")

            # Create a Treeview to display the results
            columns = ("id", "commentaire", "id_video", "timestamp")
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
        elif selected_choice == 3:
            # Connect to the SQLite database
            conn = sqlite3.connect('tvideos.db')
            cursor = conn.cursor()

            # Query the chaine table
            cursor.execute("SELECT id, pseudo, abonnes,bio,timestamp,email FROM chaines")# noqa: E501
            rows = cursor.fetchall()

            # Create a new sub-window to display the results
            sub_window = customtkinter.CTk()
            sub_window.title("Chaine Table")
            sub_window.geometry("700x500")

            # Create a Treeview to display the results
            columns = ("id", "pseudo", "abonnes", "bio", "timestamp", "email")
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
        elif selected_choice == 4:
            # Connect to the SQLite database
            conn = sqlite3.connect('tvideos.db')
            cursor = conn.cursor()

            # Query the n_com table
            cursor.execute("SELECT id_video, id_commentaire FROM n_com")
            rows = cursor.fetchall()

            # Create a new sub-window to display the results
            sub_window = customtkinter.CTk()
            sub_window.title("N_com Table")

            # Create a Treeview to display the results
            columns = ("id_videos", "id_commentaires")
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
        else:
            pass






app = App()
app.mainloop()