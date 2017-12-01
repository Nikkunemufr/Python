"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""

tab=[1,9,4,3,9,4,4,1,6]

def elimine(tab=tab,c=8):
    newtab=[]
    for elem in tab:
        if elem!=c:
            if elem not in newtab:
                newtab+=[elem]
    return newtab
	
print(tab)
print(elimine(tab,8))
