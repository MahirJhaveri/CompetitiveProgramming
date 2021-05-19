// Problem 1519D - Maximum Sum of Products

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<long long> a(n);
	vector<long long> b(n);
	for(int i=0;i<n;i++)
	    cin >> a[i];
	for(int i=0;i<n;i++)
	    cin >> b[i];

	vector<long long> l(n);
	vector<long long> r(n);
	long long lsum = 0, rsum = 0;
	for(int i=0;i<n;i++){
	    lsum += a[i]*b[i];
	    l[i] = lsum;
	    rsum += a[n-1-i]*b[n-1-i];
	    r[n-1-i] = rsum;
	}
	long long ans = lsum;
	for(int c=0; c<=2*n; c++) {
	    long long i = (long long)floor(c/2.0), j = (long long)ceil(c/2.0);
	    long long temp=0;
	    while(i>=0 && j<n){
	        if(i != j){
	            temp += a[j]*b[i] + a[i]*b[j];
	        } else {
	            temp += a[i]*b[i];
	        }
            long long val = temp;
            if(i>0)
                val += l[i-1];
            if(j<n-1)
                val += r[j+1];
            ans = max(val, ans);
	        i--;
	        j++;
	    }
	}
	
    cout << ans << "\n";
	return 0;
}
