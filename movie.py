rented_movies = ["poo"]
movies = ["pee"]

def add_movies():
    pass

def search_movies():
    user_exit = False
    while user_exit == False:
        user_input = str(input("Enter the title of the movie you would like to search.\nType 'Finish' to return: "))
        title = user_input.lower()
        if title != "finish":
            for i in movies:
                if i == title:
                    print(f"\n{user_input} is currently available!\n")
                else:
                    for j in rented_movies:
                        if j == title:
                            print(f"\n{user_input} is currently being rented!\n")
                        else:
                            print(f"\nWe currently do not have {user_input} :(\n")
        else:
            start()
            user_exit = True

def rent_movies():
    user_exit = False
    while user_exit == False:
        user_input = str(input("Enter the name of the movie you would like to rent. \nType 'Finish' to return: "))
        title = user_input.lower()

def return_movies():
    pass

def generate_report():
    pass

def start():
    user_exit = False
    while user_exit != True:
        print("\n----- Movie Rentals -----\n")
        user_input = int(input("Choose your option: \n1 - Search for a Movie \n2 - Rent a Movie \n3 - Return a Movie \n4 - Admin Access\n\n"))
        if user_input == 1:
            search_movies()
        elif user_input == 2:
            rent_movies()
        elif user_input == 3:
            return_movies()
        else:
            print(f"Error: {user_input} is not an option!")
            start()
        user_exit = True


start()