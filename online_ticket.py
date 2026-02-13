seats = 50

print("Online Ticket Booking System")
print("Total seats available:", seats)

while seats > 0:
    try:
        print("\nSeats remaining:", seats)
        inp = input("Enter number of tickets to book (or type exit): ")

        if inp.lower() == "exit":
            print("Booking closed by user.")
            break

        tickets = int(inp)

        if tickets <= 0:
            raise Exception("Ticket count must be greater than zero.")

        if tickets > seats:
            raise Exception("Not enough seats available.")

        seats -= tickets
        print("Booking successful.")
        print("Tickets booked:", tickets)
        print("Seats left:", seats)

        if seats == 0:
            print("\nAll seats are booked. Housefull.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print("Error:", e)