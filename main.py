from re import T


def start():    
    print("Witaj w programie który rozwiąrze każde zadanie fizyczne z jedną niewiadomą.")
    print("Wpisuj dane według układu jednostek miar SI")
start()

def dane():
    print("\nNajpierw poproszę cię o wpisanie danych. Wprowadź odpowiedni numer który odpowiada nie posiadania danych podanej rzeczy.")
    print("\n1. Droga\n2. Czas\n3. Prędkość")
    x = int(input("\n"))
    if x == 1:
        print("\nWprowadź resztę danych:")
        t = int(input("czas = "))
        v = int(input("prędkość = "))
        s = "x"
    elif x == 2:
        print("\nWprowadź resztę danych:")
        s = int(input("droga = "))
        v = int(input("prędkość = "))
        t = "x"
    elif x == 3:
        print("\nWprowadź resztę danych:")
        t = int(input("czas = "))
        v = "x"
        s = int(input("droga = "))
    print("\n\nPodsumujmy:\ndroga =",s ,"\nczas = ",t ,"\nprędkość =",v)
    obliczenia(s, t, v)
def obliczenia(a, b, c):
    wzor = "V=S/t"
    print("\n\nPrzechodzimy do następnej części zadania czyli do obliczeń.")
    print("\nWzór, który tu użyjemy to:", wzor)
    if c == "x":
        print("Oblicznenia:", c, "=", a, "/", b)
        print("\n", c,"=", a/b)
        print("Wynik końcowy:", a/b, "m/s")
        print("\t",(a/1000)/(b/3600), "km/h")
    if a == "x":
        print("Oblicznenia:", c, "=", a, "/", b)
        print("Przekształcanie wzoru:", a, "=", c, "*", b)
        print("\n", a,"=", c*b)
        print("Wynik końcowy:", c*b, "m")
        print("\t", c*b/1000, "km")
    if b == "x":
        print("Oblicznenia:", c, "=", a, "/", b)
        print("Przekształcenie wzoru:", b, "=", a, "/", c)
        print("\n", b,"=", a/c)
        print("Wynik końcowy:", a/c, "s")
        print("\t", a/c/60, "h")
def exercise():
    dane()
exercise()