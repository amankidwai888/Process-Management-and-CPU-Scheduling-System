from Byte import *

def MakeMemory(FileName,SPRs): #Creates Memory, An array with length 8000, and copies the value from file to this memory

    Mem = []
    for i in range(8000):
        Mem.append(Byte(0, 0, 0, 0, 0, 0, 0, 0))


    F = open(FileName, "r")
    L = F.read().split(" ")
    for i in range(len(L)):
        Mem[i+2].Set(L[i])

    Mem[0]=IntToByte(1)
    Mem[1]=IntToByte(2+50+1+len(L))

    SPRs.SetCodeBase(2)
    SPRs.SetCodeLimit(2+len(L))
    SPRs.SetCodeCounter(2)

    SPRs.SetDataBase(3+len(L))
    SPRs.SetDataLimit(3+len(L))

    SPRs.SetStackBase(4+len(L))
    SPRs.SetStackCounter(4+len(L))
    SPRs.SetStackLimit(54+len(L))
    return Mem
def AllocateProcessToMemory(Memory,Filename): #Placeholder for the future
    return Memory
def ReadMemory(Memory,i): # returns the contents of our memory in the ith index
    return Memory[i]
def MakeGPRegisters(): #Creates 16 registers used for GPRs
    R = []
    for i in range(16):
        R.append(Register(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
    return R
def MakeSPRegisters():
    SpecialPR = SpecialPurposeRegisters()
    return SpecialPR
def PrintGPR(R): #Prints the contents of our set of 16 Registers (Meant for GPRs but can be used for SPRs)
        print("R0 : " + str(R[0])  + "    R1 :" + str(R[1]) +  "    R2 :" + str(R[2])  + "    R3 :" + str(R[3]))
        print("R4 : " + str(R[4])  + "    R5 :" + str(R[5]) +  "    R6 :" + str(R[6])  + "    R7 :" + str(R[7]))
        print("R8 : " + str(R[8])  + "    R9 :" + str(R[9]) +  "    R10:" + str(R[10]) + "    R11:" + str(R[11]))
        print("R12: " + str(R[12]) + "    R13:" + str(R[13]) + "    R14:" + str(R[14]) + "    R15:" + str(R[15]))
        print()



GPR = MakeGPRegisters()                 #General Purpose Registers Created
SPR = MakeSPRegisters()                 #Special Purpose Registers Created
Memory = MakeMemory("p0.txt",SPR)       #Memory Created, Data Copied to Memory, SPRs Adjusted accordingly

PC = 0                                #Program Counter Created
IR = IntToByte(SPR.GetCodeBase())                #Instruction Register Created
END = Byte(1,1,1,1,0,0,1,1)           #The value of IR at which Execution will STOP

while ByteToInt(IR) != ByteToInt(END): # Fetch Execute Loop, ends when END value in IR

    PrintGPR(GPR)
    MAR = SPR.GetCodeCounter()
    IR = ReadMemory(Memory, MAR)

    # the hexadecimal opcodes have been converted to int for the conditional statements
    # eg MOVI = 30 in hex but 48 in decimal

    if(ByteToInt(IR)==48):         #MOVI
        RegCode =  ByteToInt(ReadMemory(Memory,MAR+1))                                        #Checks which Register to Address
        Num = 256*ByteToInt(ReadMemory(Memory,MAR+2)) + ByteToInt(ReadMemory(Memory,MAR+3))   #Gets Value to insert in Register
        if (Num > 32768):                                                                     #Checks Overflow
            SPR.SetFlagOverflow(1)
        GPR[RegCode] = IntToRegister(Num)                                                     #Executes MOVI
        SPR.SetCodeCounter(SPR.GetCodeCounter()+4)
        PC += 4

    elif(ByteToInt(IR)==25):      #MUL
        RegCode1 =  ByteToInt(ReadMemory(Memory,MAR+1))                                           #Gets Index of Register 1
        RegCode2 =  ByteToInt(ReadMemory(Memory,MAR+2))                                           #Gets Index of Register 2
        GPR[RegCode1] = IntToRegister(RegisterToInt(GPR[RegCode1])*RegisterToInt(GPR[RegCode2]))  #Executes MUL
        SPR.SetCodeCounter(SPR.GetCodeCounter() + 3)
        PC += 3

    #Command Executed, Back to Start of Loop



