#include <cstdio>

int gcd(int a,int b){
    if(b==0) return a;
    return gcd(b,a%b);
}

int lcm(int a,int b){
    return (a*b)/gcd(a,b);
}

int main(){
    int t,a,b;
    scanf("%d",&t);
    while (t--){
        scanf("%d%d",&a,&b);
        printf("%d\n",lcm(a,b));
    }
    return 0;
}
