
def toDecimal (n : str) -> int :
    HexInDecimal = {
     "A" : 10,
     "B" : 11,
     "C" : 12,
     "D" : 13,
     "E" : 14,
     "F" : 15
    }
    if n.upper() in HexInDecimal.keys() :
        return HexInDecimal[n]
    else :
        return int(n)


def convertHexToDecimal (numberInHex : str ) -> int :
    power = 0
    numberInDecimal = 0
    numberInHex = numberInHex.upper()
    numberInHex = reversed(numberInHex)
    for digit in numberInHex :
        digit = toDecimal(digit)
        numberInDecimal += digit * (16**power)
        power += 1
    return int(numberInDecimal)

#*** MAIN FUNCTION ***#

# hexNumber = "1CCF8A6734A0A153017B478FC7EB9709193759BE"
hexNumber = "4B07D3B4"
hexNumber = "d1af2403-3c37-4e60-86c6-9249d72d135a".replace("-","")
hexNumber = "2cd007ff7628431181e458aaf642b0b0"
decimalNumber = convertHexToDecimal(hexNumber)
print(f"Hex Number = {hexNumber}")
print(f"Decimal Number = {decimalNumber}")

### CHECK IF CONVERTING IS CORRECT 
areSame = hexNumber.lower() == hex(decimalNumber).lower().replace("0x","")       
print("------------------------")
print(f"Hex == Dec ?? {areSame}")

