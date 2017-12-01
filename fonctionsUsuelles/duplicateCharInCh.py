"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
exemple="coucou"
def duplicateCharInCh(ch=exemple):
	res=""
	for x in range(len(ch)):
		res+=ch[x]*2
	print(res)