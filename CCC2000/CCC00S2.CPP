#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  int initial;
  cin >> initial;

  vector<double> streams;
  streams.reserve(initial);
  for (int i = 0; i < initial; i++) {
    double value;
    cin >> value;
    streams.emplace_back(value);
  }

  while (true) {
    int op;
    cin >> op;

    if (op == 99) {
      // Split
      int line;
      cin >> line;
      line -= 1;

      double percent;
      cin >> percent;

      auto it = streams.begin() + line + 1;
      streams.insert(it, streams[line] * (1.0 - percent / 100.0));
      streams[line] *= percent / 100.0;
    } else if (op == 88) {
      // Merge
      int line;
      cin >> line;

      streams[line - 1] += streams[line];
      streams.erase(streams.begin() + line);
    } else {
      break;
    }
  }

  for (int i = 0; i < streams.size(); i++) {
    cout << round(streams[i]) << " ";
  }
}