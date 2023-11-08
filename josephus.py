n = int(input("Enter n:\n"))
soldiers = []

# Populate the soldiers
for i in range(0,n):
    soldiers.append(i+1)

# Remove the even soldiers, as first pass kills them
current_soldier = 1

def kill(soldiers):
    # If even, end of pass will start on first element, else it will start on last element
    new_soldiers = []
    if len(soldiers) > 1:
        for i in range(0,len(soldiers)):
            # even soldiers die, python is 0-major so preserve everything but the "odd" soldiers
            if i%2 == 0:
                new_soldiers.append(soldiers[i])
        # If even soldiers from start, begin with last element
        if len(soldiers)%2 == 1:
            new_soldiers = [new_soldiers[-1]] + new_soldiers[:-1]
            kill(new_soldiers)
        else:
            kill(new_soldiers)
    else:
        print("The surviving soldier is:", soldiers[0])

kill(soldiers)
