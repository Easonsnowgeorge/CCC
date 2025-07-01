def solve(level, lines, x):
    if (level == 0):
        res = set({})
        for line in lines:
            startX, startY, endX, endY, d = line
            if (startX > endX):
                startX, endX = endX, startX

            if (x >= startX and x <= endX):
                if (startX == endX):
                    if (startY > endY):
                        startY, endY = endY, startY
                    for y in range(int(startY), int(endY)):
                        res.add(y)
                else:
                    res.add(endY)

        return res
    newLines = []
    for line in lines:
        startX, startY, endX, endY, d = line
        if (startX > endX):
            startX, endX = endX, startX
        if (startY > endY):
            startY, endY = endY, startY
        widthXSeg = abs((endX - startX) / 3)
        widthYSeg = abs((endY - startY) / 3)
        # up
        if (d == 0):
            newLines.append([startX, startY, startX + widthXSeg, endY, d])
            newLines.append([startX + 2 * widthXSeg, startY, endX, endY, d])
            newLines.append([startX + widthXSeg, startY, startX + widthXSeg, startY + widthXSeg, 3])
            newLines.append([startX + 2 * widthXSeg, startY, startX + 2 * widthXSeg, startY + widthXSeg, 1])
            newLines.append([startX + widthXSeg, startY + widthXSeg, endX - widthXSeg, startY + widthXSeg, d])
        # right
        if (d == 1):
            newLines.append([startX, startY, endX, startY + widthYSeg, d])
            newLines.append([startX, startY + 2 * widthYSeg, endX, endY, d])
            newLines.append([startX, startY + widthYSeg, startX + widthYSeg, startY + widthYSeg, 2])
            newLines.append([startX, startY + 2 * widthYSeg, startX + widthYSeg, startY + 2 * widthYSeg, 0])
            newLines.append([startX + widthYSeg, startY + widthYSeg, startX + widthYSeg, startY + 2 * widthYSeg, d])

        # down
        if (d == 2):
            newLines.append([startX, startY, startX + widthXSeg, endY, d])
            newLines.append([startX + 2 * widthXSeg, startY, endX, endY, d])
            newLines.append([startX + widthXSeg, startY, startX + widthXSeg, startY + widthXSeg, 3])
            newLines.append([startX + 2 * widthXSeg, startY, startX + 2 * widthXSeg, startY + widthXSeg, 1])
            newLines.append([startX + widthXSeg, startY - widthXSeg, endX - widthXSeg, startY - widthXSeg, d])
        # left
        if (d == 3):
            newLines.append([startX, startY, endX, startY + widthYSeg, d])
            newLines.append([startX, startY + 2 * widthYSeg, endX, endY, d])
            newLines.append([startX, startY + widthYSeg, startX - widthYSeg, startY + widthYSeg, 2])
            newLines.append([startX, startY + 2 * widthYSeg, startX - widthYSeg, startY + 2 * widthYSeg, 0])
            newLines.append([startX - widthYSeg, startY + widthYSeg, startX - widthYSeg, startY + 2 * widthYSeg, d])
    return solve(level - 1, newLines, x)


level, width, x = map(int, input().split())

lines = [[0, 1, width, 1, 0]]
ans = list(solve(level, lines, x))
ans.sort()
s = ""
for num in ans:
    s += str(int(num)) + " "
print(s[:-1])