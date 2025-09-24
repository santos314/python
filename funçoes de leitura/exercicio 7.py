
def celsius_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit
    print(f"{graus_celsius}°C é igual a {graus_fahrenheit}°F.")


graus_celsius = float(input("Digite a temperatura em graus Celsius: "))

graus_fahrenheit = celsius_para_fahrenheit(graus_celsius)

print(f"{graus_celsius}°C é igual a {graus_fahrenheit}°F.")
