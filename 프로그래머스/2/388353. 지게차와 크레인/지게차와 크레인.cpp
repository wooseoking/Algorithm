#include<iostream>
#include<vector>
#include<string>
#include<queue>

using namespace std;


constexpr int dy[] = { -1,1,0,0 };
constexpr int dx[] = { 0,0,-1,1 };
constexpr char EMPTY = ' ';

struct Point {
	int y;
	int x;
	Point(int y, int x) :
		y(y), x(x) {}
};

// 1<< y << n , 1 << x << m 보드로 생성
class Board {
private:
	int n, m;
	vector<string> storage;
	vector<Point> candidates;
	
public:

	Board(int n, int m,const vector<string>& storage) :
		n(n), m(m) 
	{
		vector<string> newStorage(n + 2, string(m + 2, EMPTY));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				newStorage[i + 1][j + 1] = storage[i][j];
			}
		}
		this->storage = std::move(newStorage);
	}

	bool inside(const int& y, const int& x) {
		return 0 <= y and y < n + 2 and 0 <= x and x < m + 2;
	}
	// 후보 찾기
	void FindCandidates(string request) {
		auto c = request[0];


		if (request.size() == 2) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= m; j++) {
					if (storage[i][j] == c) {
						candidates.emplace_back(Point{ i,j });
					}
				}
			}
		}
		else {
			vector<vector<bool>> visited(n + 2, vector<bool>(m + 2, false));
			queue<Point> q;
			q.push(Point{ 0,0 });
			visited[0][0] = true;
			
			while (!q.empty()) {
				Point p = q.front(); q.pop();
				int y = p.y;
				int x = p.x;
				
				for (int k = 0; k < 4; k++) {
					int ny = y + dy[k];
					int nx = x + dx[k];
					if (not inside(ny, nx))continue;
					if (visited[ny][nx])continue;
					if (storage[ny][nx] == c) {
						visited[ny][nx] = true;
						candidates.emplace_back(Point{ ny,nx });
					}
					if (storage[ny][nx] == EMPTY) {
						visited[ny][nx] = true;
						q.push(Point{ ny,nx });
					}
				}
			}
		}
	}
	// 후보 삭제
	void DeleteCandidates() {
		for (auto& p : candidates) {
			int y = p.y;
			int x = p.x;
			storage[y][x] = EMPTY;
		}
		candidates.clear();
	}
	// 현재 남아있는 컨테이너 수
	int GetRemainedContainer() {
		int cnt = 0;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (storage[i][j] != EMPTY)cnt++;
			}
		}
		return cnt;
	}

	void PrintBoard() {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				cout << storage[i][j] << ' ';
			}cout << endl;
		}
		cout << "----------------------------------------------------------" << endl;
	}
};

int solution(vector<string> storage, vector<string> requests) {
	int answer = 0;
	int n = storage.size();
	int m = storage[0].size();

	Board board(n, m, storage);
	
	for (auto& request : requests) {
		board.FindCandidates(request);
		board.DeleteCandidates();
		// board.PrintBoard();
	}
	answer = board.GetRemainedContainer();
	return answer;
}

