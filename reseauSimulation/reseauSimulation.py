"""
    :Authors : MORTELIER Alexis < 21605783@etu.unicaen.fr>
"""
from random import randint

def NRZBitsToSignal(signaux):
        res=""
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


def NRZIBitsToSignal(sequence):
    res="+"
    for x in sequence:
        if int(x):
            if res[-1] == "-":
                res+="+"
            else:
                res+="-"
        else:
            if not res:
                res+="-"
            else:
                res+=res[-1]
    return res


def NRZISignalToBits(sequence):
    res=""
    i = 1
    while i < len(sequence):
        if sequence[i - 1] != sequence[i]:
            res +="1"
        else:
            res +="0"
        i += 1
    return res

def decimal_to_binary(number):
    i, ref = 7, 2 ** 7
    binary_length = ""
    while i >= 0:
        if ref > number:
            binary_length += '0'
        else:
            binary_length += '1'
            number -= ref
        ref -= 2 ** (i - 1)
        i -= 1
    return binary_length


def binary_to_decimal(number):
    i, res = 0, 0
    for x in number[::-1]:
        if int(x):
            res += 2 ** i
        i += 1
    return res

def couche1(trame_de_bits):
    """Represent the translation made by the NRZ encoding."""
    return trame_de_bits.replace("0", "-").replace("1", "+")

def couche1_nrzi(trame_de_bits):
    return NRZIBitsToSignal(trame_de_bits)

def couche1R(trame_de_bits):
    """Represent the translation made by the NRZ encoding."""
    return trame_de_bits.replace("-", "0").replace("+", "1")

def couche1R_nrzi(trame_de_bits):
    return NRZISignalToBits(trame_de_bits)

def couche2(message_from_sender):
    """Translate a message into a sequence of bits."""
    bin_length = decimal_to_binary(len(message_from_sender))
    res = bin_length + "01111110" + message_from_sender.replace("o", "0").replace("i", "1")
    return res

def couche2R(message_from_sender):
    """Translate a sequence of bits into a message."""
    border = "01111110"
    border_index = message_from_sender.find(border)
    len_message = binary_to_decimal(message_from_sender[border_index - 8:border_index])
    message_index = border_index + len(border)
    message = message_from_sender[message_index:message_index + len_message]
    return message.replace("0", "o").replace("1", "i")

def addIdentification(sequence):
    return sequence+"0001"+"0011"

def whoIsTheSender(sequence):
    border = "01111110"
    border_index = sequence.find(border)
    len_message = binary_to_decimal(sequence[border_index - 8:border_index])
    sender_index = border_index + len(border)+len_message
    sender = sequence[sender_index:sender_index + 4]
    return sender

def isAdressedToMe(sequence):
    recepteur="0011"
    border = "01111110"
    border_index = sequence.find(border)
    len_message = binary_to_decimal(sequence[border_index - 8:border_index])
    receiver_index = border_index + len(border)+len_message
    receiver = sequence[receiver_index+4:receiver_index + 8]
    if receiver==recepteur:
        return "message bien adressé"
    else:
        return "message ignoré"

def transmission(signal_from_sender):
    """Simulate the channel state (for instance: an electric wire).

    A channel exists before the transmitter wants to send the message. It
    initially contains noise: the receiver was aware before the transmitter
    sends its message.
    It also contains a final noise, because the receiver will also be aware
    after the sending of the message.
    The challenge of the second layer is to enable the receiver to determinate
    where the sent message begins or ends.
    """
    print("Nombre de signaux nécessaires pour envoyer le message: "
          + str(len(signal_from_sender)))
    # bruit initial :
    for x in range(0, randint(4, 10)):
        if randint(0, 1) == 1:
            signal_from_sender = "-" + signal_from_sender
        else:
            signal_from_sender = "+" + signal_from_sender
    # bruit final :
    for x in range(0, randint(4, 10)):
        if randint(0, 1) == 1:
            signal_from_sender = signal_from_sender + "-"
        else:
            signal_from_sender = signal_from_sender + "+"
    return signal_from_sender


def emission(message_from_sender):
    print("Message à envoyer: " + message_from_sender)
    trame_de_bits_envoyee = addIdentification(couche2(message_from_sender))
    print("Trame à envoyer: " + trame_de_bits_envoyee)
    signal_envoye = couche1_nrzi(trame_de_bits_envoyee)
    #signal_envoye = couche1(trame_de_bits_envoyee)
    print("Signal envoyé: " + signal_envoye)
    return signal_envoye


def reception(signal_sur_canal):
    print("Signal entendu, avec le bruit: " + signal_sur_canal)
    bits_recus = couche1R_nrzi(signal_sur_canal)
    #bits_recus = couche1R(signal_sur_canal)
    print("Bits reçus par le recepteur: " + bits_recus)
    message_recu = couche2R(bits_recus)
    print("Message reçu par le recepteur: " + message_recu)
    sender_recu = whoIsTheSender(bits_recus)
    print("L'emetteur: " + sender_recu)
    bon_destinataire = isAdressedToMe(bits_recus)
    print("Message bien adressé ? : " + bon_destinataire)
    return message_recu


def simulation(message_from_sender):
    signal_envoye = emission(message_from_sender)
    signal_sur_canal = transmission(signal_envoye)
    return reception(signal_sur_canal)


print(simulation("oooiii"))
