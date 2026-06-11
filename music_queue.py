queue = []

while True:
    print("=" * 40)
    print("1. Add Song")
    print("2. Play Next Song")
    print("3. Show Queue")
    print("4. Exit")
    print("=" * 40)
    
    choice = int(input("Enter Choice: "))
    
    if choice == 1:
        song = input("Enter Your Song")
        queue.append(song)
        print(queue)
    
    if choice == 2:
        if len(queue) > 0:
            print(queue[0])
            queue.pop(0)
            print(queue)
        else:
            print("No Music")
            
    if choice == 3:
        if len(queue) > 0:
            print(queue)
        else:
            print("Queue is Empty")
            
    if choice == 4:
        print("Vist Again!")
        break
