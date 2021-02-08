import string

dict = {}

# Open file
textfile = open("text.txt", "r")

# Read lines in file
for line in textfile.readlines():
    text = line
    text = text.lower()

# Remove empty punctaution strings
    text = text.translate(str.maketrans("", "", string.punctuation))

    new = text.split()
# Output
    for word in new:
        if word not in dict.keys():
            dict[word] = 1
        else:
            dict[word] = dict[word] + 1


for word in sorted(dict):
    print(word, dict[word], "\n")

# Close file
textfile.close()
