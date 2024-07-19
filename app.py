import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# connecting to database
Database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="hotel",
)

Cursor = Database.cursor()

def insert_guest():
    g_id = guest_id_entry.get()
    name = guest_name_entry.get()
    lastname = guest_lastname_entry.get()
    nationality = guest_nationality_entry.get()
    phone = guest_phone_entry.get()
    email = guest_email_entry.get()

    if not phone:
        messagebox.showerror("Error", "Guest phone number is required!")
        return
    if not name:
        messagebox.showerror("Error", "Guest name is required!")
        return
    if not lastname:
        messagebox.showerror("Error", "Guest lastname is required!")
        return

    try:
        #inserting guest information
        query_guest = "INSERT INTO guest (guest_id, guest_name, guest_lastname, guest_nationality) VALUES (%s, %s, %s, %s)"
        values_guest = (g_id, name, lastname, nationality)
        Cursor.execute(query_guest, values_guest)
        Database.commit()

        query_contact = "INSERT INTO guest_contactinfo (guest_id, guest_phonenumber, guest_email) VALUES (%s, %s, %s)"
        values_contact = (g_id, phone, email)
        Cursor.execute(query_contact, values_contact)
        Database.commit()

        messagebox.showinfo("Success", "Guest inserted successfully!")
        load_guests()

        # deleting entries
        guest_id_entry.delete(0, tk.END)
        guest_name_entry.delete(0, tk.END)
        guest_lastname_entry.delete(0, tk.END)
        guest_nationality_entry.delete(0, tk.END)
        guest_phone_entry.delete(0, tk.END)
        guest_email_entry.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        Database.rollback()


def insert_reservation():
    reservation_id = reservation_id_entry.get()
    checkin_date = checkin_date_entry.get()
    checkout_date = checkout_date_entry.get()
    personnel_id = personnel_id_entry.get()
    price = reservation_price_entry.get()
    g_id = reservation_guest_id_entry.get()

    if not reservation_id:
        messagebox.showerror("Error", "Reservation id is required!")
        return
    if not checkin_date:
        messagebox.showerror("Error", "Check-in date is required!")
        return
    if not checkout_date:
        messagebox.showerror("Error", "Check-out date is required!")
        return

    try:
        # checking if the guest exists
        Cursor.execute("SELECT * FROM guest WHERE guest_id = %s", (g_id,))
        guest = Cursor.fetchone()
        if not guest:
            messagebox.showerror("Error", "Guest ID does not exist!")
            return

        #inserting guest informations
        query_reservation = "INSERT INTO reservation (reservation_id, reservation_startday, reservation_endday, reservation_price, guest_id, personnel_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values_reservation = (reservation_id, checkin_date, checkout_date, price, g_id, personnel_id)
        Cursor.execute(query_reservation, values_reservation)
        Database.commit()

        messagebox.showinfo("Success", "Reservation inserted successfully!")
        load_reservations()

        # deleting entries
        reservation_id_entry.delete(0, tk.END)
        checkin_date_entry.delete(0, tk.END)
        checkout_date_entry.delete(0, tk.END)
        personnel_id_entry.delete(0, tk.END)
        reservation_price_entry.delete(0, tk.END)
        reservation_guest_id_entry.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        Database.rollback()


def insert_office_personnel():
    p_id = personnel_id_entry.get()
    register_date = reg_date_entry.get()
    register_time = reg_time_entry.get()

    if not p_id:
        messagebox.showerror("Error", "Personnel ID number is required!")
        return
    if not register_date:
        messagebox.showerror("Error", "Register Date is required!")
        return
    if not register_time:
        messagebox.showerror("Error", "Register Time is required!")
        return

    try:
        query = "INSERT INTO office_personnel (personnel_id, reg_date, reg_time) VALUES (%s, %s, %s)"
        values = (p_id, register_date, register_time)
        Cursor.execute(query, values)
        Database.commit()

        messagebox.showinfo("Success", "Personnel inserted successfully!")
        clear_office_personnel_entries()
        load_office_personnel()  # inserting the new data in personnel treeview

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        Database.rollback()


def delete_guest_by_id(g_id):
    try:
        query = "DELETE FROM guest WHERE guest_id = %s"
        Cursor.execute(query, (g_id,))
        Database.commit()

        query = "DELETE FROM guest_contactinfo WHERE guest_id = %s"
        Cursor.execute(query, (g_id,))
        Database.commit()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        Database.rollback()


def delete_guest():
    g_id = guest_id_entry.get()

    if not g_id :
        messagebox.showerror("Error", "Guest ID is required!")
        return

    try:
        query = "DELETE FROM guest WHERE guest_id = %s"
        Cursor.execute(query, (g_id,))
        Database.commit()

        query = "DELETE FROM guest_contactinfo WHERE guest_id = %s"
        Cursor.execute(query, (g_id,))
        Database.commit()

        messagebox.showinfo("Success", "Guest deleted successfully!")
        clear_guest_entries()
        load_guests()  #loading changed data after deleting in guest treeview
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        Database.rollback()


def update_guest():
    g_id = guest_id_entry.get()
    name = guest_name_entry.get()
    lastname = guest_lastname_entry.get()
    nationality = guest_nationality_entry.get()
    phone = guest_phone_entry.get()
    email = guest_email_entry.get()

    if not phone:  
        messagebox.showerror("Error", "Guest phone number is required!")
        return

    try:
        query = "UPDATE guest SET guest_name = %s, guest_lastname = %s, guest_nationality = %s WHERE guest_id = %s"
        values = (name, lastname, nationality, g_id)
        Cursor.execute(query, values)
        Database.commit()

        query = "UPDATE guest_contactinfo SET guest_phonenumber = %s, guest_email = %s WHERE guest_id = %s"
        values = (phone, email, g_id)
        Cursor.execute(query, values)
        Database.commit()

        messagebox.showinfo("Success", "Guest updated successfully!")
        clear_guest_entries()
        load_guests()  #loading data after updating guest in treeview
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        Database.rollback()


def clear_guest_entries():
    guest_id_entry.delete(0, tk.END)
    guest_name_entry.delete(0, tk.END)
    guest_lastname_entry.delete(0, tk.END)
    guest_nationality_entry.delete(0, tk.END)
    guest_phone_entry.delete(0, tk.END)
    guest_email_entry.delete(0, tk.END)


def load_guests():
    for row in guest_tree.get_children():
        guest_tree.delete(row)
    query = """
    SELECT g.guest_id, g.guest_name, g.guest_lastname, g.guest_nationality, gc.guest_phonenumber, gc.guest_email 
    FROM guest g 
    JOIN guest_contactinfo gc ON g.guest_id = gc.guest_id
    """
    Cursor.execute(query)
    rows = Cursor.fetchall()
    for row in rows:
        guest_tree.insert("", tk.END, values=row)


def update_room_type():
    room_id = room_id_entry.get()
    room_status = room_status_entry.get()
    if not room_id :
        messagebox.showerror("Error", "Room ID is required!")
        return
    try:
        query = "UPDATE room SET room_status = %s WHERE room_id = %s"
        values = (room_status, room_id)
        Cursor.execute(query, values)
        Database.commit()

        messagebox.showinfo("Success", "Room status updated successfully!")
        clear_room_entries()
        load_rooms()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        Database.rollback()


def clear_room_entries():
    room_id_entry.delete(0, tk.END)
    room_status_entry.delete(0, tk.END)


def load_rooms():
    for row in room_tree.get_children():
        room_tree.delete(row)
    query = """
    SELECT r.room_id, r.room_type, r.room_status, g.guest_name, g.guest_lastname
    FROM room r
    LEFT JOIN reservation res ON r.reservation_id = res.reservation_id
    LEFT JOIN guest g ON res.guest_id = g.guest_id;
    """
    Cursor.execute(query)
    rows = Cursor.fetchall()
    for row in rows:
        room_tree.insert("", tk.END, values=row)

def load_reservations():
    for row in reservation_tree.get_children():
        reservation_tree.delete(row)
    query = """
    SELECT r.reservation_id, r.reservation_startday, r.reservation_endday, r.reservation_price 
    FROM reservation r
    """
    Cursor.execute(query)
    rows = Cursor.fetchall()
    for row in rows:
        reservation_tree.insert("", tk.END, values=row)



def load_office_personnel():
    for row in personnel_tree.get_children():
        personnel_tree.delete(row)
    query = """
    SELECT op.personnel_id, p.personnel_name, p.personnel_lastname, op.reg_date, op.reg_time
    FROM offiice_personnel op
    JOIN personnel p ON op.personnel_id = p.personnel_id
    """
    Cursor.execute(query)
    rows = Cursor.fetchall()
    for row in rows:
        personnel_tree.insert("", tk.END, values=row)


def clear_office_personnel_entries():
    personnel_id_entry.delete(0, tk.END)
    reg_date_entry.delete(0, tk.END)
    reg_time_entry.delete(0, tk.END)


# creating gui
root = tk.Tk()
root.title("Hotel Management System")

tab_control = ttk.Notebook(root)

guest_tab = ttk.Frame(tab_control)
tab_control.add(guest_tab, text="Guests")

room_tab = ttk.Frame(tab_control)
tab_control.add(room_tab, text="Rooms")

personnel_tab = ttk.Frame(tab_control)
tab_control.add(personnel_tab, text="Office Personnel")

reservation_tab = ttk.Frame(tab_control)
tab_control.add(reservation_tab, text="Reservations")

# Guests tab
guest_id_label = tk.Label(guest_tab, text="Guest ID:")
guest_id_label.grid(row=0, column=0)
guest_id_entry = tk.Entry(guest_tab)
guest_id_entry.grid(row=0, column=1)

guest_name_label = tk.Label(guest_tab, text="Name:")
guest_name_label.grid(row=1, column=0)
guest_name_entry = tk.Entry(guest_tab)
guest_name_entry.grid(row=1, column=1)

guest_lastname_label = tk.Label(guest_tab, text="Lastname:")
guest_lastname_label.grid(row=2, column=0)
guest_lastname_entry = tk.Entry(guest_tab)
guest_lastname_entry.grid(row=2, column=1)

guest_nationality_label = tk.Label(guest_tab, text="Nationality:")
guest_nationality_label.grid(row=3, column=0)
guest_nationality_entry = tk.Entry(guest_tab)
guest_nationality_entry.grid(row=3, column=1)

guest_phone_label = tk.Label(guest_tab, text="Phone:")
guest_phone_label.grid(row=4, column=0)
guest_phone_entry = tk.Entry(guest_tab)
guest_phone_entry.grid(row=4, column=1)

guest_email_label = tk.Label(guest_tab, text="Email:")
guest_email_label.grid(row=5, column=0)
guest_email_entry = tk.Entry(guest_tab)
guest_email_entry.grid(row=5, column=1)

insert_guest_button = tk.Button(guest_tab, text="Insert Guest", command=insert_guest)
insert_guest_button.grid(row=6, column=0)

update_guest_button = tk.Button(guest_tab, text="Update Guest", command=update_guest)
update_guest_button.grid(row=6, column=1)

delete_guest_button = tk.Button(guest_tab, text="Delete Guest", command=delete_guest)
delete_guest_button.grid(row=6, column=2)

guest_tree = ttk.Treeview(guest_tab, columns=("ID", "Name", "Lastname", "Nationality", "Phone", "Email"), show="headings")
guest_tree.grid(row=7, column=0, columnspan=3)

for col in guest_tree["columns"]:
    guest_tree.heading(col, text=col)

load_guests()

#  Rooms tab
room_id_label = tk.Label(room_tab, text="Room ID:")
room_id_label.grid(row=0, column=0)
room_id_entry = tk.Entry(room_tab)
room_id_entry.grid(row=0, column=1)

room_status_label = tk.Label(room_tab, text="Room Status:")
room_status_label.grid(row=1, column=0)
room_status_entry = tk.Entry(room_tab)
room_status_entry.grid(row=1, column=1)

update_room_button = tk.Button(room_tab, text="Update Room Type", command=update_room_type)
update_room_button.grid(row=2, column=0, columnspan=2)

room_tree = ttk.Treeview(room_tab, columns=("Room ID", "Type", "Status", "Guest Name", "Guest Lastname"), show="headings")
room_tree.grid(row=3, column=0, columnspan=2)

for col in room_tree["columns"]:
    room_tree.heading(col, text=col)

load_rooms()

personnel_id_label = tk.Label(personnel_tab, text="Personnel ID:")
personnel_id_label.grid(row=0, column=0)
personnel_id_entry = tk.Entry(personnel_tab)
personnel_id_entry.grid(row=0, column=1)

reg_date_label = tk.Label(personnel_tab, text="Reg Date:")
reg_date_label.grid(row=1, column=0)
reg_date_entry = tk.Entry(personnel_tab)
reg_date_entry.grid(row=1, column=1)

reg_time_label = tk.Label(personnel_tab, text="Reg Time:")
reg_time_label.grid(row=2, column=0)
reg_time_entry = tk.Entry(personnel_tab)
reg_time_entry.grid(row=2, column=1)

insert_personnel_button = tk.Button(personnel_tab, text="Insert Personnel", command=insert_office_personnel)
insert_personnel_button.grid(row=3, column=0, columnspan=2)

personnel_tree = ttk.Treeview(personnel_tab, columns=("Personnel ID", "Name", "Lastname", "Reg Date", "Reg Time"), show="headings")
personnel_tree.grid(row=4, column=0, columnspan=2)

for col in personnel_tree["columns"]:
    personnel_tree.heading(col, text=col)

tab_control.pack(expand=1, fill="both")

# loading data
load_office_personnel()


# Reservations tab
reservation_id_label = tk.Label(reservation_tab, text="Reservation ID:")
reservation_id_label.grid(row=0, column=0)
reservation_id_entry = tk.Entry(reservation_tab)
reservation_id_entry.grid(row=0, column=1)

checkin_date_label = tk.Label(reservation_tab, text="Check-in Date:")
checkin_date_label.grid(row=1, column=0)
checkin_date_entry = tk.Entry(reservation_tab)
checkin_date_entry.grid(row=1, column=1)

checkout_date_label = tk.Label(reservation_tab, text="Check-out Date:")
checkout_date_label.grid(row=2, column=0)
checkout_date_entry = tk.Entry(reservation_tab)
checkout_date_entry.grid(row=2, column=1)

reservation_price_label = tk.Label(reservation_tab, text="Price:")
reservation_price_label.grid(row=3, column=0)
reservation_price_entry = tk.Entry(reservation_tab)
reservation_price_entry.grid(row=3, column=1)



personnel_id_label = tk.Label(reservation_tab, text="Personnel ID:")
personnel_id_label.grid(row=4, column=0)
personnel_id_entry = tk.Entry(reservation_tab)
personnel_id_entry.grid(row=4, column=1)

reservation_guest_id_label = tk.Label(reservation_tab, text="Guest ID:")
reservation_guest_id_label.grid(row=5, column=0)
reservation_guest_id_entry = tk.Entry(reservation_tab)
reservation_guest_id_entry.grid(row=5, column=1)

insert_reservation_button = tk.Button(reservation_tab, text="Insert Reservation", command=insert_reservation)
insert_reservation_button.grid(row=6, column=0, columnspan=2)

reservation_tree = ttk.Treeview(reservation_tab, columns=("Reservation ID", "check in date", "check out date", "price"), show="headings")
personnel_tree.grid(row=7, column=0, columnspan=2)

for col in personnel_tree["columns"]:
    personnel_tree.heading(col, text=col)


tab_control.pack(expand=1, fill="both")


root.mainloop()

Cursor.close()
Database.close()