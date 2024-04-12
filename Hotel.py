
class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        self.employees = []
        self.services = []
        self.reservations = {}

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room_number):
        self.rooms = [room for room in self.rooms if room.room_number != room_number]

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def add_service(self, service):
        if service not in self.services:
            self.services.append(service)

    def book_room(self, room_number, guest_name, stay_length):
        self.reservations[room_number] = (guest_name, stay_length)

    def check_in(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_occupied():
                room.check_in()
                return f"Check-in successful for room {room_number}"
        return "Room is already occupied or does not exist."

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.is_occupied():
                room.check_out()
                guest_name, stay_length = self.reservations.pop(room_number, (None, None))
                if guest_name:
                    cost = room.room_price * stay_length
                    return f"Check-out successful for {guest_name}. Total cost: ${cost}"
        return "Room is not occupied or does not exist."

    def list_rooms(self):
        return "\n".join(str(room) for room in self.rooms)

    def list_employees(self):
        return "\n".join(str(emp) for emp in self.employees)



#Testing

def main():
    hotel = Hotel("Hotel Paradise", "123 Paradise Road")

    while True:
        print("\nHotel Management System")
        print("1. Add room")
        print("2. Remove room")
        print("3. Add employee")
        print("4. Remove employee")
        print("5. Add service")
        print("6. Book room")
        print("7. Check-in")
        print("8. Check-out")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add room 
            pass
        elif choice == "2":
            # Remove room 
            pass
        elif choice == "3":
            # Add employee
            pass
        elif choice == "4":
            # Remove employee
            pass
        elif choice == "5":
            # Add service 
            pass
        elif choice == "6":
            # Book room 
            pass
        elif choice == "7":
            # Check-in
            pass
        elif choice == "8":
            # Check-out 
            pass
        elif choice == "9":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()