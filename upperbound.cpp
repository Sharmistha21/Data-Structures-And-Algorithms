#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    vector<int>arr1={10,15,20,25,30,35};
    vector<int>arr2={10,15,20,20,25,30,35};
    vector<int>arr3={10,15,25,30,35};

    int val=20;

    cout<<upper_bound(arr1.begin(),arr1.end(),val)-arr1.begin();
    cout<<endl;

    cout<<upper_bound(arr2.begin(),arr2.end(),val)-arr2.begin();
    cout<<endl;

    cout<<upper_bound(arr3.begin(),arr3.end(),val)-arr3.begin();
    cout<<endl;

    return 0;

}