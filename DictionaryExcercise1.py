import string

dic = {}

textFile = open("Text.txt", "r")

# Iterate over each line in the file

for line in textFile.readlines():

    tex = line

    tex = tex.lower()

    tex = tex.translate(
        str.maketrans("", "", string.punctuation)
    )  # removes every punctuation

    # section 2

    new = tex.split()

    for word in new:

        if word not in dic.keys():

            dic[word] = 1

        else:

            dic[word] = dic[word] + 1

for word in sorted(dic):

    print(word, dic[word], "\n")


textFile.close()