def main():
    # Open file
    infile = open("WorldSeriesWinners.txt", "r")

    # Strip lines
    for line in open("WorldSeriesWinners.txt"):
        line = line.rstrip("\n")

    # Split and Read contents of the file
    winners = infile.read().splitlines()

    # Close file
    infile.close()

    # User input
    team_entered = input("Enter name of team: ")

    counter = 0

    # Lowercase Conversion
    for winner in winners:
        if team_entered.lower() == winner.lower():
            counter = counter + 1

    # Output
    if counter == 1:
        print(
            "The",
            team_entered,
            "won the world series",
            counter,
            "time between 1903 and 2009.",
        )
    elif counter > 1:
        print(
            "The",
            team_entered,
            "won the world series",
            counter,
            "times between 1903 and 2009.",
        )
    else:
        print("The", team_entered, "never won the world series.")


main()
