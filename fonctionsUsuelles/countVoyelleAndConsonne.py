"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
ch="python est un langage informatique vraiment très puissant  tout en étant très simple et intéressant"
def countVoyelleAndConsonne(ch=exemple):
	voyelle=["a","e","i","o","u","y"]
	nbvoyelle=0
	nbconsonne=0
	for x in range(len(ch)):
		if ch[x] in voyelle:
			nbvoyelle+=1
		else:
			nbconsonne+=1
	print(nbvoyelle, nbconsonne)