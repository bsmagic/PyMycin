import math
from sys import stderr

TRUE =1 #定义返回值
FALSE= 0
FACT_LENGTH =9  #'''前提与结论总数'''
PRMS_LENGTH= 2  #'''每条规则的前提个数'''
PREMISE= 7      #'''前提数量''' 
RULE_LENGTH = 4  #'''规则数量'''
LIMIT= 0.5      #'''结论阈值'''
AND =1         #'''规则前提逻辑关系'''
OR =0
VH =0.9       #'''规则前提可信度初始化'''
H =0.7
M =0.5
#double Rule_CF[RULE_LENGTH]
Rule_CF=[0.0]*RULE_LENGTH
Str=["E1","E2","E3","E4","E5","E6","E7","H1","H","\0"]
#char *Str[FACT_LENGTH+1]={}; 
Fuzz=[]*6
Input=[]*6
Repeat=-111
#double(*Fuzz[6])(int)
#void (*Input[6])(int)
#char *Repeat="-111";   #'''重新输入变量'''

#'''知识表达'''
#int Sign[FACT_LENGTH]={0,0,0,0,0,0,0,0,1}
Sign=[0,0,0,0,0,0,0,0,1]
Rulep=[[1,2,0],[4,5,0],[6,8,0],[3,7,0]]
Rulec=[[9,'AND'],[8,'AND'],[7,'AND'],[9,'OR']]
#int Rulep[RULE_LENGTH][PRMS_LENGTH+1]={{1,2,0},{4,5,0},{6,8,0},{3,7,0}
#int Rulec[RULE_LENGTH][2]={{9,AND},{8,AND},{7,AND},{9,OR}
def Input1(i):
     print("按q或Q退出")
     print("请输入事实:E[",i,"的可信度")
     print("可信度为：") 
     print(" [1]高")
     print(" [2]中")
     print(" [3]低")

def Input2(i=3):
     print("按q或Q退出")
     print("请输入事实 E[",i,"]数值[30-45]：")  

def Input3(i=4):
     print("按q或Q退出")
     print("请输入事实 E[",i,"]数值[60,160]：")

def Fuzz1(self,sign):
    switcher = {
        1: VH,
        2: H,
        3: M,
    }
    if(sign in switcher.keys()):
        return switcher[sign]
    else:
        stderr.write("请重新输入！")
        return Repeat    


def Fuzz2(self, sign):
    if sign<30 or sign>45:
        stderr.write("请重新输入！")
        return Repeat
    i=(sign-37.0)/9.0
    return i if i>0 else -i

def Fuzz3(self, sign):
    if sign<60 or sign>160:
        stderr.write("请重新输入！")
        return Repeat

    i=(sign-60.0)/100.0
    return(i)

def DefFuncArray(self):
    for i in range(4):
        Fuzz[i]=Fuzz1
    Fuzz[4]=Fuzz2
    Fuzz[5]=Fuzz3

def DefInput(self):
    for i in range(4):
        Input[i]=Input1
    Input[4]=Input2
    Input[5]=Input3

#'''定义规则的可信度'''
def DefRule_CF(self):
    Rule_CF[0]=0.9
    Rule_CF[1]=1.0
    Rule_CF[2]=0.9
    Rule_CF[3]=0.9

