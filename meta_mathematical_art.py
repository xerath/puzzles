#  This is an attempt at Metas Coding Puzzle Level 4 : Mathematical art : https://www.metacareers.com/profile/coding_puzzles?puzzle=587690079288608
#  The idea is to follow the moves described in L and the directions in D on a 2D Cartesian plane, and respond with the number of complete crosses shown on it when traced out.
#  This solution doesn't pass all of the hidden test cases so I've had to abandon it.. However, I think I took an interesting approach that was worth sharing.

#  1) We take a window that offers us a view onto the last 3 moves of the complete route
#  2) We continually process the middle element to figure out if the moves either side of it represent Left or Right intersections
#  3) We store those intersections on a global hashmap of positions and their intersections
#  4) As each position is reached N times, it eventually ends up with a complex set of 4 directional intersections
#  5) We could the number of positions with 4 intersections at the end
#  6) We additionally process the last item separately 

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
