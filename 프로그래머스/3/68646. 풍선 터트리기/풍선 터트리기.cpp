#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> a) {
    int n = a.size();

    if (n == 1) return 1;
    else if (n == 2)return 2;
    else {

        multiset<int> leftset;
        multiset<int> rightset;

        leftset.insert(a[0]);
        for (int i = 2; i < n; i++) {
            rightset.insert(a[i]);
        }

        int diecnt = 0;
        for (int i = 1; i < n - 1; i++) {
            // 현재 검사
            // left , right 최소값
            int leftmin = *leftset.begin();
            int rightmin = *rightset.begin();
            
            if (leftmin < a[i] and a[i] > rightmin)diecnt++;

            leftset.insert(a[i]);
            rightset.erase(a[i + 1]);
        }

        return n - diecnt;
    }
    
}