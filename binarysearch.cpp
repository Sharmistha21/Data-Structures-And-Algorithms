#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void isPresent(vector<int>&arr,int val){
    if(binary_search(arr.begin(),arr.end(),val)){
        cout<<val<<" exists in vector";
    }else{
        cout<<val<<" does not exist";
    }

    cout<<endl;
}

int main(){
    vector<int>arr={10,15,20,25,30,35};
    int val1=15;
    int val2=23;

    isPresent(arr,val1);
    isPresent(arr,val2);

    return 0;
}

