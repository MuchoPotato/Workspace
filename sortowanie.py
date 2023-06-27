print ("Wskaż jakie ma być zastosowane sortowanie")
a = print("a) Malejąco")
b = print("b) Rosnąco")
choice = input("która forma: ", )

if choice == a:
    j= int(input())
    k= int(input())
    if j > k:
        print(k, b)
else:
    print(j, k)
