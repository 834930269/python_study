#include<bits/stdc++.h>
using namespace std;

double low[6]={350,550,750,950,1150,1350};
double upr[6]={550,750,950,1150,1350,1550};

//初始时各区域的单车辆数
int init_cnt[11]={0,100,109,90,99,106,102,90,120,91,93};

int cnt=0;//总点数

struct star{
    double time;
    int regino;
    int status;//status为1,则为借出态,为0,则为归还态
}reg[100000];

int Section[10][12];//某一时间区间各个区域的单车数量

int init_regino;//起始区域

int main(){
    freopen("in.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    memset(Section,0,sizeof(Section));
    char a;
    while(cin>>a){
        if(a=='I'){
            int id;
            cin>>id>>init_regino;
        }else if(a=='O'){
            double start,ended,Next;
            cin>>start>>ended>>Next;
            reg[cnt++]=(star){start,init_regino,1};
            reg[cnt++]=(star){ended,Next,0};
            init_regino=Next;
        }
    }
    for(int i=0;i<cnt;++i){
        star &p=reg[i];
        int tt;
        for(int j=0;j<6;++j){
            if(p.time>low[j]&&p.time<upr[j]){
                tt=j;break;
            }
        }
        if(p.status==1){
            Section[tt+1][p.regino]--;
        }else{
            Section[tt+1][p.regino]++;
        }
    }

    for(int i=1;i<=10;++i){
        Section[0][i]=init_cnt[i];
    }
    for(int i=1;i<=6;++i){
        //printf("Then time regino is %.2lf-%.2lf : \n",low[i-1],upr[i-1]);
        for(int j=1;j<=10;++j){
            Section[i][j]+=Section[i-1][j];
            printf("%d %d %d\n",i,j,Section[i][j]);
        }
    }
    return 0;
}
