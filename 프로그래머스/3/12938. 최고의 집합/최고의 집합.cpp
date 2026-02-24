#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

vector<int> solution(int n, int s) {

    int k = s / n;
    if (k == 0) return vector<int>{-1};
    vector<int> answer(n, k);
    int sum = k * n;
    
    int idx = 0;
    while (sum != s) {
        
        answer[idx]++;
        sum++;
        
        idx += 1;
        idx %= n;
    }
    
    std::sort(answer.begin(), answer.end());
   
    
    return answer;
}