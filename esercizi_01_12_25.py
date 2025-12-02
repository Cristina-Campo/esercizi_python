#esercizio 1
# Stampa, in console, il tuo nome e il tuo cognome raccogliendoli con un input. 
# Utilizza 2 variabili distinte e separate


mioNome = input("Qual è il tuo nome?  ")
mioCognome = input("E il tuo cognome?  ")
print("Ciao ", mioNome, mioCognome , "!")
print("Benvenuto/a in questa lezione di ripasso di geometria!")


# Esercizio 2
# Calcola l'area e il perimetro di un rettangolo avente base = 6.9 e altezza = 5.2

base = 6.9
altezza = 5.2

perimetroRet = base + base + altezza + altezza
print("IL RETTANGOLO")
print("    ____ ")
print("   |    |")
print("   |    |")
print("   |____|")
print("Considerando un rettangolo con base ", base , "e altezza ", altezza)
print("Questo è il perimetro del rettangolo: (B * 2) + (h * 2) = ", perimetroRet)
area = base * altezza
print("Mentre questa è l'area del rettangolo: B * h = ", area)
print("********************************************************")

#Esercizio 3
#Calcola l'area e il perimetro del seguente triangolo rettangolo. 
#lato1 = 9
#lato2 = 12
#lato3 = 15
#Dimostra il teorema di pitagora. Verifica che la somma dei quadratu dei 2 lati 
#sia uguale al quadrato del lato3.

lato1 = 9
lato2 = 12
lato3 = 15

print("IL TRIANGOLO RETTANGOLO")
print("        *")  
print("      *    *")
print("    *       *")
print("   *         *")
print("   ***********")
print("Considerando un triangolo rettangolo ha lato1 = " , lato1 , ", lato2 = " , lato2 , "e lato3 = ", lato3)
perimetroTri = lato1 + lato2 + lato3
print("Questo è il perimetro del triangolo: l1 + l2 + l3 = ", perimetroTri)
areaTri = (lato1 * lato2)/2
print("Questa è l'area del triangolo rettangolo: (l1 + l2) / 2 = ", areaTri)
print("********************************************************")

lato1Q = lato1 ** 2
lato2Q = lato2 ** 2
lato3Q = lato3 ** 2

print("Dimostrazione del teorema di Pitagora")
sommaLati = lato1Q + lato2Q
print("La somma dei quadrati dei due lati è: ", sommaLati)
print("Mentre il lato3 al quadrato fa: ", lato3Q)

if sommaLati == lato3Q :
    print("Sono uguali! Nice :)")
else: print("NOPE, abbiamo sbagliato qualcosa")
print("********************************************************")

#Esercizio 4
#Calcola l'area  e il perimetro i una circonferenza di raggio 8.5

print("IL CERCHIO")
print("       ***")
print("     *     *")
print("     *     *")
print("       ***")
raggio = 8.5
PI_GRECO = 3.14
print("Data una circonferenza con raggio = ", raggio)
areaCerchio = PI_GRECO * (raggio) ** 2
print("Questa è l'area del cerchio: ", areaCerchio)
perimetroCerchio = 2 * PI_GRECO * raggio
print("E questo è il perimetro del cerchio: ", perimetroCerchio)
print("Spero che questo ripasso ti sia piaciuto! A presto <3")
print("#########################################################")
