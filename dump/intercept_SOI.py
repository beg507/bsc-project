def intercept_SOI (states_jupiter, states_ship):
    if len(states_jupiter) < 2 or len(states_ship) < 2:
        return -1

    for i in range(min(len(states_jupiter), len(states_ship))):
        if states_jupiter[i].any() == states_ship[i].any():
            if i + 1 < len(states_jupiter) and i + 1 < len(states_ship) and states_jupiter[i+1].any() == states_ship[i+1].any():
                return i
            else:
                return -1


index = intercept_SOI(states_jupiter, states_ship)
if index == -1:
    print("There is no point of equality between the arrays.")
else:
    print("The point of equality between the arrays where their first two values are equal is at index", index)