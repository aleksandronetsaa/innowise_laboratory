# Генерируем профиль
def generate_profile(age):
    categories = ["Child", "Teenager", "Adult"]

    if age <= 12:
        return categories[0]
    elif age <= 19:
        return categories[1]
    else:
        return categories[2]
# 1. Имя и год рождения
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
# 1.1 Вычисляем возраст
current_age = 2025 - birth_year
# 2. Хобби
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)
# 3. Определяем стадию жизни
life_stage = generate_profile(current_age)

# 4. Собираем профиль
user_profile = {
    "name": user_name,
    "age": current_age,
    "life_stage": life_stage,
    "hobbies": hobbies
}
# 5. Вывод профиля
print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['life_stage']}")
if len(hobbies) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for h in hobbies:
        print(f"- {h}")
print("---")
