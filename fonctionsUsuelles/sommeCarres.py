"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
def sommeCarres (n):
    """Retourne la somme des carrés des entiers entre 0 et n (inclus)."""
    res=0
    for i in range(n):
        res=res+i*i
    return res