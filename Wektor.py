import random
import math

"""Funkcje umożliwiające tworzenie obiektów typu wektor oraz działania na nich."""

class Vector:
    def __init__(self, args=3):
        """Stwórz obiekt klasy wektor o podanym rozmiarze i wszystkich współrzędnych równych 0.

        Input:
        args(int) - ilu wymiarowy wektor ma zostać stworzony.

        Output:
        W razie wystąpienia błędu program zwraca informację, że należy podać jako parametr liczbę całkowitą.
        """
        
        try:
            type(args) == int and args >= 0
            list = []
            for i in range(args):
                list.append(0)
            self.lista = list
        except NameError:
            print("Podaj liczbę całkowitą większą lub równą 0.")
        except AttributeError:
            print("Podaj całkowitą, większą lub równą 0 liczbę współrzędnych, dla których zostanie wygenerowany wektor.")
        except:
            print("Coś poszło nie tak. Spróbuj wpisać liczbę całkowitą większą lub równą 0.")

    def los(self):
        """Wygeneruj losowo współrzędne wektora w zakresie (-10,10).
        
        Output:
        self.lista - losowo wygenerowane współrzędne wektora; informacja w przypadku błędu.
        """
        try:   
            for i in range(len(self.lista)):
                self.lista[i] = random.uniform(-10,10)
            return self.lista
        except AttributeError:
            return "Nie udało się wygenerować listy argumentów. Stwórz wektor, podając liczbę całkowitą!"
    
    
    def elementy_wektora(self, arg = [0,0,0]):
        """Przypisz wektorowi konkretne współrzędne.
        
        Input:
        arg (lista) - lista nowych współrzędnych wektora.
        Output: 
        self.lista - lista nowych współrzędnych wektora; informacja w przypadku błędu.
        """
        
        if type(arg) == list and len(arg) == len(self.lista):
            lista = []
            for i in range(len(arg)):
                lista.append(arg[i])
            self.lista = lista
            return self.lista
        elif TypeError:
            return "Należy wpisać listę składającą się z tak wielu argumentów, jak wyjściowy wektor."
        elif type(arg[i]) == str:
                    return "Nie można wykonać operacji na wektorze, którego elementami są znaki inne niż cyfry!"
        elif AttributeError:
            return "Nie udało się wygenerować listy argumentów. Stwórz wektor, podając liczbę całkowitą!"
        else:
            return "Nie udało się wykonać operacji."
    
    def __add__(self, other):
        """Umożliwiaj operację dodawania dwóch wektorów.
        
        Input:
        Other - inny obiekt typu wektor, który ma zostać dodany do wektora oznaczanego przez self.
        Output:
        Wynik dodawania do siebie dwóch wektorów w formie listy współrzędnych; informacja w przypadku błędu.
        """
        if len(other.lista) == len(self.lista):
            list = []
            for i in range(len(self.lista)):
                c = self.lista[i] + other.lista[i]
                list.append(c)
            self.lista = list
            return self.lista
        elif len(other.lista) != len(self.lista):
            return "Wektory muszą mieć ten sam rozmiar, aby można było je dodać."
        elif IndexError:
            return "Wektory muszą mieć ten sam rozmiar, aby można było je dodać"
        else:
            return "Nie udało się wykonać operacji!"
    
    def __sub__(self, other):
        """Umożliwiaj odejmowanie od siebie dwóch wektorów.
        
        Input:
        Other - inny obiekt typu wektor, który ma zostać odjęty od wektora oznaczanego przez self.
        Output:
        Wynik odejmowania od siebie dwóch wektorów w formie listy współrzędnych; informacja w przypadku błędu.
        """
        if len(other.lista) == len(self.lista):
            list = []
            for i in range(len(self.lista)):
                s = self.lista[i] - other.lista[i]
                list.append(s)
            self.lista = list
            return self.lista
        elif len(other.lista) != len(self.lista):
            return "Wektory muszą mieć ten sam rozmiar, aby można było je odjąć." 
        elif IndexError:
            return "Wektory muszą mieć ten sam rozmiar, aby można było je odjąć"
        else:
            return "Nie udało się wykonać operacji!"
    
    def mnozenie_przez_skalar(self, a=1.0):
        """Pomnóż wszystkie współrzędne wektora o podany skalar.
        
        Input:
        a(float/int) - liczba, o którą ma zostać pomnożona każda współrzędna.
        Output:
        self.lista - lista współrzędnych pomnożona przez podany skalar; informacja w przypadku błędu.
        """
        try:
            type(a) == float
            for i in range(len(self.lista)):
                self.lista[i] = a*self.lista[i]
            return self.lista
        except type(a) == int:
            for i in range(len(self.lista)):
                self.lista[i] = a*self.lista[i]
            return self.lista
        except AttributeError:
            return "Nie udało się wykonać operacji. Najpierw stwórz wektor, podając liczbę całkowitą!"
        except:
            return "Nie można wykonać operacji, jeżeli parametrem nie jest liczba zmiennoprzecinkowa lub całkowita."
    
    def dlugosc_wektora(self):
        """Podaj długość danego wektora.
        
        Output:
        Dlugosc (float) - długość wektora; informacja w przypadku błędu.
        """
        dlugosc = 0
        for i in range(len(self.lista)):
            if type(self.lista[i]) == str:
                raise ValueError ("Nie można obliczyć długości wektora składającego się ze znaków innych niż cyfry!")
            else:
                dlugosc += self.lista[i]**2
        dlugosc = math.sqrt(dlugosc)
        return dlugosc

    
    def suma_elementow(self):
        """Podaj sumę elementów danego wektora.
        
        Output:
        suma (float/int) - suma wszystkich współrzędnych danego wektora; informacja w przypadku błędu.
        """
        suma = 0
        for i in range(len(self.lista)):
            if type(self.lista[i]) == str:
                raise ValueError ("Nie można obliczyć sumy dla wektora składającego się ze znaków innych niż cyfry!")
            else:
                suma += self.lista[i]
        return suma
    
    def __mul__(self, other):
        """Podaj wartość iloczynu skalarnego dwóch wektorów.
        
        Input:
        Other - inny obiekt należący do klasy Vector.
        Output:
        suma (float/int) - iloczyn skalarny dwóch wektorów; informacja w przypadku błędu.
        """
        try:
            len(self.lista) == len(other.lista)
            iloczyn = 0
            for i in range(len(self.lista)):
                    iloczyn += (self.lista[i])*(other.lista[i])
            return iloczyn
        except AttributeError:
            return "Nie udało się wykonać operacji. Najpierw stwórz wektor, podając liczbę całkowitą."
        except:
            return "Nie można obliczyć iloczynu skalarnego wektorów o różnych długościach."

    
    def __contains__(self, x):
        """Sprawdź, czy podany element należy do współrzędnych wektora.
        
        Input:
        x - element, który ma zostać sprawdzony.
        Output:
        True - x znajduje się wśród współrzędnych wektora.
        False - x nie znajduje się wśród elementów wektora.
        """
        if x in self.lista:
            return True
        else:
            return False
        
    def __str__(self):
        """Zwróć interpretację tekstową wektora.
        
        Output:
        self.lista (str) - reprezentacja wektora w formie tekstowej.
        """
        return (str(self.lista))
    
    def __getitem__(self, i = 0):
        """Podaj współrzędną wektora znajdującą się na wskazanej pozycji.
        
        Input:
        i (int) - pozycja współrzędnej, która ma zostać sprawdzona.
        Output:
        self.lista[i] - współrzędna, która znajduje się na wskazanej pozycji; informacja w przypadku błędu.
        """
        try:
            return self.lista[i]
        except IndexError:
            return "Nie można podać współrzędnej dla tego numeru indeksu!"
        except AttributeError:
            return "Nie można wykonać operacji. Najpierw stwórz wektor, podając liczbę całkowitą."






