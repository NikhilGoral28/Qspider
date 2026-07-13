class BookMyShow:
    def __init__(self, theater_name):
        self.theater_name = theater_name

        if self.theater_name == "PVR":
            print("\nMovies available at PVR:")
            self.movie1 = "Avatar: The Way of Water"
            self.movie2 = "The Batman"
            self.price1 = 850   
            self.price2 = 800

        elif self.theater_name == "INOX":
            print("\nMovies available at INOX:")
            self.movie1 = "Mission: Impossible - Fallout"
            self.movie2 = "Jurassic World: Dominion"
            self.price1 = 900
            self.price2 = 950

        else:
            print("Sorry, theater not available.")
            return

        print(f"1. {self.movie1}")
        print(f"2. {self.movie2}")

        # Ask movie choice AFTER showing movies
        self.movie_choice = input("\nEnter your movie choice (1 or 2): ")
        self.select_movie()

    def select_movie(self):
        if self.movie_choice == "1":
            self.selected_movie = self.movie1
            self.price = self.price1
        elif self.movie_choice == "2":
            self.selected_movie = self.movie2
            self.price = self.price2
        else:
            print("Invalid choice")
            return

        print(f"\nSelected Movie: {self.selected_movie}")
        print(f"Ticket Price: RS {self.price}")

        # Ask confirmation AFTER selection
        self.confirm = input("\nDo you want to book ticket? (yes/no): ")
        self.confirm_booking()

    def confirm_booking(self):
        if self.confirm == "yes":
            print(f"\nTicket for '{self.selected_movie}' booked successfully!")
        else:
            print("\nBooking cancelled.")


# Step 1: Take only theater input
print("Welcome to Book My Show!")
theater = input("Enter the name of the theater (PVR, INOX): ")

# Step 2: Pass to constructor
booking = BookMyShow(theater)

"""

class BookMyShow:

    def __init__(self, theater):
        self.theater = theater  

    def show_movies(self):
        if self.theater == 'PVR':
            print("Movies Available")
            print("1. Dhurandar - 20$\n2. KGF - 30$")
        elif self.theater == "INOX":
            print("Movies Available")
            print("1. Dhurandar - 20$\n2. KGF - 30$")
        else:
            print("Sorry, theater not available")

    def confirmation(self):
        self.movie = input("Enter your Choice: ")
        print(f"You selected the movie {self.movie}")
        confirm = input("Confirmation: YES/NO: ")

        if confirm.upper() == "YES":
            print("Congratulations! You are confirmed.")
        else:
            print("Thank you for using BookMyShow.")



print("Welcome to BookMyShow")
print("Theaters Available are:\n1. PVR \n2. INOX")
theater = input("Enter the theater: ")

ob = BookMyShow(theater)
ob.show_movies()
ob.confirmation()  """