def start():    
    print("Witaj w programie który rozwiąrze każde zadanie fizyczne z jedną niewiadomą.")
start()

def dane():
    print("\nNajpierw poproszę cię o wpisanie danych. Wprowadź 'x' gdzie nie posiadasz danych.")
    s=input("droga = ")
    t=input("czas = ")
    v=input("prędkość = ")
    if s == "x":
        print("\nZatem droga jest naszą niewiadomą.")
    elif t == "x":
        print("\nZatem czas jest naszą niewiadomą.")
    elif v == "x":
        print("\nZatem prędkość jest naszą niewiadomą.")
    print("\n\nPodsumujmy:\ndroga =",s ,"\nczas = ",t ,"\nprędkość =",v)
    obliczenia(s, t, v)
def obliczenia(a, b, c):
    print("Przechodzimy do następnej części zadania czyli do obliczeń.")
def exercise():
    dane()
exercise()