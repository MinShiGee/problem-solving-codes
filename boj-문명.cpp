# https://www.acmicpc.net/problem/14868

#include <stdio.h>
#include <queue>
#include <algorithm>

#define MAX_N 2005
#define MAX_K 100005
#define MAX_INT 2e9

using namespace std;

int N, M;
int arr[MAX_N][MAX_N];
int par[MAX_K];
int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,1,-1 };
int vis[MAX_N][MAX_N];

struct Data {

	int y;
	int x;
	int index;
	int cnt;

	Data(int y_, int x_, int i_, int cnt_) { y = y_; x = x_; index = i_; cnt = cnt_; }

};

queue<Data> que;


int find(int a) {
	return (a == par[a]) ? a : par[a] = find(par[a]);
}
bool merge(int a, int b) {

	a = find(a);
	b = find(b);

	if (a == b)
		return false;

	if (a < b)
		par[b] = a;
	else
		par[a] = b;

	return true;
}

void input() {

	scanf("%d %d", &N, &M);

	for (int i = 0; i <= N + 1; i++)
		for (int j = 0; j <= N + 1; j++)
			arr[i][j] = -1;

	for (int i = 0; i < M; i++) {
		int temp, temp2;
		scanf("%d %d", &temp, &temp2);
		que.push(Data(temp2, temp, i + 1, 0));
		arr[temp2][temp] = i + 1;
		par[i + 1] = i + 1;
	}

}

int solve() {

	int COUNT = M;
	int res = 0;

	while (!que.empty()) {

		int x = que.front().x;
		int y = que.front().y;
		int index = que.front().index;
		int cnt = que.front().cnt;
		que.pop();

		int uni = find(index);

		for (int i = 0; i < 4; i++) {
			int qx = x + dx[i];
			int qy = y + dy[i];

			if (qx < 1 || qx > N || qy < 1 || qy > N)
				continue;

			if (arr[qy][qx] == -1) {
				arr[qy][qx] = index;
				vis[qy][qx] = cnt + 1;
				que.push(Data(qy, qx, index, cnt + 1));
			}
			else {
				int quni = find(arr[qy][qx]);
				if (vis[y][x] >= vis[qy][qx] && merge(uni, quni)) {
					COUNT--;
					res = max(res, vis[y][x]);
				}
			}

		}

	}

	return res;

}

int main() {
	input();
	int res = solve();
	printf("%d", res);
}