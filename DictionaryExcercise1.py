file = open("text.txt", "r")

text = file.read()
text = text.replace("\n", "")

word_list = text.split(" ")

for word in word_list:
    word_count = ""
    for x in range(len(word)):
        word_count += word[x]
    word_list[word_list.index(word)] = word_count

while "" in word_list:
    word_list.remove("")

word_dict = ()
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print("World\tFrequency")
for word in word_dict:
    print(format(word), "\t\t", format(word_dict[word]))

file.close()