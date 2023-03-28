import xml.etree.ElementTree as gfg 
import os 
import re

total_insts=0
num_of_integer=0
num_of_loadstore=0
num_of_branch=0
num_of_len1=0

# def GenerateXMLforASM(srcs_num=1, srcs_mem_flag=False, srcs_mem_idx=[], srcs_mem_base=False, srcs_mem_disp=False, srcs_mem_index=False,
#                       dsts_num=1, dsts_mem_flag=False, dsts_mem_idx=[], dsts_mem_base=False, dsts_mem_disp=False, dsts_mem_index=False):
def GenerateXMLforASM(**p):
    root = gfg.Element("block")

    inst = gfg.Element("inst")
    root.append(inst)

    opcode = gfg.SubElement(inst, "opcode")
    opcode.text = "1"

    srcs = gfg.SubElement(inst, "srcs")
    if p["srcs_num"]>=1: # srcs的第一个源操作数
        srcs_opreand1 =gfg.SubElement(srcs, "operand")
        if p["srcs_mem_flag"] and (1 in p["srcs_mem_idx"]): # 第一个源操作数是访存
            srcs_opreand1_mem = gfg.SubElement(srcs_opreand1, "mem")
            srcs_opreand1_mem_base = gfg.SubElement(srcs_opreand1_mem, "base")
            srcs_opreand1_mem_base.text = "1"
            if p["srcs_mem_disp"]:
                srcs_opreand1_mem_disp = gfg.SubElement(srcs_opreand1_mem, "disp")
                srcs_opreand1_mem_disp.text = "1"
            elif p["srcs_mem_index"]:
                srcs_opreand1_mem_index = gfg.SubElement(srcs_opreand1_mem, "index")
                srcs_opreand1_mem_index.text = "1"
        else:
            srcs_opreand1.text = "1"

    if p["srcs_num"]>=2: # srcs的第二个源操作数
        srcs_opreand2 =gfg.SubElement(srcs, "operand")
        if p["srcs_mem_flag"] and (2 in p["srcs_mem_idx"]): # 第二个源操作数是访存
            srcs_opreand2_mem = gfg.SubElement(srcs_opreand2, "mem")
            srcs_opreand2_mem_base = gfg.SubElement(srcs_opreand2_mem, "base")
            srcs_opreand2_mem_base.text = "1"
            if p["srcs_mem_disp"]:
                srcs_opreand2_mem_disp = gfg.SubElement(srcs_opreand2_mem, "disp")
                srcs_opreand2_mem_disp.text = "1"
            elif p["srcs_mem_index"]:
                srcs_opreand2_mem_index = gfg.SubElement(srcs_opreand2_mem, "index")
                srcs_opreand2_mem_index.text = "1"
        else:
            srcs_opreand2.text = "1"

    if p["srcs_num"]>=3: # srcs的第三个源操作数
        srcs_opreand3 =gfg.SubElement(srcs, "operand")
        if p["srcs_mem_flag"] and (3 in p["srcs_mem_idx"]): # 第三个源操作数是访存
            srcs_opreand3_mem = gfg.SubElement(srcs_opreand3, "mem")
            srcs_opreand3_mem_base = gfg.SubElement(srcs_opreand3_mem, "base")
            srcs_opreand3_mem_base.text = "1"
            if p["srcs_mem_disp"]:
                srcs_opreand3_mem_disp = gfg.SubElement(srcs_opreand3_mem, "disp")
                srcs_opreand3_mem_disp.text = "1"
            elif p["srcs_mem_index"]:
                srcs_opreand3_mem_index = gfg.SubElement(srcs_opreand3_mem, "index")
                srcs_opreand3_mem_index.text = "1"
        else:
            srcs_opreand3.text = "1"

    if p["srcs_num"]>=4: # srcs的第四个源操作数
        srcs_opreand4 =gfg.SubElement(srcs, "operand")
        if p["srcs_mem_flag"] and (4 in p["srcs_mem_idx"]): # 第四个源操作数是访存
            srcs_opreand4_mem = gfg.SubElement(srcs_opreand4, "mem")
            srcs_opreand4_mem_base = gfg.SubElement(srcs_opreand4_mem, "base")
            srcs_opreand4_mem_base.text = "1"
            if p["srcs_mem_disp"]:
                srcs_opreand4_mem_disp = gfg.SubElement(srcs_opreand4_mem, "disp")
                srcs_opreand4_mem_disp.text = "1"
            elif p["srcs_mem_index"]:
                srcs_opreand4_mem_index = gfg.SubElement(srcs_opreand4_mem, "index")
                srcs_opreand4_mem_index.text = "1"
        else:
            srcs_opreand4.text = "1"
    


    dsts = gfg.SubElement(inst, "dsts")
    if p["dsts_num"]>=1: # dsts的第一个目的操作数
        dsts_opreand1 =gfg.SubElement(dsts, "operand")
        if p["dsts_mem_flag"] and (1 in p["dsts_mem_idx"]):
            dsts_opreand1_mem = gfg.SubElement(dsts_opreand1, "mem")
            dsts_opreand1_mem_base = gfg.SubElement(dsts_opreand1_mem, "base")
            dsts_opreand1_mem_base.text = "1"
            if p["dsts_mem_disp"]:
                dsts_opreand1_mem_disp = gfg.SubElement(dsts_opreand1_mem, "disp")
                dsts_opreand1_mem_disp.text = "1"
            elif p["dsts_mem_index"]:
                dsts_opreand1_mem_index = gfg.SubElement(dsts_opreand1_mem, "index")
                dsts_opreand1_mem_index.text = "1"
        else:
            dsts_opreand1.text = "1"

    if p["dsts_num"]>=2: # dsts的第二个目的操作数
        dsts_opreand2 =gfg.SubElement(dsts, "operand")
        if p["dsts_mem_flag"] and (2 in p["dsts_mem_idx"]):
            dsts_opreand2_mem = gfg.SubElement(dsts_opreand2, "mem")
            dsts_opreand2_mem_base = gfg.SubElement(dsts_opreand2_mem, "base")
            dsts_opreand2_mem_base.text = "1"
            if p["dsts_mem_disp"]:
                dsts_opreand2_mem_disp = gfg.SubElement(dsts_opreand2_mem, "disp")
                dsts_opreand2_mem_disp.text = "1"
            elif p["dsts_mem_index"]:
                dsts_opreand2_mem_index = gfg.SubElement(dsts_opreand2_mem, "index")
                dsts_opreand2_mem_index.text = "1"
        else:
            dsts_opreand2.text = "1"


    tree = gfg.ElementTree(root)
    xml_str = gfg.tostring(root, encoding='unicode')
    return xml_str


def AnalyzeAsm(asm_code, asm_flags):
    global num_of_integer
    global num_of_loadstore
    global num_of_branch
    global num_of_len1
    if len(asm_code)>1:
        if len(asm_flags)==1 and asm_flags[0]=='IsInteger':
            num_of_integer = num_of_integer+1
            srcs_num=len(asm_code)-2
            srcs_mem_flag=False
            srcs_mem_idx=[] # 指示访存是第几个src
            srcs_mem_base=False # 指示访存中有base
            srcs_mem_disp=False # 指示访存中有disp
            srcs_mem_index=False

            dsts_num=1
            dsts_mem_flag=False
            dsts_mem_idx=[]
            dsts_mem_base=False
            dsts_mem_disp=False
            dsts_mem_index=False
        elif 'IsStore' in asm_flags: # store指令dst是访存
            assert(asm_flags[0]=='IsInteger')
            num_of_loadstore=num_of_loadstore+1
            if len(asm_code)==3:
                if 'u' in asm_code[0]: # 拥有两个dsts
                    srcs_num=3
                    srcs_mem_flag=False
                    srcs_mem_idx=[] # 指示访存是第几个src
                    srcs_mem_base=False # 指示访存中有base
                    srcs_mem_disp=False # 指示访存中有disp
                    srcs_mem_index=False

                    dsts_num=2
                    dsts_mem_flag=True
                    dsts_mem_idx=[1]
                    dsts_mem_base=True
                    dsts_mem_disp=True
                    dsts_mem_index=False
                else:
                    srcs_num=3
                    srcs_mem_flag=False
                    srcs_mem_idx=[] # 指示访存是第几个src
                    srcs_mem_base=False # 指示访存中有base
                    srcs_mem_disp=False # 指示访存中有disp
                    srcs_mem_index=False

                    dsts_num=1
                    dsts_mem_flag=True
                    dsts_mem_idx=[1]
                    dsts_mem_base=True
                    dsts_mem_disp=True
                    dsts_mem_index=False
            elif len(asm_code)==4:
                assert('x' in asm_code[0])
                if 'u' in asm_code[0]: # 拥有两个dsts
                    srcs_num=3 # RA, RB, RS
                    srcs_mem_flag=False
                    srcs_mem_idx=[] # 指示访存是第几个src
                    srcs_mem_base=False # 指示访存中有base
                    srcs_mem_disp=False # 指示访存中有disp
                    srcs_mem_index=False

                    dsts_num=2
                    dsts_mem_flag=True
                    dsts_mem_idx=[1]
                    dsts_mem_base=True
                    dsts_mem_disp=False
                    dsts_mem_index=True
                else:
                    srcs_num=3 # RA, RB, RS
                    srcs_mem_flag=False
                    srcs_mem_idx=[] # 指示访存是第几个src
                    srcs_mem_base=False # 指示访存中有base
                    srcs_mem_disp=False # 指示访存中有disp
                    srcs_mem_index=False

                    dsts_num=1
                    dsts_mem_flag=True
                    dsts_mem_idx=[1]
                    dsts_mem_base=True
                    dsts_mem_disp=False
                    dsts_mem_index=True
            else: assert(0)
        elif 'IsLoad' in asm_flags: # load指令的srcs有访存
            assert(asm_flags[0]=='IsInteger')
            num_of_loadstore=num_of_loadstore+1
            if len(asm_code)==3: # 有base和disp的
                if 'u' in asm_code[0]: # 拥有两个dsts 且有3个srcs(一个寄存器, 一个立即数, 一个mem)
                    srcs_num=3
                    srcs_mem_flag=True # 指示在srcs中有访存
                    srcs_mem_idx=[1] # 指示访存是第几个src
                    srcs_mem_base=True # 指示访存中有base
                    srcs_mem_disp=True # 指示访存中有disp
                    srcs_mem_index=False

                    dsts_num=2
                    dsts_mem_flag=False
                    dsts_mem_idx=[]
                    dsts_mem_base=False
                    dsts_mem_disp=False
                    dsts_mem_index=False
                else:
                    srcs_num=1
                    srcs_mem_flag=True # 指示在srcs中有访存
                    srcs_mem_idx=[1] # 指示访存是第几个src
                    srcs_mem_base=True # 指示访存中有base
                    srcs_mem_disp=True # 指示访存中有disp
                    srcs_mem_index=False

                    dsts_num=1
                    dsts_mem_flag=False
                    dsts_mem_idx=[]
                    dsts_mem_base=False
                    dsts_mem_disp=False
                    dsts_mem_index=False
            elif len(asm_code)==4: # 就像 ldx, RT, RA, RB（好像带了x字母的就是这样）
                assert('x' in asm_code[0])
                if 'u' in asm_code[0]: # 拥有两个dsts 且有3个srcs(两个寄存器, 一个mem)
                    srcs_num=3
                    srcs_mem_flag=True # 指示在srcs中有访存
                    srcs_mem_idx=[1] # 指示访存是第几个src
                    srcs_mem_base=True # 指示访存中有base
                    srcs_mem_disp=True # 指示访存中有disp
                    srcs_mem_index=False

                    dsts_num=2
                    dsts_mem_flag=False
                    dsts_mem_idx=[]
                    dsts_mem_base=False
                    dsts_mem_disp=False
                    dsts_mem_index=False
                else:
                    srcs_num=1
                    srcs_mem_flag=True
                    srcs_mem_idx=[1]
                    srcs_mem_base=True
                    srcs_mem_disp=False
                    srcs_mem_index=True

                    dsts_num=1 # TODO: 有些情况还有别的隐藏dst，比如ldux指令(好像有u的就是)
                    dsts_mem_flag=False
                    dsts_mem_idx=[]
                    dsts_mem_base=False
                    dsts_mem_disp=False
                    dsts_mem_index=False
            else: assert(0)
        elif 'IsControl' in asm_flags:
            assert(asm_code[0][0]=='b')
            num_of_branch=num_of_branch+1

            # file = open("test2.txt", 'a')
            # file.write(" ".join(asm_code)+'\t'+"|".join(asm_flags)+'\n')
            if asm_code[0] in ['b','ba','bl','bla']: pass
            elif asm_code[0] in ['bc','bca','bcl','bcla','blt','bne','bdnz']: pass
            elif asm_code[0] in ['bclr','bclrl','bltlr','bnelr','bdnzlr']: pass
            elif asm_code[0] in ['bcctr','bcctrl','bltctr','bnectr']: pass
            else: assert(0)
            srcs_num=1
            srcs_mem_flag=False
            srcs_mem_idx=[] # 指示访存是第几个src
            srcs_mem_base=False # 指示访存中有base
            srcs_mem_disp=False # 指示访存中有disp
            srcs_mem_index=False

            dsts_num=1
            dsts_mem_flag=False
            dsts_mem_idx=[]
            dsts_mem_base=False
            dsts_mem_disp=False
            dsts_mem_index=False
        else: assert(0)
        asm_xml_str = \
        GenerateXMLforASM(srcs_num=srcs_num, srcs_mem_flag=srcs_mem_flag, srcs_mem_idx=srcs_mem_idx, srcs_mem_base=srcs_mem_base, srcs_mem_disp=srcs_mem_disp, srcs_mem_index=srcs_mem_index,
                        dsts_num=dsts_num, dsts_mem_flag=dsts_mem_flag, dsts_mem_idx=dsts_mem_idx, dsts_mem_base=dsts_mem_base, dsts_mem_disp=dsts_mem_disp, dsts_mem_index=dsts_mem_index)
        return asm_xml_str
    elif len(asm_code)==1:
        num_of_len1 = num_of_len1+1
        if asm_code[0] == 'nop':
            srcs_num=1
            srcs_mem_flag=False
            srcs_mem_idx=[] # 指示访存是第几个src
            srcs_mem_base=False
            srcs_mem_disp=False
            srcs_mem_index=False

            dsts_num=1
            dsts_mem_flag=False
            dsts_mem_idx=[]
            dsts_mem_base=False
            dsts_mem_disp=False
            dsts_mem_index=False
            asm_xml_str = \
            GenerateXMLforASM(srcs_num=srcs_num, srcs_mem_flag=srcs_mem_flag, srcs_mem_idx=srcs_mem_idx, srcs_mem_base=srcs_mem_base, srcs_mem_disp=srcs_mem_disp, srcs_mem_index=srcs_mem_index,
                            dsts_num=dsts_num, dsts_mem_flag=dsts_mem_flag, dsts_mem_idx=dsts_mem_idx, dsts_mem_base=dsts_mem_base, dsts_mem_disp=dsts_mem_disp, dsts_mem_index=dsts_mem_index)
            return asm_xml_str
        elif  asm_code[0] =='dcbt': pass
        elif  asm_code[0] =='sc': pass
        elif  asm_code[0] =='isync':pass
        elif  asm_code[0] =='synco':pass
        elif  asm_code[0] =='dcbtst':pass
        else:
            num_of_len1 = num_of_len1-1
            file = open("test2.txt", 'a')
            file.write(" ".join(asm_code)+'\t'+"|".join(asm_flags)+'\n')
            assert(0)
    else: assert(0)
    return '1'


def ReadLog(fileName):
    global total_insts
    with open(fileName) as log:
        for lineID, line in enumerate(log):
            if lineID <= 20000:
                if lineID % 2 == 0: # 偶数行 decode
                    decode_line = line
                    decode_parts = decode_line.split(':')
                    decode_tick = decode_parts[0]
                    hex = decode_parts[4]
                    # decode_tick = re.match("\s*\d+", decode_line).group(0) # 在开头匹配tick数
                    # hex = re.search("0x[0-9a-z]{8}", decode_line).group(0) # 匹配decode line中的编码hex形式
                    # print(hex, end="")
                if lineID % 2 == 1: # 奇数行 exec
                    exec_line = line
                    exec_parts = exec_line.split(":")
                    exec_tickt = exec_parts[0]
                    assert(decode_tick == exec_tickt)
                    assert(len(exec_parts) == 7)

                    asm_code = exec_parts[4]
                    asm_code_parts = [i.replace(',', '') for i in list(filter(lambda x: x != '', asm_code.split(" ")))] # asm_parts是汇编字符串的各个部分, 且去除了逗号
                    assert(len(asm_code_parts)<=6)

                    asm_flags=exec_parts[-1].split(" ")[-1]
                    assert(asm_flags[0:6]=='flags=')
                    asm_flags=asm_flags[7:-2].split('|')
                    assert(len(asm_flags)<=5)

                    asm_xml_str = AnalyzeAsm(asm_code=asm_code_parts, asm_flags=asm_flags)
                    file = open("test.txt", 'a')
                    file.write(asm_code+'\t'+asm_xml_str+'\n')

                    total_insts=total_insts+1
                    pass


if __name__ == "__main__":
    file1=open('test.txt', 'w')
    file1.write('1')
    file1.close()
    file2=open('test2.txt', 'w')
    file2.write('2')
    file2.close()
    os.remove(r'test.txt')
    os.remove(r'test2.txt')


    ReadLog("log.txt")
    print("total_insts:{}, total_insts:{}, num_of_loadstore:{}, num_of_branch:{}, num_of_len1{}, ratio:{}".\
          format(total_insts, num_of_integer, num_of_loadstore, num_of_branch, num_of_len1, \
                 (num_of_integer+num_of_loadstore+num_of_branch+num_of_len1)/total_insts))
