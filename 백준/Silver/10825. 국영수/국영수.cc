#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
//문제
//도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다.이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
//
//국어 점수가 감소하는 순서로
//국어 점수가 같으면 영어 점수가 증가하는 순서로
//국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
//모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로(단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

struct Data {
	std::string name;
	int kr;
	int en;
	int math;

	Data(std::string name,int kr,int en,int math) :
		name(name),kr(kr),en(en),math(math)
	{

	}
};
int main() {

	int n;
	std::cin >> n;
	std::vector<Data> vec;

	while (n--) {
		std::string name;
		int kr, en, math;
		
		std::cin >> name >> kr >> en >> math;
		
		vec.emplace_back(Data(name,kr,en,math));
	}

	std::sort(vec.begin(), vec.end(), [](Data d1,Data d2) {
		if (d1.kr == d2.kr) {
			if (d1.en == d2.en) {
				if (d1.math == d2.math) {
					return d1.name < d2.name;
				}
				return d1.math > d2.math;
			}

			return d1.en < d2.en;
		}
		return d1.kr > d2.kr;
		});

	for (auto& d : vec) {
		std::cout << d.name << '\n';
	}
	return 0;
}