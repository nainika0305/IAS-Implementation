
def opcode(instruction):
    if(instruction == 'LOAD -'):
        return '00000010'
    elif(instruction == 'LOAD MQ,M(X)'):
        return '00001001'
    elif instruction=="LOAD MQ":
        return '00001010'
    elif instruction == 'DISC':
        return '01010101'
    elif(instruction == 'JUMP'):
        return '00001111'
    elif(instruction == 'SQRT'):
        return '00110011'
    elif(instruction == 'STOR'):
        return '00100001'
    elif(instruction == 'MUL'):
        return '00001011'
    elif(instruction == 'SUB'):
        return '00000110'
    elif(instruction == 'ADD'):
        return '00000101'
    elif(instruction == 'HALT'):
        return '00000000'
    elif(instruction == 'DIV'):
        return '00001100'
    else:
        return None
    
def convert_binary(x, my_opcode):
    x=int(x)
    binary_num=bin(x)
    binary_lst=list(binary_num[2:])
    n= len(binary_lst)

    if my_opcode=="01010101":
        for i in range(4,n,-1):
            binary_lst.insert(0,'0')    
    else:
        for i in range(12,n,-1):
            binary_lst.insert(0,'0')
    
    return "".join(binary_lst)



def mach_lang_prog(mach_lang):
    print("type the commands:")
    zeroes="00000000000000000000"
    while(1):
        ins_list=list(input("").split())
        if (ins_list[0] == "EXIT"): #EXIT 
            break
        else:
            #special for jump 
            if(ins_list[0] == "JUMP"): #JUMP +
                op=opcode("JUMP")
                binary=convert_binary(ins_list[2][2:5], op)
                address=op+binary+zeroes
            #lhs only 
            elif(len(ins_list)==2):
                if(ins_list[0]=="DISC"): #DISC 
                    op=opcode("DISC")
                    mem_a=ins_list[1][2] #m[0] ka 0 
                    mem_b=ins_list[1][7] #1
                    mem_c=ins_list[1][12] #2
                    binary=convert_binary(mem_a,op)+convert_binary(mem_b,op)+convert_binary(mem_c,op)
                    address=op+binary+zeroes               
                elif(ins_list[0]=="LOAD" and ins_list[1][0:4]=="MQ,M"): #LOAD MQ,MX
                    op=opcode("LOAD MQ,M(X)")
                    binary=convert_binary(ins_list[1][5],op)
                    address=op+binary+zeroes
                elif(ins_list[0]=="LOAD" and ins_list[1][0:2]=="MQ"): #LOAD MQ
                    op=opcode("LOAD MQ")
                    binary=convert_binary(ins_list[1][5],op)
                    address=op+binary+zeroes
                else:
                    op=opcode(ins_list[0]) #STOR M[x]
                    str1=ins_list[1] 
                    binary=convert_binary(str1[2],op)
                    address=op+binary+zeroes
            #lhs and rhs 
            elif(len(ins_list)==4):
                if(ins_list[1][0]=="-"): #LOAD-M[x]
                    op=opcode("LOAD -")
                    binary=convert_binary(ins_list[1][3],op)
                    address=op+binary
                    op=opcode(ins_list[2])
                    binary=convert_binary(ins_list[3][2],op)
                    address=address+op+binary
                elif (ins_list[2]=="LOAD" and ins_list[3]=="MQ"): ## lhs , load mq 
                    op=opcode(ins_list[0])
                    binary=convert_binary(ins_list[1][2],op)
                    address=op+binary
                    op= opcode("LOAD MQ")
                    binary= "000000000000"
                    address=address+op+binary
                elif (ins_list[1][1]=="-"):  #LOAD -Mx
                    op= opcode("LOAD -")
                    binary = convert_binary(ins_list[1][3],op)
                    address= op+binary
                    op=opcode(ins_list[2])
                    binary=convert_binary(ins_list[3][2],op)
                    address=address+op+binary
                else:
                    op=opcode(ins_list[0]) 
                    binary=convert_binary(ins_list[1][2],op)
                    address=op+binary
                    op=opcode(ins_list[2])
                    binary=convert_binary(ins_list[3][2],op)
                    address=address+op+binary
        mach_lang.append(address)
    print("The machine language program")
    for i in mach_lang:
        print(i, end="")
    print("\n")
    return mach_lang








