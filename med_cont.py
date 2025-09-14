import random

medicine_ch = [
    "Aspirin", "Paracetamol", "Ibuprofen", "Amoxicillin", "Metformin",
    "Atorvastatin", "Omeprazole", "Losartan", "Cetirizine", "Prednisone"
]

unique_medicines = random.sample(medicine_ch, k=10)

medicines = []

for med_name in unique_medicines:
    medicine = {
        "name": med_name,
        "amount": random.randint(0, 5000),
        "category": random.choice(["antibiotic", "vitamin", "vaccine"]),
        "t": random.randint(-10, 30)
    }
    medicines.append(medicine)

result = []

for m in medicines:
    if not isinstance(m["amount"], int):
        print("Помилка даних")
    if not isinstance(m["t"], (int, float)):
        print("Помилка даних")

    if m["t"] < 5:
        t_status = "Надто холодно"
    elif m["t"] > 25:
        t_status = "Надто жарко"
    else:
        t_status = "Норма"

    match m["category"]:
        case "antibiotic":
            c_status = "Рецептурний препарат"
        case "vitamin":
            c_status = "Вільний продаж"
        case "vaccine":
            c_status = "Потребує спецзберігання"
        case _:
            c_status = "Невідома категорія"

    result.append(f"{m['name']}: {c_status}, {t_status}")

for r in result:
    print(r)