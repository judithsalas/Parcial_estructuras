
from Roomtype import HotelRoomType

class Room:
    def __init__(self, room_type, room_number, is_occupied, room_price):
        if not isinstance(room_type, HotelRoomType):
            raise ValueError("Invalid room type. Must be a 'RoomType' enum value.")
        if not isinstance(room_number, int):
            raise ValueError("Room number must be an integer.")
        if not isinstance(is_occupied, bool):
            raise ValueError("Is occupied must be a boolean.")
        if not isinstance(room_price, (int, float)) or room_price < 0:
            raise ValueError("Room price must be a non-negative number.")
        
        self._room_type = room_type
        self._room_number = room_number
        self._is_occupied = is_occupied
        self._room_price = room_price

    # Getters
    def get_room_type(self):
        return self._room_type

    def get_room_number(self):
        return self._room_number

    def is_occupied(self):
        return self._is_occupied

    def get_room_price(self):
        return self._room_price
    
    # Setters
    def set_room_type(self, room_type):
        if not isinstance(room_type, HotelRoomType):
            raise ValueError("Invalid room type. Must be a 'RoomType' enum value.")
        self._room_type = room_type

    def set_room_number(self, room_number):
        if not isinstance(room_number, int):
            raise ValueError("Room number must be an integer.")
        self._room_number = room_number

    def set_is_occupied(self, is_occupied):
        if not isinstance(is_occupied, bool):
            raise ValueError("Is occupied must be a boolean.")
        self._is_occupied = is_occupied

    def set_room_price(self, room_price):
        if not isinstance(room_price, (int, float)) or room_price < 0:
            raise ValueError("Room price must be a non-negative number.")
        self._room_price = room_price
    
    # Métodos relacionados con el estado de ocupación de la habtación
    def check_in(self):
        if self._is_occupied:
            raise Exception("The room is already occupied.")
        self._is_occupied = True

    def check_out(self):
        if not self._is_occupied:
            raise Exception("The room is not currently occupied.")
        self._is_occupied = False



def main():
    #TESTING 
    print("=================================================================")
    print("Test Case 1: Create a Room.")
    print("=================================================================")
    room1 = Room("Doble", 101, "Desocupada", 150)

    if room1.get_room_type() == "Doble":
        print("Test PASS. The parameter room_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_number() == 101:
        print("Test PASS. The parameter room_number has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_state() == "Desocupada":
        print("Test PASS. The parameter room_state has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_price() == 150:
        print("Test PASS. The parameter room_price has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================")
    print("Test Case 2: Check-in a Room.")
    print("=================================================================")
    room2 = Room("Suite", 102, "Desocupada", 300)
    check_in_result = room2.check_in()

    if check_in_result == "Check-in realizado con éxito." and room2.is_occupied():
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")


    print("=================================================================")
    print("Test Case 3: Check-out a Room.")
    print("=================================================================")
    # Assuming room2 was checked in from the previous test
    check_out_result = room2.check_out()

    if check_out_result == "Check-out realizado con éxito." and not room2.is_occupied():
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")


    print("=================================================================")
    print("Test Case 4: Attempt Check-in on an Occupied Room.")
    print("=================================================================")
    room3 = Room("Individual", 103, "Ocupada", 100)
    check_in_result = room3.check_in()

    if check_in_result == "La habitación ya está ocupada.":
        print("Test PASS. Attempted check-in on an occupied room handled correctly.")
    else:
        print("Test FAIL. Check the method check_in() for occupied rooms.")


    print("=================================================================")
    print("Test Case 5: Attempt Check-out on a Vacant Room.")
    print("=================================================================")
    # Assuming room3 was made vacant from the previous operation or is initially vacant
    room4 = Room("Doble", 104, "Desocupada", 200)
    check_out_result = room4.check_out()

    if check_out_result == "La habitación ya está desocupada.":
        print("Test PASS. Attempted check-out on a vacant room handled correctly.")
    else:
        print("Test FAIL. Check the method check_out() for vacant rooms.")


# Testing
try:
    room101 = Room(HotelRoomType.DOUBLE, 101, False, 150.00)
    print("Room 101 created:", room101.get_room_type().value, "at $", room101.get_room_price())
    room101.check_in()
    print("Check-in status:", room101.is_occupied())
    room101.check_out()
    print("Check-out status:", room101.is_occupied())
except Exception as e:
    print("Error:", e)

if __name__ == "__main__":
    main()