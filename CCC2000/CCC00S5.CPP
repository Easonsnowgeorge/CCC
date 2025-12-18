#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <cstdio> // 替代i/o stream的输出，用于精确格式化

using namespace std;

// 定义绵羊结构体
struct Sheep {
    double x;
    double y;
    int id; // 用于标识绵羊的原始顺序
    bool might_be_eaten = false; // 是否可能被吃
};

// 计算土狼进入点 P(px, 0) 到绵羊 S(sx, sy) 距离的平方
double distance_sq(double px, const Sheep& s) {
    // 土狼的 y 坐标为 0
    return (s.x - px) * (s.x - px) + s.y * s.y;
}

void solve() {
    int N;
    if (!(cin >> N)) return;

    // 读取所有绵羊的坐标
    vector<Sheep> sheeps(N);
    for (int i = 0; i < N; ++i) {
        if (!(cin >> sheeps[i].x >> sheeps[i].y)) return;
        sheeps[i].id = i;
    }

    // 离散化测试参数
    const int MAX_X = 1000;
    // 使用整数步长来避免浮点数循环误差
    // 步长为 0.01，即 0 到 100000 步
    const int NUM_STEPS = 100000;
    const double STEP_SIZE = (double)MAX_X / NUM_STEPS;
    // 浮点数比较的容差（epsilon），用于处理距离相等的情况
    const double EPSILON = 1e-9; 

    // 遍历南边界上的所有测试点 P(px, 0)
    for (int i = 0; i <= NUM_STEPS; ++i) {
        double px = i * STEP_SIZE;
        
        // 1. 找到最小距离的平方
        double min_dist_sq = 1e18; // 足够大的初始值
        for (const auto& s : sheeps) {
            double dist_sq = distance_sq(px, s);
            if (dist_sq < min_dist_sq) {
                min_dist_sq = dist_sq;
            }
        }
        
        // 2. 标记所有距离等于最小距离的绵羊
        for (int j = 0; j < N; ++j) {
            double dist_sq = distance_sq(px, sheeps[j]);
            
            // 如果距离在这个测试点 P 处是最小的（考虑到浮点误差）
            if (dist_sq <= min_dist_sq + EPSILON) {
                sheeps[j].might_be_eaten = true;
            }
        }
    }

    // 3. 收集并输出结果
    // 使用 C 的 printf 进行精确的两位小数输出
    for (const auto& s : sheeps) {
        if (s.might_be_eaten) {
            printf("The sheep at (%.2f, %.2f) might be eaten.\n", s.x, s.y);
        }
    }
}

int main() {
    // 优化输入/输出速度
    // std::ios_base::sync_with_stdio(false);
    // std::cin.tie(NULL);
    // 由于使用了 printf，此处不使用 cin/cout 优化，但保持 main 结构

    // 设置输出浮点数的精度，虽然 printf 更直接，但这是 good practice
    // cout << fixed << setprecision(2); 

    solve();

    return 0;
}