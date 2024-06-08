#Ejercicio de pasar frase a código morse
users = input("Escribe la frase que quieras pasar a código morse: ")
morse = {
    " ":"/",
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l": ".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"--..",
    "z":"--.."
}
for x in users:
    print(x)
for x in users:
    print(morse.get(f"{x}"))
