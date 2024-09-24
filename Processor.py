import IMT2023020_IMT2023034_IMT2023059_assembler

MAR=""
IR=""
PC= 0
IBR=""
AC= 0
MQ= 0
MBR= 0
ext= 0 
a, b, c, a_2, dis, root_d, x1, x2=0,0,0,0,0,0,0,0
M = [ a, b, c, a_2, dis, 4, 2, root_d, x1, x2 ]
#equation is ax^2 +bx +c 
#a_2 stores the value of 2a needed for denominator 
#dis stores the value of discriminant 
#x1 and x2 are roots 

def my_operation(op, address):
    global PC 
    global MAR
    global IR
    global IBR
    global MBR
    global AC
    global MQ


    if op=="01010101": #DISC M[x],M[x],M[x] 
        bin_a=address[0:4]
        bin_b=address[4:8]
        bin_c=address[8:12]
        a=M[int(bin_a,2)]
        b=M[int(bin_b,2)]
        c=M[int(bin_c,2)]
        discriminant= (b**2) - (4*a*c)        
        AC = discriminant
        print(f"AC={AC}")
        print("\n")
    elif op=="00000010": #LOAD -M[x]
        MBR= M[int(address,2)]
        AC= -MBR
        print(f"AC={AC}")
        print("\n")
    elif op=="00100001": #STOR M[x]
        MBR=AC
        M[int(address,2)] = MBR
        print(f"AC={AC}")
        print("\n")
    elif op=="00110011": #SQRT M[x]
        MBR= M[int(address,2)]
        AC=MBR
        AC=(AC**0.5)
        print(f"AC={AC}")
        print("\n")
    elif op=="00001111": #JUMP 
        if AC>=0:
            PC = int(address,2) - 1
    elif op == '00000101': #ADD M[x]
        MBR = M[int(address, 2)]
        AC = AC + MBR
        print(f'AC = {AC}')                          
        print('\n')
    elif op == '00000110': #SUB M[x]
        MBR = M[int(address,2)]
        AC = AC-MBR                                   
        print(f"AC = {AC}")
        print("\n")
    elif op == "00001100": #DIV M[x]
        MBR = M[int(address,2)]
        MQ = AC / MBR
        AC = AC % MBR                                  
        print(f'AC ={AC}')
        print(f'MQ ={MQ}')
        print("\n")
    elif op == '00001011': #MUL M[x]
        MBR = M[int(address,2)]
        AC = MBR 
        MQ = AC * MQ
        print(f'AC = {AC}')
        print(f'MQ = {MQ}')
        print("\n")
    elif op=="00001001": #LOAD MQ,M[x]
        MBR = M[int(address,2)]
        MQ= MBR 
        print(f"MQ = {MQ}")
        print("\n")
    elif op=="00001010": #LOAD MQ 
        AC=MQ
        print(f"MQ = {MQ}")
        print(f'AC = {AC}')
        print("\n")
    elif op=="00000010": #LOAD -M[x]
        AC = -M[int(address,2)]
        print(f'AC = {AC}')
        print("\n")
    
    
def decode_instruction(word): #word is a string , stored at m[pc]
    global PC 
    global MAR
    global IR
    global IBR
    global MBR
    global AC
    global MQ

    #assume pc set to address of instrucion 
    MAR=str(PC)
    
    MBR=word #first the word goes to MBR from M[MAR]
    
    #transfer the word present in the MBR
    left_instruction = MBR[0:20]
    left_opcode = MBR[0:8]
    left_address = MBR[8:20]
    right_instruction = MBR[20:40]
    right_opcode = MBR[20:28]
    right_address = MBR[28:40]
    
    IR = left_opcode #From MBR , left address opcode goes to IR 
    MAR = left_address #from MBR , left address goes to MAR
    IBR = right_instruction #from MBR right instruction goes to IBR 

    my_operation(IR,MAR)#execute left instruction 

    IR = IBR[0:8] #from IBR , load right opcode in IR 
    MAR = IBR[8:20] #from IBR , load right address in MAR

    my_operation(IR, MAR) #execute right instruction

    PC= int(PC) + 1 #increment PC to point to next word's memory location 


print('''Enter the values of a , b , c corresponding to ax^2 + bx +c :
      note: a<=15, b<=15, c<=15''')
a_in= int(input("a:"))
b_in= int(input("b:"))
c_in= int(input("c:"))

M[0]=a_in
M[1]=b_in
M[2]=c_in
PC=496 
i=0
mach_lang=[]
mach_lang = IMT2023020_IMT2023034_IMT2023059_assembler.mach_lang_prog(mach_lang)

i=0
while (1): 
    if PC==510:
        break
    if mach_lang[i]=="00000000000000000000000000000000000000000" or PC==499: #HALT
        break

    decode_instruction(mach_lang[i])
    print(f"PC={PC}")
    print("\n\n") 
    i+=1

if (PC==499):
    print("No real roots exist since d<0") # if d<0 
else:
    print(f"The roots are {M[8]} and {M[9]}")  #roots are stored in these memory locations  




