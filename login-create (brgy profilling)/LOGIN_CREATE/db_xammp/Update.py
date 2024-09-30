def login_action():
    username = entry_1.get()  # Get username from Tkinter Entry widget
    password = entry_2.get()  # Get password from Tkinter Entry widget

    # Check if fields are empty
    if not (username and password):
        tk.messagebox.showwarning("Warning!", "Invalid Username or Password")
        return

    connection = db_xammp.db_manager.create_connection(self=db_xammp.db_manager)
    if connection:
        try:
            cursor = connection.cursor()
            select_query = "SELECT * FROM tbl_adminlogin WHERE Username=%s AND Password=%s;"
            user_input = (username, password)

            cursor.execute(select_query, user_input)
            result = cursor.fetchone()

            # If no result is found
            if result is None:
                tk.messagebox.showwarning("Warning!", "Invalid Username or Password")
            else:
                tk.messagebox.showinfo("Success", f"Login Successful!\nUsername: {username}")

        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

        finally:
            db_xammp.db_manager.close_connection(connection, cursor)
    else:
        tk.messagebox.showerror("Error", "Could not connect to the database.")