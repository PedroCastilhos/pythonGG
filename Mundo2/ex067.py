#67

number = 10


while number > 0: 
    number = int(input("Tabuada de qual número? "))
    if number < 0:
        break
    print(f'{number} X 1 = {number * 1}')
    print(f'{number} X 2 = {number * 2}')
    print(f'{number} X 3 = {number * 3}')
    print(f'{number} X 4 = {number * 4}')
    print(f'{number} X 5 = {number * 5}')
    print(f'{number} X 6 = {number * 6}')
    print(f'{number} X 7 = {number * 7}')
    print(f'{number} X 8 = {number * 8}')
    print(f'{number} X 9 = {number * 9}')
    print(f'{number} X 10 = {number * 10}')
    

print("Fim")