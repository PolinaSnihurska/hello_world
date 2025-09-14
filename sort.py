from faker import Faker
import random

fake = Faker("uk_UA")

clients = []
for _ in range(10):
    client = {
        "ім’я": fake.first_name(),
        "сума угоди": random.randint(10, 5000),
        "статус перевірки": random.choice(["clean", "suspicious", "fraud"])
    }
    clients.append(client)

result = []

for c in clients:
    if not isinstance(c["сума угоди"], (int, float)):
        print(f"{c['ім’я']}: Фальшиві дані")

    if c["сума угоди"] < 100:
        category = "Дрібнота"
    elif 100 < c["сума угоди"] < 999:
        category = "Середнячок"
    else:
        category = "Великий клієнт"

    match c["статус перевірки"]:
        case "clean":
            decision = "Працювати без питань"
        case "suspicious":
            decision = "Перевірити документи"
        case "fraud":
            decision = "Y чорний список"
        case _:
            decision = "Невідомий статус"

    result.append(f"{c['ім’я']}: {category} — {decision}")

for r in result:
    print(r)