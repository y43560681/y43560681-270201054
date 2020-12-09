books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
books1 = []
books2 = []
books_dict = {}
for i in books:
    if "'" in i:
        i = i.replace("'","")
        i = i.replace(" ", "")
        books1.append(i)
    elif " " in i:
        i = i.replace(" ","")
        books1.append(i)
    else:
        books1.append(i)

for i in books1:
    books2.append(set(i))

books_dict[books[0]] = len(books1[0]),len(books2[0])
books_dict[books[1]] = len(books1[1]),len(books2[1])
books_dict[books[2]] = len(books1[2]),len(books2[2])
books_dict[books[3]] = len(books1[3]),len(books2[3])



for i in books_dict.items():
    print(str(i[0])+"------->"+str(i[1]))