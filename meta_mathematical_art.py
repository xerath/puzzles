"""
Problem: Mathematical Art

You are creating a special painting on a canvas which may be represented as a 2D Cartesian plane. 
You start by placing a thin brush at the origin (0, 0) and then make N axis-aligned strokes 
without lifting the brush off of the canvas. For the ith stroke, you'll move your brush Li units 
from its current position in a direction indicated by the character Di, which is either U (up), 
D (down), L (left), or R (right), while leaving behind a line segment of paint between the brush's 
current and new positions. For example, if L1 = 5 and D1 = L, you'll draw a stroke between 
coordinates (0, 0) and (-5, 0), with your brush ending up at coordinates (-5, 0). Note that each 
stroke is either horizontal or vertical, and that each stroke (after the first) begins where the 
previous stroke ended.

This painting is being marketed as a work of mathematical art, and its value is based on the 
number of times a certain mathematical symbol appears in it – specifically, the plus sign. A 
plus sign is considered to be present at a certain position if and only if, for each of the 4 
cardinal directions (up, down, left, and right), there's paint leading from the point in that 
direction (or, vice versa, leading to that point from that direction). Note that the paint from 
arbitrarily many strokes of your brush might come together to form any given plus sign, and that 
at most one plus sign may be considered to exist at any given position.

Determine the number of positions in the painting at which a plus sign is present.

Constraints:
2 <= N <= 2,000,000
1 <= Li <= 1,000,000,000
Di ∈ {U, D, L, R}

Sample test case #1:
N = 9
L = [6, 3, 4, 5, 1, 6, 3, 3, 4]
D = ULULRURRD
Expected Return Value = 4

Sample test case #2:
N = 8
L = [1, 1, 1, 1, 1, 1, 1, 1]
D = RDLULDR
Expected Return Value = 1

Sample test case #3:
N = 8
L = [1, 2, 2, 1, 1, 2, 2, 1]
D = UUDDLRLR
Expected Return Value = 1

Sample Explanation:

The first case is depicted below, with blue arrows indicating brush strokes and the 4 plus 
signs highlighted in red:
"""


"""
NOTES :
This is an attempt at Metas Coding Puzzle Level 4 : Mathematical art : https://www.metacareers.com/profile/coding_puzzles?puzzle=587690079288608
This solution doesn't pass all of the hidden test cases so I've had to abandon it.. However, I think I took an interesting approach that was worth sharing.

1) We take a window that offers us a view onto the last 3 moves of the complete route
2) We continually process the middle element to figure out if the moves either side of it represent Left/Right/Up/Down intersections
3) We store those intersections on a global hashmap of positions and their intersections
4) As each position is reached multiple times, it eventually ends up with a complex set of 4 directional intersections
5) We could the number of positions with 4 intersections at the end
6) We additionally process the last item separately
"""

from typing import List
from collections import deque

def getPlusSignCount(N: int, L: List[int], D: str) -> int:
    # window through the landscape
    window = deque([[0, 0]])
    
    # hashmap of positions and which intersections they have
    posMap = { '00': { 'l': False, 'r': False, 'u': False, 'd': False } }
    
    # X, Y
    position = [0, 0]
    
    # plus symbols detected
    plusSymbols = 0
  
    for move in range(N):
        # X or Y axis
        axis = 0
        if(D[move] == 'U' or D[move] == 'D'): axis = 1
        
        # 1 or -1 depending on pos/neg direction
        multip = 1
        if D[move] == 'L' or D[move] == 'D': multip = -1
        
        # for each part of the move
        for i in range(1, L[move] + 1):
            # Ensure window is length <= 3
            if len(window) == 3: window.popleft()
        
            # Add new position to queue
            position[axis] += (1 * multip)
            # prevents pointer
            window.append([position[0], position[1]])
            
            # position to string eg/ [0,-3] -> "0-3"
            positionStr = ''.join(map(str, [position[0], position[1]]))
            
            # create hashmap entry
            if positionStr not in posMap:
                posMap[positionStr] = { 'l': False, 'r': False, 'u': False, 'd': False }    
            
            # process the previous item
            if len(window) > 1:
                prevInd = 1 if len(window) == 3 else 0
                previousposstr = ''.join(map(str, window[prevInd]))
                for x in [0, len(window) - 1]:
                    # Compare to next/previous
                    if window[1][0] < window[x][0]: posMap[previousposstr]['l'] = True
                    if window[1][0] > window[x][0]: posMap[previousposstr]['r'] = True
                    if window[1][1] < window[x][1]: posMap[previousposstr]['d'] = True
                    if window[1][1] > window[x][1]: posMap[previousposstr]['u'] = True
            
            # If this is the very last item
            if i == L[move] and move == N - 1:
                # Compare to previous
                if window[1][0] < window[2][0]: posMap[positionStr]['l'] = True
                if window[1][0] > window[2][0]: posMap[positionStr]['r'] = True
                if window[1][1] < window[2][1]: posMap[positionStr]['d'] = True
                if window[1][1] > window[2][1]: posMap[positionStr]['u'] = True
            
    
    # Count how many positions have all 4 intersections
    for pos in posMap:
        # all directions = true
        if all(posMap[pos].values()): plusSymbols += 1

    return plusSymbols


# result = getPlusSignCount(8, [1, 2, 2, 1, 1, 2, 2, 1], 'UDUDLRLR')
result = getPlusSignCount(9, [6, 3, 4, 5, 1, 6, 3, 3, 4], 'ULDRULURD')
# result = getPlusSignCount(8, [1, 1, 1, 1, 1, 1, 1, 1], 'RDLUULDR')

print(result)
