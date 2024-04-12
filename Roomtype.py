from enum import Enum

class HotelRoomType(Enum):
    INDIVIDUAL = 'Individual'
    DOBLE = 'Doble'
    SUITE = 'Suite'




def main():
    #TESTING
    print("=================================================================.")
    print("Test Case 1: Check Class HotelRoomType.")
    print("=================================================================.")

    if isinstance(HotelRoomType.INDIVIDUAL, HotelRoomType):
        print("Test PASS. The enum for Individual has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(HotelRoomType.DOBLE, HotelRoomType):
        print("Test PASS. The enum for Doble has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(HotelRoomType.SUITE, HotelRoomType):
        print("Test PASS. The enum for Suite has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


def recommend_room(guests):
    if guests == 1:
        return HotelRoomType.INDIVIDUAL
    elif guests == 2:
        return HotelRoomType.DOBLE
    else:
        return HotelRoomType.SUITE

guest_count = 3
recommended_room = recommend_room(guest_count)
print(f"Para {guest_count} huéspedes, se recomienda una habitación de tipo: {recommended_room.name}")


if __name__ == "__main__":
    main()
