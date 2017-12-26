from sys import stderr
#########################
TRUE = 1 #定义返回值
FALSE = 0
FACT_LENGTH = 9  #'''前提与结论总数'''
PRMS_LENGTH = 2  #'''每条规则的前提个数'''
PREMISE = 7 #'''前提数量''' 
RULE_LENGTH = 4  #'''规则数量'''
LIMIT = 0.5      #'''结论阈值'''
AND = 1         #'''规则前提逻辑关系'''
OR = 0
VH = 0.9       #'''规则前提可信度初始化'''
H = 0.7
M = 0.5
#double Rule_CF[RULE_LENGTH]
Rule_CF = [0.0]*(RULE_LENGTH+1)
Str = ["E1", "E2", "E3", "E4", "E5",
"E6", "E7", "H1", "H", "\0"]
Fuzz = [None]*10
Input = [None]*PREMISE
Repeat = -111   #'''重新输入变量'''

#'''知识表达'''
Sign = [0,0,0,0,0,0,0,0,1]
Rulep = [[1,2,0],[4,5,0],[6,8,0],[3,7,0]]
Rulec = [[9,'AND'],[8,'AND'],[7,'AND'],[9,'OR']]
##
def Max(a, b): #  '''可信度计算'''
    return a if a>b else b
def Min(a, b):  
    return b if a>b else a
def Mix(x, y):
    return (x+y-x*y)

class fact(object):  #'''定义事实类''' 
    def __init__(self,Num,NamInput):
        self.Number=Num    #'''事实编号'''
        self.Active=False  #'''记录事实的激活状态'''
        self.CF=0  #'''事实可信度'''
        self.SignNum=0  #'''输出标记'''
        self.Name=NamInput  #'''事实内容'''
    def Fuzz(i):   #'''定义可信度模糊函数'''
        pass
###        
    def Input(self,int):
        pass
    def GetName(self):
        return self.Name    
    def GetNumber(self):
        return self.Number
    def GetAct(self):
        return self.Active
    def PutAct(self,Act):
        self.Active=Act
    def PutFunc(self,f):
        self.Fuzz=f
    def GetCF(self):
        return self.CF
    def PutCF(self,i):
        if isinstance(i,int):
            self.CF=self.Fuzz(i)
            return self.CF
        else:
            self.CF=i    
    def PutSign(self,i):
            self.Sign =i        
    def GetSign(self):
        return self.Sign



class rule(object):   #'''定义规则类'''

    def GetConc():
        return self.Conc
    def GetName():
        return self.Name
    def __init__(self,P,C,Rule_CF_Val):  
         #'''构造规则函数''' 
        #print(P)
        self.List=[None]*2
        self.Name="Rule Name"   
        self.List[0]=P[0]
        self.List[1]=P[1]
        self.Logic=C[1]
        self.Conc=C[0]
        self.RCFi=Rule_CF_Val
        self.Next=None    

               

    def __del__(self):  #'''构造释放规则空间函数'''
        #delete Name
        #delete []List
        pass

    def Query(self):  #  '''构造推理函数'''
        sign=0
        temps=['']*10
        choose=""
        #fact* (*temp)=Fact
        temp=Fact
        while (sign<PRMS_LENGTH):
            #for(;(*temp)!=NULL;temp=temp+1)
            for index in range(len(temp)):
                if(temp[index].GetNumber()==self.List[sign]): break
            if(temp[index]==None): return FALSE
            if(temp[index].GetAct()>0):
                sign=sign+1
                temp=Fact
            else:
                temp[index].Input(temp[index].GetNumber())
                choose=input() #scanf("%s",choose)
                # flushall()
                print()                
                if choose.lower()=="q":
                    return TRUE
                if str(int(choose))!= choose :
                    continue
                if temp[index].PutCF(int(choose))==int(Repeat):
                    continue
                temp[index].PutAct(TRUE)
        for index in range(len(temp)):
            if(temp[index].GetNumber()==self.Conc): break
        if(temp[index]==None): return FALSE
        temp[index].PutCF(Mix(temp[index].GetCF(),self.CF()))
        temp[index].PutAct(1)
        return FALSE

    def CF(self):  #'''构造可信度推理函数'''
        if self.Logic:
            i=Min(Fact[self.List[0]-1].GetCF(),Fact[self.List[1]-1].GetCF())
            i=i*self.RCFi
            return i

     
     #################
##
Fact=[fact]*FACT_LENGTH

#########################
def Init():  #'''初始化函数'''
    DefFuncArray()
    DefInput()
    DefRule_CF()


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

def Fuzz1(sign):
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


def Fuzz2(sign):
    if sign<30 or sign>45:
        stderr.write("请重新输入！")
        return Repeat
    i=(sign-37.0)/9.0
    return i if i>0 else -i

def Fuzz3(sign):
    if sign<60 or sign>160:
        stderr.write("请重新输入！")
        return Repeat

    i=(sign-60.0)/100.0
    return(i)

def DefFuncArray():
    for i in range(4):
        Fuzz[i]=Fuzz1
    Fuzz[4]=Fuzz2
    Fuzz[5]=Fuzz3

def DefInput():
    for i in range(4):
        Input[i]=Input1
    Input[4]=Input2
    Input[5]=Input3

#'''定义规则的可信度'''
def DefRule_CF():
    Rule_CF[0]=0.9
    Rule_CF[1]=1.0
    Rule_CF[2]=0.9
    Rule_CF[3]=0.9


def main():
    #rule *Rule,*R    
    #int i=0
    Init()
    #while(*Str[i]) #   '''激活事实对象集'''
    for i in range(len(Fact)):
        Fact[i]=fact((i+1),Str[i])
        #print(Fact[i].GetName())
        Fact[i].PutSign(Sign[i])
    for s in range(PREMISE):
        Fact[s].Input=Input[s]
        Fact[s].PutFunc(Fuzz[s])

    Rule=None
    for i in range(RULE_LENGTH-1,-1,-1): #'''激活规则对象集'''
        if(i<0): return FALSE  
        print(i)      
        R=rule(Rulep[i],Rulec[i],Rule_CF[i])
        R.Next=Rule
        Rule=R

    R=Rule
    while(True):
           if(R.Query()): break
           R=R.Next
           if(not R): break

    #for(i=0;i<FACT_LENGTH;i++)  '''给出结论'''
    for i in range(FACT_LENGTH):
         if Fact[i].GetCF()>LIMIT and Fact[i].GetSign()==1:
                Fact[i].PutSign(0)
                print(" 结论为：")
                print(Fact[i].GetName())
                print(" 其可信度为：")
                print(Fact[i].GetCF())

    print("运行结束。")
    input()
    return TRUE

if __name__=='__main__':
    main() 
 