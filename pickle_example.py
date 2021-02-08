import pickle
import os

eof = False
path = "names_file.dat"

outfile = open("names_file.dat", "ab")
infile = open("names_file.dat", "rb")

print(os.path.getsize(path))


if os.path.getsize(path) > 0:
    names = pickle.load(infile)
    print(names)
    name = input("Add a name: ")
    names.append(name)
else:
    names = []
    name = input("Add a name: ")
    names.append(name)

print(names)
pickle.dump(names, outfile)
outfile.close

print(names)