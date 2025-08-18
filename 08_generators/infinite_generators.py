def infinite_chai():
    count=1
    while True:
        yield f"Refill #{count}"
        count+=1

user1 = infinite_chai()
user2 = infinite_chai()

for _ in range(3):
    print(f"{next(user1)}")

for _ in range(5):
    print(f"{next(user2)}")
