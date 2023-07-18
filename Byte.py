def BoolToInt(bit):
    if (bit):
        return 1
    return 0

def HexToBits(Hex):     # Converts Hexadecimal values to 4bits
    Hex = str(Hex)
    if (Hex.upper()=="F"):
        return "1111"
    elif (Hex.upper()=="E"):
        return "1110"
    elif (Hex.upper() == "D"):
        return "1101"
    elif (Hex.upper() == "C"):
        return "1100"
    elif (Hex.upper() == "B"):
        return "1011"
    elif (Hex.upper() == "A"):
        return "1010"
    elif (Hex.upper() == "9"):
        return "1001"
    elif (Hex.upper() == "8"):
        return "1000"
    elif (Hex.upper() == "7"):
        return "0111"
    elif (Hex.upper() == "6"):
        return "0110"
    elif (Hex.upper() == "5"):
        return "0101"
    elif (Hex.upper() == "4"):
        return "0100"
    elif (Hex.upper() == "3"):
        return "0011"
    elif (Hex.upper() == "2"):
        return "0010"
    elif (Hex.upper() == "1"):
        return "0001"
    elif (Hex.upper() == "0"):
        return "0000"

def BitsToHex(Bits):   #Converts 4bits to Hexadecimal value
    Bits = str(Bits)
    if Bits=="0000":
        return "0"
    elif Bits=="0001":
        return "1"
    elif Bits=="0010":
        return "2"
    elif Bits=="0011":
        return "3"
    elif Bits=="0100":
        return "4"
    elif Bits=="0101":
        return "5"
    elif Bits=="0110":
        return "6"
    elif Bits=="0111":
        return "7"
    elif Bits=="1000":
        return "8"
    elif Bits=="1001":
        return "9"
    elif Bits=="1010":
        return "A"
    elif Bits=="1011":
        return "B"
    elif Bits=="1100":
        return "C"
    elif Bits=="1101":
        return "D"
    elif Bits=="1110":
        return "E"
    elif Bits=="1111":
        return "F"

def IntToBool(bit):   # Converts integer to Boolean where 1 equals True and 0 equals False
    if (bit == 1):
        return True
    return False

def IntToByte(int):    #Creates an object of Byte with the value of the integer

    B = Byte(0, 0, 0, 0, 0, 0, 0, 0)
    int = int % 256
    if (int >= 128):
        B.bit7 = True
        int -= 128
    if (int >= 64):
        B.bit6 = True
        int -= 64
    if (int >= 32):
        B.bit5 = True
        int -= 32
    if (int >= 16):
        B.bit4 = True
        int -= 16
    if (int >= 8):
        B.bit3 = True
        int -= 8
    if (int >= 4):
        B.bit2 = True
        int -= 4
    if (int >= 2):
        B.bit1 = True
        int -= 2
    if (int >= 1):
        B.bit0 = True
        int -= 1
    return B

def IntToRegister(int):   #Creates an object of Register with the value of the integer
    B = Register(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if (int<0):
        B.bit15 = True

    int = int % 32768
    if (int >= 16384):
        B.bit14 = True
        int -= 16384
    if (int >= 8192):
        B.bit13 = True
        int -= 8192
    if (int >= 4096):
        B.bit12 = True
        int -= 4096
    if (int >= 2048):
        B.bit11 = True
        int -= 2048
    if (int >= 1024):
        B.bit10 = True
        int -= 1024
    if (int >= 512):
        B.bit9 = True
        int -= 512
    if (int >= 256):
        B.bit8 = True
        int -= 256
    if (int >= 128):
        B.bit7 = True
        int -= 128
    if (int >= 64):
        B.bit6 = True
        int -= 64
    if (int >= 32):
        B.bit5 = True
        int -= 32
    if (int >= 16):
        B.bit4 = True
        int -= 16
    if (int >= 8):
        B.bit3 = True
        int -= 8
    if (int >= 4):
        B.bit2 = True
        int -= 4
    if (int >= 2):
        B.bit1 = True
        int -= 2
    if (int >= 1):
        B.bit0 = True
        int -= 1
    return B

def ByteToInt(byte):   #Retreives the value inside the object byte in integer form
    i = 0
    if(byte.bit7):
        i += 128
    if (byte.bit6):
        i += 64
    if (byte.bit5):
        i += 32
    if (byte.bit4):
        i += 16
    if (byte.bit3):
        i += 8
    if (byte.bit2):
        i += 4
    if (byte.bit1):
        i += 2
    if (byte.bit0):
        i += 1
    return i

def RegisterToInt(register):   #Retreives the value inside the object register in integer form
    i = 0
    if (register.bit15):
        i += -32768
    if (register.bit14):
        i += 16384
    if (register.bit13):
        i += 8192
    if (register.bit12):
        i += 4096
    if (register.bit11):
        i += 2048
    if (register.bit10):
        i += 1024
    if (register.bit9):
        i += 512
    if (register.bit8):
        i += 256
    if (register.bit7):
        i += 128
    if (register.bit6):
        i += 64
    if (register.bit5):
        i += 32
    if (register.bit4):
        i += 16
    if (register.bit3):
        i += 8
    if (register.bit2):
        i += 4
    if (register.bit1):
        i += 2
    if (register.bit0):
        i += 1

    return i

def RegisterCodeToInt(RegCode):   #maps the register code to the corresponding register in our array
    RegCode = str(RegCode)
    if (RegCode=="00"):
        return 0
    elif (RegCode=="01"):
        return 1
    elif (RegCode=="02"):
        return 2
    elif (RegCode=="03"):
        return 3
    elif (RegCode=="04"):
        return 4
    elif (RegCode=="05"):
        return 5
    elif (RegCode=="06"):
        return 6
    elif (RegCode=="07"):
        return 7
    elif (RegCode=="08"):
        return 8
    elif (RegCode=="09"):
        return 9
    elif (RegCode=="0A"):
        return 10
    elif (RegCode=="0B"):
        return 11
    elif (RegCode=="0C"):
        return 12
    elif (RegCode=="0D"):
        return 13
    elif (RegCode=="0E"):
        return 14
    elif (RegCode=="0F"):
        return 15

class Byte:  # An object which stores 8bits, this will be the building blocks of our memory
    def __int__(self):
        self.bit0 = False
        self.bit1 = False
        self.bit2 = False
        self.bit3 = False
        self.bit4 = False
        self.bit5 = False
        self.bit6 = False
        self.bit7 = False

    def __init__(self,bit7,bit6,bit5,bit4,bit3,bit2,bit1,bit0):

        self.bit0 = bit0
        self.bit1 = bit1
        self.bit2 = bit2
        self.bit3 = bit3
        self.bit4 = bit4
        self.bit5 = bit5
        self.bit6 = bit6
        self.bit7 = bit7

    def Set(self,Hex):
        while (len(Hex) < 2):
            Hex = "0" + Hex
        L = HexToBits(Hex[0])
        R = HexToBits(Hex[1])
        self.bit7 = IntToBool(int(L[0]))
        self.bit6 = IntToBool(int(L[1]))
        self.bit5 = IntToBool(int(L[2]))
        self.bit4 = IntToBool(int(L[3]))
        self.bit3 = IntToBool(int(R[0]))
        self.bit2 = IntToBool(int(R[1]))
        self.bit1 = IntToBool(int(R[2]))
        self.bit0 = IntToBool(int(R[3]))

    def Add(self,Byte2):
        return IntToByte(ByteToInt(self) + ByteToInt(Byte2))

    def __str__(self):
        H1 = str(self.bit3) + str(self.bit2) + str(self.bit1) + str(self.bit0)
        H2 = str(self.bit7) + str(self.bit6) + str(self.bit5) + str(self.bit4)
        return (BitsToHex(H2) + BitsToHex(H1))

class Register:  #An object which stores 16bits, this will be the building block of our General and Special purpose Registers
    def __int__(self):
        self.bit0 = False
        self.bit1 = False
        self.bit2 = False
        self.bit3 = False
        self.bit4 = False
        self.bit5 = False
        self.bit6 = False
        self.bit7 = False
        self.bit8 = False
        self.bit9 = False
        self.bit10 = False
        self.bit11 = False
        self.bit12 = False
        self.bit13 = False
        self.bit14 = False
        self.bit15 = False

    def __init__(self,bit15,bit14,bit13,bit12,bit11,bit10,bit9,bit8,bit7,bit6,bit5,bit4,bit3,bit2,bit1,bit0):

        self.bit0 = bit0
        self.bit1 = bit1
        self.bit2 = bit2
        self.bit3 = bit3
        self.bit4 = bit4
        self.bit5 = bit5
        self.bit6 = bit6
        self.bit7 = bit7
        self.bit8 = bit8
        self.bit9 = bit9
        self.bit10 = bit10
        self.bit11 = bit11
        self.bit12 = bit12
        self.bit13 = bit13
        self.bit14 = bit14
        self.bit15 = bit15

    def Set(self,Hex):
        while(len(Hex)<4):
            Hex =  "0" + Hex
        L2 = HexToBits(Hex[0])
        L = HexToBits(Hex[1])
        R = HexToBits(Hex[2])
        R2 = HexToBits(Hex[3])

        self.bit15 = IntToBool(int(L2[0]))
        self.bit14 = IntToBool(int(L2[1]))
        self.bit13 = IntToBool(int(L2[2]))
        self.bit12 = IntToBool(int(L2[3]))
        self.bit11 = IntToBool(int(L[0]))
        self.bit10 = IntToBool(int(L[1]))
        self.bit9 = IntToBool(int(L[2]))
        self.bit8 = IntToBool(int(L[3]))
        self.bit7 = IntToBool(int(R[0]))
        self.bit6 = IntToBool(int(R[1]))
        self.bit5 = IntToBool(int(R[2]))
        self.bit4 = IntToBool(int(R[3]))
        self.bit3 = IntToBool(int(R2[0]))
        self.bit2 = IntToBool(int(R2[1]))
        self.bit1 = IntToBool(int(R2[2]))
        self.bit0 = IntToBool(int(R2[3]))

    def Add(self,Reg2):
        return IntToRegister(RegisterToInt(self) + RegisterToInt(Reg2))

    def Mul(self,Reg2):
        return IntToRegister(RegisterToInt(self)*RegisterToInt(Reg2))

    def __str__(self):
        st1 = ""
        st2 = ""
        st3 = ""
        st4 = ""
        st4 = st4 + str(BoolToInt(self.bit15))
        st4 = st4 + str(BoolToInt(self.bit14))
        st4 = st4 + str(BoolToInt(self.bit13))
        st4 = st4 + str(BoolToInt(self.bit12))
        st3 = st3 + str(BoolToInt(self.bit11))
        st3 = st3 + str(BoolToInt(self.bit10))
        st3 = st3 + str(BoolToInt(self.bit9))
        st3 = st3 + str(BoolToInt(self.bit8))
        st2 = st2 + str(BoolToInt(self.bit7))
        st2 = st2 + str(BoolToInt(self.bit6))
        st2 = st2 + str(BoolToInt(self.bit5))
        st2 = st2 + str(BoolToInt(self.bit4))
        st1 = st1 + str(BoolToInt(self.bit3))
        st1 = st1 + str(BoolToInt(self.bit2))
        st1 = st1 + str(BoolToInt(self.bit1))
        st1 = st1 + str(BoolToInt(self.bit0))
        return BitsToHex(st4) + BitsToHex(st3) + BitsToHex(st2) + BitsToHex(st1)

class SpecialPurposeRegisters:

    def __init__(self):
        self.FirstReg = IntToRegister(0)
        self.CodeBase = IntToRegister(0)
        self.CodeLimit = IntToRegister(0)
        self.CodeCounter = IntToRegister(0)
        self.StackBase = IntToRegister(0)
        self.StackLimit = IntToRegister(0)
        self.StackCounter = IntToRegister(0)
        self.DataBase = IntToRegister(0)
        self.DataLimit = IntToRegister(0)
        self.Flags = IntToRegister(0)
        self.EleventhReg = IntToRegister(0)
        self.TwelvthReg = IntToRegister(0)
        self.ThirteenthReg = IntToRegister(0)
        self.FourteenthReg = IntToRegister(0)
        self.FifteenthReg = IntToRegister(0)
        self.SixteenthRegister = IntToRegister(0)

    def SetCodeBase(self,Reg):
        self.CodeBase = Reg
    def SetCodeLimit(self,Reg):
        self.CodeLimit = Reg
    def SetCodeCounter(self,Reg):
        self.CodeCounter = Reg
    def SetStackBase(self,Reg):
        self.StackBase = Reg
    def SetStackLimit(self,Reg):
        self.StackLimit = Reg
    def SetStackCounter(self,Reg):
        self.StackCounter = Reg
    def SetDataBase(self,Reg):
        self.DataBase = Reg
    def SetDataLimit(self,Reg):
        self.DataLimit = Reg
    def SetFlagCarry(self,IntBool): #IntBool represents integer values either 0 or 1
        self.Flags.bit0 = IntBool
    def SetFlagZero(self,IntBool):
        self.Flags.bit1 = IntBool
    def SetFlagSign(self,IntBool):
        self.Flags.bit2 = IntBool
    def SetFlagOverflow(self,IntBool):
        self.Flags.bit3 = IntBool



    def GetCodeBase(self):
        return self.CodeBase
    def GetCodeLimit(self):
        return self.CodeLimit
    def GetCodeCounter(self):
        return self.CodeCounter
    def GetStackBase(self):
        return self.StackBase
    def GetStackLimit(self):
        return self.StackLimit
    def GetStackCounter(self):
        return self.StackCounter
    def GetDataBase(self):
        return self.DataBase
    def GetDataLimit(self):
        return self.DataLimit
    def GetFlagCarry(self):
        return self.Flags.bit0
    def GetFlagZero(self):
        return self.Flags.bit1
    def GetFlagSign(self):
        return self.Flags.bit2
    def GetFlagOverflow(self):
        return self.Flags.bit3