# Hotel_reservation
## Hotel Management System

This project is a Hotel Management System built using Python with a graphical user interface (GUI) created with Tkinter. It connects to a MySQL database to manage various aspects of hotel operations including guest information, room status, reservations, and office personnel.

### Features

1. **Guest Management**
    - Add new guests with details such as ID, name, lastname, nationality, phone, and email.
    - Update existing guest details.
    - Delete guests from the database.
    - View a list of all guests with their respective details.

2. **Room Management**
    - Update room status (e.g., occupied, vacant).
    - View a list of all rooms, including room ID, type, status, and guest details if applicable.

3. **Reservation Management**
    - Add new reservations with details such as reservation ID, check-in and check-out dates, price, guest ID, and personnel ID.
    - View a list of all reservations.

4. **Office Personnel Management**
    - Add new office personnel with details such as personnel ID, registration date, and registration time.
    - View a list of all office personnel with their respective details.

### How to Use

1. **Database Setup**
    - Ensure you have MySQL installed and running.

2. **Running the Application**
    - Install the required Python libraries:
      ```bash
      pip install mysql-connector-python
      ```
    - Run the `Hotel_Management.py` script:
      ```bash
      python Hotel_Management.py
      ```
    - The GUI will launch, allowing you to interact with the hotel management system.

### Code Overview

- **Database Connection**: Establishes a connection to the MySQL database.
- **GUI Creation**: Uses Tkinter to create a multi-tabbed interface for managing different aspects of the hotel.
- **Functions**:
  - `insert_guest()`: Inserts a new guest into the database.
  - `insert_reservation()`: Inserts a new reservation into the database.
  - `insert_office_personnel()`: Inserts a new office personnel record into the database.
  - `delete_guest()`: Deletes a guest from the database.
  - `update_guest()`: Updates a guest's details in the database.
  - `update_room_type()`: Updates the status of a room.
  - `clear_guest_entries()`, `clear_room_entries()`, `clear_office_personnel_entries()`: Clears input fields.
  - `load_guests()`, `load_rooms()`, `load_reservations()`, `load_office_personnel()`: Loads data from the database into the respective tree views.
