# def main():
# infile = open("WorldSeriesWinners.txt", "r")  # Open the file

# for line in open("WorldSeriesWinners.txt"):
# line = line.strip()  # But wait, strip the newlines first!

# winners = infile.read().splitlines()  # Read the contents of the file into the list

# Always remember to close the file

# team = input("Enter the name of a team: ")

# counter = 0  # If said team won a game, count how many times

# for winner in winners:  # convert input to lowercase for case-insensitive input
# if team == winners:
#   counter = counter + 1

# if counter == 1:  # Finally, print the results
#    print(
#        "The", team, "won the world series", counter, "time between 1903 and 2009."
#    )
# else:
#    print(
#       "The", team, "won the world series", counter, "times between 1903 and 2009."
#    )

# infile.close()


# main()


def main():
    infile = open("WorldSeriesWinners.txt", "r")  # Open the file

    for line in open("WorldSeriesWinners.txt"):
        line = line.rstrip("\n")  # But wait, strip the newlines first!

    winners = infile.read().splitlines()  # Read the contents of the file into the list

    infile.close()  # Always remember to close the file

    team = input("Enter the name of a team: ")

    counter = 0  # If said team won a game, count how many times

    for winner in winners:  # convert input to lowercase for case-insensitive input
        if team.lower() == winner.lower():
            counter = counter + 1

    if counter == 1:  # Finally, print the results
        print(
            "The", team, "won the world series", counter, "time between 1903 and 2009."
        )
    elif counter > 1:
        print(
            "The", team, "won the world series", counter, "times between 1903 and 2009."
        )
    else:
        print("The", team, "never won the world series.")


main()
