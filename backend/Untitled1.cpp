#include<iostream>

using namespace std;

int main(){

int t;
cin>>t;

for(int k=1;k<=t;k++){

int n;
cin>>n;
int a[16];
for(int i=0;i<16;i++) cin>>a[i];

int m;
cin>>m;
int b[16];
for(int i=0;i<16;i++) cin>>b[i];

int s=0,f;

for(int i=4*n-4;i<4*n;i++){
for(int j=4*m-4;j<4*m;j++){
if(a[i]==b[j]) {f=a[i];s++;}

}
}


if(s==0) cout<<"Case #"<<k<<": Volunteer cheated!";
else{
if(s==1) cout<<"Case #"<<k<<": "<<f<<endl;
else cout<<"Case #"<<k<<": Bad magician!"<<endl;

}



}

}
