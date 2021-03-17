/* Problem 1495D - BFSTrees */

#include <iostream>
#include <vector>
using namespace std;

#define INF 99999 

#define BIGNUM 998244353

/* TASKS:
 - Take all inputs
 - Represent the data as a graph in c++ - vector<vector<int>>
 - Compute all distances in c++ (form a distance matrix - pretty standard problem)
 - 
*/

int main() {
	int n,m;
	cin >> n >> m;
	
	vector<int> g[n];
	int dist[n][n];
	int i,j,k;
	int x,y;
	
	// Initialize dist 
	for(i = 0; i < n; i++) {
	    for(j = 0; j < n; j++) {
	        dist[i][j] = INF;
	        if (i == j) {
	            dist[i][j] = 0;
	        }
	    }
	}
	
	
	for(i = 0; i < m; i++) {
	    int a,b;
	    cin >> a >> b;
	    g[a-1].push_back(b-1);
	    g[b-1].push_back(a-1);
	    dist[a-1][b-1] = 1;
	    dist[b-1][a-1] = 1;
	}
	
	// Apply the floyd-warshal algorithm to compute distances 
	for(k = 0; k < n; k++) {
	    for(i = 0; i < n; i++) {
	        for(j = i+1; j < n; j++) {
	            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j]);
	            dist[j][i] = dist[i][j];  
	        }
	    }
	}
	
	long ans[n][n];
	for(x = 0; x < n; x++) {
	    for(y = x; y < n; y++) {
	        unsigned long long numBTrees = 1;
	        int numPathNodes = 0;
	        for(j = 0; j < n; j++) {
	            if (x != j and y != j) {
	                if(dist[x][j] + dist[y][j] == dist[x][y]) { // k must be on the path
	                    if(numPathNodes < dist[x][y]-1) {
	                        numPathNodes++;
	                    } else {
	                        numBTrees = 0;
	                    }
	                } else {
	                    unsigned long long count = 0;
	                    for(int i : g[j]) {
	                        if (dist[x][i] + 1 == dist[x][j] && dist[y][i] + 1 == dist[y][j]) {
	                            count++;
	                        }
	                    }
	                    numBTrees = (numBTrees * count) % BIGNUM;
	                }
	                if (numBTrees == 0)
	                    break;
	            }
	        }
	        ans[x][y] = numBTrees;
	        ans[y][x] = numBTrees;
	    }
	}
	
	for (int i = 0; i < n; i++) 
       for (int j = 0; j < n; j++) 
          cout << ans[i][j] <<  " \n"[j == n-1];
	
	
	return 0;
}
