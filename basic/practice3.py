total = 0

start = input (" start num: ")
end = input ( "end num: ")

start = int(start)
end = int(end)

for i in range(start, end):
    if i % 7 == 0:
        print(i,"... multiple of 7")
        continue
    
    total = total + i
    print(i, "   ", total)
    if total >= 2000:
        print ("Over 2000.")
        break

print("Terminates the program.")

