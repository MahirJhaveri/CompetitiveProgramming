// Problem 863 - Rectangle Overlap

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    
    bool area0(vector<int>& rec) {
        return (rec[0] == rec[2]) || (rec[1] == rec[3]);
    }
    
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        if (area0(rec1) || area0(rec2)) return false;
        else if ((rec2[2] <= rec1[0]) || (rec2[0] >= rec1[2])) return false;
        else if ((rec2[1] >= rec1[3]) || (rec2[3] <= rec1[1])) return false;
        return true;
    }
};
