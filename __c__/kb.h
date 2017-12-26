#ifndef kb_h
#define kb_h
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <conio.h>
#include <stdlib.h>
#define TRUE 1/*定义返回值*/
#define FALSE 0
#define FACT_LENGTH 9  /*前提与结论总数*/
#define PRMS_LENGTH 2  /*每条规则的前提个数*/
#define PREMISE 7      /*前提数量*/ 
#define RULE_LENGTH 4  /*规则数量*/
#define LIMIT 0.5      /*结论阈值*/
#define AND  1         /*规则前提逻辑关系*/
#define OR   0
#define VH   0.9       /*规则前提可信度初始化*/
#define H    0.7
#define M    0.5
using namespace std;
double Rule_CF[RULE_LENGTH];
double(*Fuzz[6])(int);
void (*Input[6])(int);
char *Repeat="-111";   /*重新输入变量*/
/*知识表达*/ss
char *Str[FACT_LENGTH+1]={"E1","E2","E3","E4","E5","E6","E7","H1","H","\0"}; 
int Sign[FACT_LENGTH]={0,0,0,0,0,0,0,0,1};
int Rulep[RULE_LENGTH][PRMS_LENGTH+1]={{1,2,0},{4,5,0},{6,8,0},{3,7,0}};
int Rulec[RULE_LENGTH][2]={{9,AND},{8,AND},{7,AND},{9,OR}};
void Input1(int i)
{
     cout<<endl<<"按q或Q退出";
     cout<<endl<<"请输入事实"<<"E["<<i<<"]的可信度";
     cout<<"可信度为："; 
     cout<<endl<<" [1]高";
     cout<<endl<<" [2]中";
     cout<<endl<<" [3]低"<<endl;
 }
void Input2(int i=3)
{
     cout<<endl<<"按q或Q退出";
     cout<<endl<<"请输入事实"<<"E["<<i<<"]数值[30-45]："<<endl;  
 }
void Input3(int i=4)
{
     cout<<endl<<"按q或Q退出";
     cout<<endl<<"请输入事实"<<"E["<<i<<"]数值[60,160]："<<endl;
 }
double Fuzz1(int sign)
{
       switch(sign)
       {
           case 1:return VH;
           case 2:return H;
           case 3:return M;
           default:
                   cerr<<"请重新输入！";
                   return atoi(Repeat);
                   }
       }
double Fuzz2(int sign)
{
       if(sign<30||sign>45)
       {
          cerr<<"请重新输入！";
          return atoi(Repeat);
                           }
       double i=(sign-37.0)/9.0;
       return (i>0?i:-i);
       }
double Fuzz3(int sign)
{
       if(sign<60||sign>160)
       {
          cerr<<"请重新输入！";
          return atoi(Repeat);
                            }
       double i,x;
       i=(sign-60.0)/100.0;
       return(i);
       }
void DefFuncArray()
{
     for(int i=0;i<=3;i++) Fuzz[i]=Fuzz1;
     Fuzz[4]=Fuzz2;
     Fuzz[5]=Fuzz3;
 }
void DefInput()
{
     for(int i=0;i<=3;i++) Input[i]=Input1;
     Input[4]=Input2;
     Input[5]=Input3;
 }
/*定义规则的可信度*/
void DefRule_CF()
{
     Rule_CF[0]=0.9;
     Rule_CF[1]=1.0;
     Rule_CF[2]=0.9;
     Rule_CF[3]=0.9;
 }
 #endif
