/*主程序文件expert.cpp*/
#ifndef Expert_H
#define Expert_H
#include <iostream>
#include "inference.h"
using namespace std;
#endif
int main()
{
    rule *Rule,*R;
    int i=0;
    Init();
    while(*Str[i])    /*激活事实对象集*/
    {
                      Fact[i]=new fact((i+1),Str[i]);
                      Fact[i]->PutSign(Sign[i]);
                      i++;
                      }
    for(int s=0;s<PREMISE;s++ )
    {
            Fact[s]->Input=Input[s];
            Fact[s]->PutFunc(Fuzz[s]);
            }
    Rule=NULL;
    for(i=RULE_LENGTH;i!=0;)/*激活规则对象集*/
    {
        if(i<0) return FALSE;
        i--;
        R=new rule(Rulep[i],Rulec[i],Rule_CF[i]);
        R->Next=Rule;
        Rule=R;
                                              }
    R=Rule;
    for(;;)
    {
           if(R->Query()) break;
           R=R->Next;
           if(!R) break;
           }
    for(i=0;i<FACT_LENGTH;i++)  /*给出结论*/
    {
         if(Fact[i]->GetCF()>LIMIT && Fact[i]->GetSign()==1)
         {
             Fact[i]->PutSign(0);
             cout<<endl<<endl<<" 结论为：";
             cout<<Fact[i]->GetName();
             cout<<endl<<" 其可信度为：";
             cout<<Fact[i]->GetCF();
                                   }
         cout<<endl<<"运行结束。";
         system("Pause");
         return TRUE;
                                }
} 
 

