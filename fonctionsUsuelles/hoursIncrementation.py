"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""

def seconde(t):
    return t[0]*3600+t[1]*60+t[2]

def suivant(t):
    if t[2]==59:
        if t[1]==59:
            if t[0]==23:
                return(0,0,0)
            else:
                return(t[0]+1,0,0)
        else:
            return(t[0],t[1]+1,0)
    else:
        return(t[0],t[1],t[2]+1)

def nsec(t,n):
    for x in range(n):
        t=suivant(t)
    return t