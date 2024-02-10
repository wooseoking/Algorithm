#include <iostream>
#include <vector>
#include <algorithm> // max 함수 사용을 위해 포함

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d, k, c;
    cin >> n >> d >> k >> c;
    
    vector<int> a(n); // 초밥 번호를 저장할 벡터
    vector<int> cnt(d + 1, 0); // 각 초밥 종류별 먹은 횟수를 저장할 벡터
    cnt[c]++; // 쿠폰 초밥 미리 추가

    for (int i = 0; i < n; ++i) {
        cin >> a[i]; // 초밥 번호 입력 받기
    }

    // 처음 k개 초밥 처리
    for (int i = 0; i < k; ++i) {
        cnt[a[i]]++;
    }

    int init = 0; // 초기에 먹을 수 있는 초밥 종류 수
    for (int i = 1; i <= d; ++i) {
        if (cnt[i] > 0) {
            init++;
        }
    }

    int max_res = init; // 최대 초밥 종류 수

    // 초밥 순환하며 검사
    for (int i = 1; i < n; ++i) {
        int out = a[i-1]; // 이전 초밥
        int newSushi = a[(i + k - 1) % n]; // 새로운 초밥

        if (--cnt[out] == 0) {
            init--;
        }

        if (cnt[newSushi]++ == 0) {
            init++;
        }

        max_res = max(max_res, init); // 최대값 갱신
    }

    cout << max_res << endl; // 최대 초밥 종류 수 출력

    return 0;
}
