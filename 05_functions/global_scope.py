chai_type = "Pain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
    kitchen()

front_desk()
print(f"Final global chai: {chai_type}")
