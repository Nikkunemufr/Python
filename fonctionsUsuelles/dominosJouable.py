"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
dominos=((1,4),(4,5),(0,5),(0,0),(0,1))
debut=3
fin=5
somme=0
for i in range(len(dominos)):
    somme+=dominos[i][0]+dominos[i][1]
print(somme)

print("dominos : " + str((debut,fin)))

for i in range(len(dominos)):
    if dominos[i][0]==debut or dominos[i][1]==debut or dominos[i][0]==fin or dominos[i][1]==fin:
        print("Vous pouvez jouer",dominos[i])
    else:
        print("Vous ne pouvez pas jouer",dominos[i])

print("dominos : " + str((debut,fin)))
s=()
for i in range(len(dominos)):
    if dominos[i][0]==debut or dominos[i][1]==debut or dominos[i][0]==fin or dominos[i][1]==fin:
        s+=(dominos[i],)
print("Vous pouvez jouer",s)


