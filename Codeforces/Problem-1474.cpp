// Problem 1474C - Array Destruction

#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

const int MAX_SIZE = 1e6 + 1;

int cnt[MAX_SIZE];

void reset(vector<int> a) {
    for(int i=0; i < a.size(); i++) {
        cnt[a[i]] = 0;
    }
}

void solve() {
    int n;
    cin >> n;
    vector<int> a(2*n);
    for(int k=0; k < 2*n; k++) {
        cin >> a[k];
    }
    sort(a.begin(), a.end());
    int t = 0;
    for(int i=0; i < 2*n-1; i++) {
        for(int i=0; i < a.size(); i++) {
            cnt[a[i]]++;
        }
        int x = a[i] + a[2*n-1];
        int j = 2*n-1;
        vector<int> res;
        res.push_back(x);
        while (j >= 0) {
            if (cnt[a[j]] > 0) {
                cnt[a[j]] -= 1;
                if(cnt[x-a[j]] > 0) {
                    res.push_back(a[j]);
                    res.push_back(x-a[j]);
                    cnt[x - a[j]] -= 1;
                    x = a[j];
                }
                else {
                    t = 0;
                    break;
                }
            }
            if(j == 0) {
                t = 1;
            }
            j -= 1;
        }
        
        if(t) {
            cout << "YES\n";
            cout << res[0] << "\n";
            for (int l = 1; l < res.size(); l+=2){
                cout << res[l] << " " << res[l+1] << "\n";
            }
            return;
        }
        reset(a);
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
