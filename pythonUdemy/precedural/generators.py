

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters= ['A','B','C','D']
    for i in range(number):
        yield letters[i % len(letters)]

def generate_row_numbers():
    """Generator that yields row numbers, skipping row 13."""
    row = 1
    while True:
        if row == 13:
            row += 1
            continue
        yield row
        row += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = ['A', 'B', 'C', 'D']
    row_numbers = generate_row_numbers()  # Row number generator
    seat_count = 0
    while seat_count < number:
        row = next(row_numbers)
        for letter in seat_letters:
            if seat_count >= number:
                return
            yield f"{row}{letter}"
            seat_count += 1
            
def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    
    seat_generator = generate_seats(len(passengers))  # Generate seats for the number of passengers
    
    assigned_seats = {}
    for passenger in passengers:
        seat = next(seat_generator)  # Get the next seat from the generator
        assigned_seats[passenger] = seat  # Assign the seat to the passenger
    
    return assigned_seats
    
    
passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']

print(assign_seats(passengers))