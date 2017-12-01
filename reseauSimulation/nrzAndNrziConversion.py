"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
def NRZBitsToSignal(signaux):
        res=[]
        for x in range(len(signaux)):
                if signaux[x]=="0":
                        res+="-"
                elif signaux[x]=="1":
                        res+="+"
        return res


def NRZSignalToBits(signaux):
        res=""
        for x in range(len(signaux)):
                if signaux[x]=="-":
                        res+="0"
                elif signaux[x]=="+":
                        res+="1"
        return res


def NRZIBitsToSignal(signaux):
        res=[]
        if signaux[0]=="0":
                res+="-"
        elif signaux[0]=="1":
                res+="+"
        for x in range(1,len(signaux)):

                if signaux[x]=="0":
                        if res[x-1]=="+":
                                res+="-"
                        else:
                                res+="+"

                elif signaux[x]=="1":
                        if res[x-1]=="+":
                                res+="+"
                        else:
                                res+="-"
        return res


def NRZISignalToBits(signaux):
        res=""
        i=1
        while i<len(signaux):
                if signaux[i-1]!= signaux[i]:
                        res+="1"
                else:
                        res+="0"
                i+=1
        return res


print(NRZISignalToBits(['-','-','+','+','-']))
