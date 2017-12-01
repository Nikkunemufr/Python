"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
def fahr(x):
        celcius=(x-32)*5/9
        print(celcius)

def celsius(c):
        fahrenheit=9/5*c+32
        print(fahrenheit)

x=int(input("1 pour convertion C/F, 2 pour convertion F/C "))
      
if x==1:
    c=float(input("temperature : "))
    celsius(c)
elif x==2:
    f=float(input("temperature : "))
    fahr(f)
else:
      x=int(input("Seulement 1 et 2 sont autoriser comme choix "))