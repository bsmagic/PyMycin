/*推理机头文件inference.h*/
#ifndef inference_h
#define inference_h
#include "kb.h"
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <alloc.h>
#include "stdio.h"
//using namespace std;

class fact  /*定义事实类*/ 
{
      private:
              int Number;    /*事实编号*/
              char *Name;    /*事实内容*/
              double CF;     /*事实可信度*/
              int Active;    /*记录事实的激活状态*/
              int Sign;      /*输出标记*/
              double (*Fuzz)(int i); /*定义可信度模糊函数*/
      public:
             void (*Input)(int);  /*输入函数*/
             fact(int Num,char *L)  /*初始化事实*/
             {
                      Name=(char*) malloc(strlen(L)+1);
                      strcpy(Name,L);
                      Number=Num;
                      Active=FALSE;
                      CF=0;
                      Sign=0;
                      };
             char* GetName()
             {
                   char *L;
                   L=new char(strlen(Name)+1);
                   if(L!=NULL) strcpy(L,Name);
                   return L;
                   }
             int GetNumber(){return Number;}
             int GetAct(){return Active;}
             void PutAct(const int Act){Active=Act;}
             void PutFunc(double(*f)(int)){Fuzz=f;}
             double GetCF(){return CF;}
             int PutCF(int i)   /*处理用户输入*/
             {
                 CF=Fuzz(i);
                 return CF;
             }
             void PutCF(double d)  /*置可信度计算结果标记*/
             {
                  CF=d;
              }
             void PutSign(int i)   /*置输出标记*/
             {
                  Sign=i;
              }
             int GetSign(){return Sign;}
      };
fact *Fact[FACT_LENGTH+1];

class rule   /*定义规则类*/
{
      private:
              char *Name;     /*规则名*/
              int List[PRMS_LENGTH]; /*同一规则的所有前提链表*/
              int Logic;      /*定义规则间的逻辑关系*/
              int Conc;       /*规则结论*/
              double RCFi;    /*规则可信度*/
      public:
             rule *Next;
             rule(const int P[],int C[],double Rule_Cf);
             ~rule();
             int Query();
             char *GetName(){return Name;}
             double CF();
             int GetConc(){return Conc;}
      };
double Max(double a,double b)  /*可信度计算*/
{return (a>b?a:b);}
double Min(double a,double b){return (a>b?b:a);}
double Mix(double x,double y){return(x+y-x*y);}
rule::~rule()  /*构造释放规则空间函数*/
{
    delete Name;
    delete []List;
               }
rule::rule(const int P[],int C[],double Rule_CF) /*构造规则函数*/
{
    List[0]=P[0];
    List[1]=P[1];
    Logic=C[1];
    Conc=C[0];
    RCFi=Rule_CF;
                 }
int rule::Query()  /*构造推理函数*/
{
    int sign=0;
    char* choose;
    char temps[10];
    choose=new char(4);
    fact* (*temp)=Fact;
    while(sign<PRMS_LENGTH)
    {
        for(;(*temp)!=NULL;temp=temp+1)
          if((*temp)->GetNumber()==List[sign]) break;
        if((*temp)==NULL) return FALSE;
        if((*temp)->GetAct()>0){sign++;temp=Fact;}
        else{
               (*temp)->Input((*temp)->GetNumber());
               scanf("%s",choose);
              // flushall();
               cout<<endl;
               if((strcmp(choose,"q")&&strcmp(choose,"Q"))==0)
                   return TRUE;
               if(strcmp(itoa(atoi(choose),temps,10),choose)!=0)
                   continue;
               if((*temp)->PutCF(atoi(choose))==atoi(Repeat))
                   continue;
               (*temp)->PutAct(TRUE);
             }
                           }
    for(temp=Fact;(*temp)!=NULL;temp++)
       if((*temp)->GetNumber()==Conc)  break;
    if((*temp)==NULL) return FALSE;
    (*temp)->PutCF(Mix((*temp)->GetCF(),CF()));
    (*temp)->PutAct(1);
    return FALSE;
}
double rule::CF()  /*构造可信度推理函数*/
{
       double i;
       if(Logic)
       {
                i=Min(Fact[List[0]-1]->GetCF(),Fact[List[1]-1]->GetCF());
                i=i*RCFi;
                return i;
                }
       }
/*初始化函数*/
void Init()
{
     DefFuncArray();
     DefInput();
     DefRule_CF();
     Fact[FACT_LENGTH]=NULL; 
     
     
 }
 #endif    
     
