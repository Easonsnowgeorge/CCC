#include <bits/stdc++.h>

using namespace std;

#define showme(x) cout << #x << ": " << x << endl;
typedef long long ll;
typedef long double ld;

#if 0 // desperate measures
#define int ll
#define double ld
#endif

typedef pair<int, int> pi;
#define fi first
#define se second
typedef vector<int> vi;
typedef vector<pi> vpi;
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()

int N, id, tt;
string s, t, curr;
map<string, int> mapp;
vi adj[101];
bool vis[101];

bool dfs(int a) {
	vis[a] = true;
	if (a == tt) return true;
	for (int v : adj[a]) {
		if (vis[v]) continue;
		if (dfs(v)) return true;
	}
	return false;
}

int32_t main(void) {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	getline(cin, s);
	N = stoi(s);

	for (int i = 0; i < N; i++) {
		getline(cin, curr); // url
		if (mapp.find(curr) == mapp.end()) {
			mapp[curr] = ++id;
		}
		while (true) {
			getline(cin, s);
			
			int sb = 0;
			while (true) {
				auto f = s.find("<A HREF=\"", sb);
				if (f == string::npos) break;
				sb = f + 1;
				if (sb >= s.length()) break;
				int end = s.find("\">", sb);
				if (end == string::npos) break;
				if (f + 9 >= s.length()) break;
				string to = s.substr(f + 9, end - (f + 9));
				if (mapp.find(to) == mapp.end()) {
					mapp[to] = ++id;
				}
				adj[mapp[curr]].pb(mapp[to]);
				cout << "Link from " << curr << " to " << to << '\n';
			}
			
			if (s.find("</HTML>") != string::npos) break;
		}
	}
	
	while (true) {
		getline(cin, s);
		if (s == "The End") break;
		getline(cin, t);
		
		memset(vis, 0, sizeof(vis));
		tt = mapp[t];
		cout << (dfs(mapp[s]) ? "Can" : "Can't") << " surf from " << s << " to " << t << ".\n";
	}

	return 0;
}