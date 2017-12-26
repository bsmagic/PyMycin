#'''推理机头文件inference.h'''
#include "kb.h"
import kb.h

class fact(object):  #'''定义事实类''' 
    def __init__(self,Num,NamInput):
        self.Number=Num    #'''事实编号'''
        self.Active=False  #'''记录事实的激活状态'''
        self.CF=0  #'''事实可信度'''
        self.Sign=0  #'''输出标记'''
        self.Name=NamInput  #'''事实内容'''
    def Fuzz(i):   #'''定义可信度模糊函数'''
        pass
###        
    def Input(int):
        pass
    def GetName():
        return self.Name    
    def GetNumber():
        return self.Number
    def GetAct():
        return self.Active
    def PutAct(Act):
        self.Active=Act
    def PutFunc(f):
        self.Fuzz=f
    def GetCF():
        return self.CF
    def PutCF(i):
        if isinstance(i,int):
            self.CF=self.Fuzz(i)
            return self.CF
        else:
            self.CF=i    
    def PutSign(i):
            self.Sign=i        
    def GetSign():
        return self.Sign

    #   private:
    #           int Number;    '''事实编号'''
    #           char *Name;    '''事实内容'''
    #           double CF;     '''事实可信度'''
    #           int Active;    '''记录事实的激活状态'''
    #           int Sign;      '''输出标记'''
    #           double (*Fuzz)(int i); '''定义可信度模糊函数'''
    #  public:
            # void (*Input)(int);  '''输入函数'''
            #  fact(int Num, *L)  '''初始化事实'''
            #           Name=(char*) malloc(strlen(L)+1)
            #           strcpy(Name,L)
            #           Number=Num
            #           Active=FALSE
            #           CF=0
            #           Sign=0
            #  char* GetName()
            #        char *L
            #        L=new char(strlen(Name)+1)
            #        if L!=NULL) strcpy(L,Name:
            #        return L

        #     int GetNumber(){return Number;
        #     int GetAct(){return Active;
        #     void PutAct( int Act){Active=Act;
        #     void PutFunc(double(*f)(int)){Fuzz=f;
        #     double GetCF(){return CF;
        #     int PutCF(int i)   '''处理用户输入'''
        #         CF=Fuzz(i)
        #         return CF

        #     void PutCF(double d)  '''置可信度计算结果标记'''
        #          CF=d

        #     void PutSign(int i)   '''置输出标记'''
        #          Sign=i

        #     int GetSign(){return Sign;

#fact *Fact[FACT_LENGTH+1]
Fact=[]*(FACT_LENGTH+1)
#for i in range(FACT_LENGTH+1):
#    Fact.append()

class rule(object):   #'''定义规则类'''
    #   private:
    #           char *Name;     '''规则名'''
    #           int List[PRMS_LENGTH]; '''同一规则的所有前提链表'''
    #           int Logic;      '''定义规则间的逻辑关系'''
    #           int Conc;       '''规则结论'''
    #           double RCFi;    '''规则可信度'''
    #   public:
    #????         rule *Next
    #         rule( int P[], C[], Rule_Cf)
    #         ~rule()
    #         int Query()
    #         char *GetName(){return Name;
    #         double CF()
    def GetConc():
        return self.Conc
    def GetName():
        return self.Name
    def __init__(*P,*C,Rule_CF): #'''构造规则函数''' 
        self.Name="Rule Name"   
        self.List[0]=P[0]
        self.List[1]=P[1]
        self.Logic=C[1]
        self.Conc=C[0]
        self.RCFi=Rule_CF    

    def Init(self):  #'''初始化函数'''
        DefFuncArray()
        DefInput()
        DefRule_CF()
        Fact[FACT_LENGTH]=None;   ###???
                

    def __del__(self):  #'''构造释放规则空间函数'''
        #delete Name
        #delete []List

    def Max(a, b): #  '''可信度计算'''
        return a if a>b else b
    def Min(a, b):  
        return b if a>b else a
    def Mix(x, y):
        return(x+y-x*y)

    def Query(): #  '''构造推理函数'''
        int sign=0
        temps=['']*10
        choose=['']*4
        fact* (*temp)=Fact
        while(sign<PRMS_LENGTH)
            for(;(*temp)!=NULL;temp=temp+1)
            if((*temp).GetNumber()==List[sign]) break
            if((*temp)==NULL) return FALSE
            if((*temp).GetAct()>0){sign++;temp=Fact;
            else:
                (*temp).Input((*temp).GetNumber())
                scanf("%s",choose)
                # flushall()
                cout<<endl
                if (strcmp(choose,"q")andstrcmp(choose,"Q"))==0:
                    return TRUE
                if strcmp(itoa(atoi(choose),temps,10),choose)!=0:
                    continue
                if (*temp).PutCF(atoi(choose))==atoi(Repeat):
                    continue
                (*temp).PutAct(TRUE)


        for(temp=Fact;(*temp)!=NULL;temp++)
        if((*temp).GetNumber()==Conc)  break
        if((*temp)==NULL) return FALSE
        (*temp).PutCF(Mix((*temp).GetCF(),CF()))
        (*temp).PutAct(1)
        return FALSE

    def CF():  #'''构造可信度推理函数'''
        if self.Logic:
            i=Min(Fact[List[0]-1].GetCF(),Fact[List[1]-1].GetCF())
            i=i*RCFi
            return i



     

     
