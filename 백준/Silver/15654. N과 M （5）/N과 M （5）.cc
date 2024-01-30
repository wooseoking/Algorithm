#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

//결과로 담을 배열
int a[8];
//중복 체크 배열
bool c[8];

void func(int index, const int& N, const int& M, vector<int>& arr) {
	if (index == M) {
		for (int i = 0; i < M; i++) {
			cout << a[i] << ' ';
		}cout << '\n';
		return;
	}
	

	for (int i = 0; i < arr.size(); i++) {
		if (c[i]) continue;
		c[i] = true;
		a[index] = arr[i];
		func(index + 1, N, M, arr);
		c[i] = false;
	}
}
int main() {
	int N, M;
	cin >> N >> M;
	vector<int> arr;
	while (N--) {
		int temp;
		cin >> temp;
		arr.push_back(temp);
	}

	sort(arr.begin(), arr.end());

	func(0, N, M, arr);
}