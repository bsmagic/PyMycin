import os
import inference
def main(self):
    #rule *Rule,*R    
    #int i=0
    Init()
    #while(*Str[i]) #   '''激活事实对象集'''
    for i in range(len(Fact)):
        Fact[i]=fact((i+1),Str[i])
        Fact[i].PutSign(Sign[i])
    for s in range(PREMISE):
        Fact[s].Input=Input[s]
        Fact[s].PutFunc(Fuzz[s])

    Rule=None
    for i in range(RULE_LENGTH,0,-1): #'''激活规则对象集'''
        if(i<0): return FALSE        
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
    os.system("Pause")
    return TRUE

if __name__=='__main__':
    main() 
 

