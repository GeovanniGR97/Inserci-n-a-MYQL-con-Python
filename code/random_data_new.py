from faker import Faker

fake = Faker()
data = []

for _ in range(100):
    # Generar un UUID, un nombre, una población simulada y kilómetros simulados
    data.append((
        fake.uuid4(),
        fake.name(),
        fake.random_int(min=1000, max=1000000),  # Generar un número aleatorio para la población
        fake.random_number(digits=4)  # Generar un número aleatorio para los kilómetros
    ))

# Ejemplo: imprimimos los primeros 5 elementos para verificar los datos
print(data[:5])

prepared_data = [(name, population, kilometers) for _, name, population, kilometers in data]
