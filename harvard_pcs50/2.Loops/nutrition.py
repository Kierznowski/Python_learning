fdalist = {"Apple": "130", "Avocado": "50", "Banana": "110", "Cantaloupe": "50", "Grapefruit": "60",
"Grapes": "90", "Kiwi": "90", "Lemon": "15", "Lime": "20", "Nectarine": "60"}

while True:
    try:
        fruit = input("Item: ").title()
    except:
        continue
    else:
        print(fdalist[fruit])