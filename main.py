def one():

    # Имеется файл JSON с информацией о продуктах:

    import json
    with open("list.json", "r") as file:
        data = json.load(file)
        for i in data["products"]:
            print("Название: ", i["name"])
            print("Цена : ", i["price"])
            print("Вес: ", i["weight"])
            print("Название: ", i["name"])
            print("В наличии! " if i["available"] else "Нет в наличии", "\n")


def two():
    import json

    k = int(input("Введите количество товаров для добавления: "))

    products = {"products": []}
    for i in range(k):
        name = input("Название: ")
        price = int(input("Цена: "))
        weight = int(input("Вес: "))
        available = bool(input("В наличии 0/1: "))
        products["products"].append({"name": name, "price": price, "weight": weight, "available": available})

    with open("list.json", "r") as file:
        data = json.load(file)

    data["products"].extend(products["products"])

    for i in data["products"]:
        print("Название: ", i["name"])
        print("Цена: ", i["price"])
        print("Вес: ", i["weight"])
        print("В наличии" if i["available"] else "Нет в наличии!", "\n")

    with open("list.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def three():

    d = {}

    with open("engrus.txt", "r") as file:
        for line in file:
            en_w = line.split("-")[0].strip()
            ru_ws = line.split("-")[1].strip().split(',')
            for i in ru_ws:
                i = i.strip()
                if i in d.keys():
                    d[i] = d[i] + ", " + en_w
                else:
                    d[i] = en_w

    with open("ruseng.txt", "w") as file:
        for i in sorted(d.keys()):
            file.writelines(f"{i} - {d[i]}\n")



