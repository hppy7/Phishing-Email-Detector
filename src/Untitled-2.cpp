#include<iostream>
using namespace std;
class number
{
    int n;
    public :
    void read()
    {
        cout<<"enter number"<<endl;
        cin>>n;
    }
    int operator <(number X)
    {

        if(n<X.n)
        return 1;
        else
        return 0;
    }
    int operator >(number X)
    {

        if(n>X.n)
        return 1;
        else
        return 0;
    }
    int operator ==(number X)
    {

        if(n==X.n)
        return 1;
        else
        return 0;
    }
};
int main()
{
number n1,n2;
n1.read();
n2.read();
if(n1<n2)
cout<<"n1 is less than n2"<<endl;
else
{
    if(n1>n2)
    cout<<"n1 is greatter than n2"<<endl;
    else
    if(n1==n2)
    cout<<"numbr is equal"<<endl;
}

}