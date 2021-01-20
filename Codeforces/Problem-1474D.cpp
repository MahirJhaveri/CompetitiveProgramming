// Problem 1474D - Cleaning

#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> arr(n+1);
    for(int i=1; i<=n; i++) {
        cin >> arr[i];
    }
    
    if(n == 1) {
        cout << "NO\n";
        return;
    }
    
    vector<int> p(n+2);
    vector<int> s(n+2);
    p[0] = 0;
    for(int i=1; i<=n; i++) {
        if (p[i-1] == -1 || arr[i] - p[i-1] < 0) {
            p[i] = -1;
        } else {
            p[i] = arr[i] - p[i-1];
        }
    }
    
    if(p[n] == 0) {
        cout << "YES" << "\n";
        return;
    }
    
    s[n+1] = 0;
    for(int i=n; i>=1; i--) {
        if(s[i+1] == -1 || arr[i] - s[i+1] < 0) {
            s[i] = -1;
        } else {
            s[i] = arr[i] - s[i+1];
        }
    }
    
    for(int i=1; i<n; i++) {
        if(p[i-1] >= 0 && s[i+2] >= 0 && arr[i+1] - p[i-1] >= 0 && arr[i+1] - p[i-1] == arr[i] - s[i+2]) {
            cout << "YES" << "\n";
            return;
        }
    }
    
    cout << "NO\n";
    return;
}

int main(int argc, char* argv[]) {
    int T;
	cin >> T;
	for(int c = 0; c < T; c++) {
	    solve();
	}
	return 0;
}
