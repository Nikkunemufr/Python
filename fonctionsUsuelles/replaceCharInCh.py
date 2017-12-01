"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
exemple="coucou"
def replaceCharInCh(ch=exemple):
	res=""
	for x in range(len(ch)):
		if x%2==0:
			res+=ch[x]
		else:
			res+="*"
	print(res)