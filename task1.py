#Варіант 3, завдання №1
import pandas as pd
df = pd.read_csv('carsale.csv')
print("Початкові дані:")
print(df)
new = []
for month in range(1, 4):
    print(f"\nВведіть дані за місяць {month}:")
    months = {}
for firm in df["Фірми"]:
    sales = int(input(f"Кількість проданих автомобілів для {firm}: "))          
new.append(months)
new_df = pd.DataFrame(new)
df = pd.concat([df, new_df], ignore_index=True)
df.to_csv('updatedcarsale.csv', index=False)
print("Оновлені дані записані в файл 'updatedcarsale.csv'.")