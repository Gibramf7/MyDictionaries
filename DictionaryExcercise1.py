def main():
    text = open("text.txt")
    dict = ()
    textlist = []
    line = text.readline()

    word_counts = []

    for word in line.split():
        if word in word_counts():
            word_counts[word] += 1
        else:
            word_counts[word] = 1

        print(dict)

    for word.count in sorted(word_counts.items()):
        print(dict)


main()