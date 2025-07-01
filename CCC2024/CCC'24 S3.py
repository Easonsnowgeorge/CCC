# from typing import List, Tuple, Optional
# from collections import deque
#
#
# def apply_swipe(A: List[int], l: int, r: int, direction: str) -> List[int]:
#     """
#     Apply a swipe operation and return the new array.
#     """
#     A = A.copy()
#     if direction == 'R':
#         target = A[l]
#     else:  # direction == 'L'
#         target = A[r]
#
#     for i in range(l, r + 1):
#         A[i] = target
#     return A
#
#
# def find_solution(A: List[int], B: List[int], n: int) -> List[Tuple[str, int, int]]:
#     """
#     Use BFS to find the shortest sequence of swipes to transform A into B.
#     Returns list of (direction, left, right) tuples.
#     """
#     # If arrays are already equal, no swipes needed
#     if A == B:
#         return []
#
#     # Queue will store (current_array, path) pairs
#     queue = deque([(A, [])])
#     seen = {tuple(A)}
#
#     while queue:
#         curr_A, path = queue.popleft()
#
#         # Try all possible swipes
#         for l in range(n):
#             for r in range(l, n):
#                 # Try right swipe
#                 new_A_right = apply_swipe(curr_A, l, r, 'R')
#                 state_right = tuple(new_A_right)
#
#                 if state_right not in seen:
#                     seen.add(state_right)
#                     new_path = path + [('R', l, r)]
#                     if new_A_right == B:
#                         return new_path
#                     queue.append((new_A_right, new_path))
#
#                 # Try left swipe
#                 new_A_left = apply_swipe(curr_A, l, r, 'L')
#                 state_left = tuple(new_A_left)
#
#                 if state_left not in seen:
#                     seen.add(state_left)
#                     new_path = path + [('L', l, r)]
#                     if new_A_left == B:
#                         return new_path
#                     queue.append((new_A_left, new_path))
#
#         # Limit the search depth to avoid TLE
#         if len(path) >= n:
#             break
#
#     return None
#
#
# def solve(n: int, A: List[int], B: List[int]) -> None:
#     """
#     Main solver function that prints the solution in the required format.
#     """
#     solution = find_solution(A, B, n)
#
#     if solution is None:
#         print("NO")
#     else:
#         print("YES")
#         print(len(solution))
#         for direction, l, r in solution:
#             print(f"{direction} {l} {r}")
#
#
# # Process input
# def main():
#     n = int(input())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     solve(n, A, B)
#
#
# if __name__ == "__main__":
#     main()

# TLE


import sys
input = sys.stdin.readline

n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
valTrack = [arrB[0]] # value track for array B
rangeTrack = [] # left, right track for array B

l = 0
r = 0
val = arrB[0]

# Array B is segmented
for i in range(1, n):
    if arrB[i] == val:
        r += 1
    else:
        rangeTrack.append((l, r))
        l = i
        r = i
        val = arrB[i]
        valTrack.append(val)
rangeTrack.append((l, r))

cur = 0
swipeL = []
swipeR = []
for i in range(n):
    if cur == len(valTrack): break
    if arrA[i] == valTrack[cur]:
        if rangeTrack[cur][0] < i:
            swipeL.append((rangeTrack[cur][0], i))
        if rangeTrack[cur][1] > i:
            swipeR.append((i, rangeTrack[cur][1]))
        cur += 1

if cur == len(valTrack):
    print("YES")
    print(len(swipeL) + len(swipeR))
    for left in swipeL:
        print("L", left[0], left[1])
    for i in range(len(swipeR)-1, -1, -1):
        print("R", swipeR[i][0], swipeR[i][1])

else:
    print("NO")