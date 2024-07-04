# Meta cafeteria puzzle : https://www.metacareers.com/profile/coding_puzzles?puzzle=203188678289677
# Determine how many diners can fit at a table with defined social distancing rules

from typing import List
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  extraSpace = 0
  firstOpenSeat = 1
  for takenSeat in S:
    openSeats = takenSeat - K - firstOpenSeat
    if(openSeats > 0):
      extraSpace += math.ceil(openSeats / (K + 1))
    firstOpenSeat = takenSeat + K + 1
  openSeats = N + 1 - firstOpenSeat
  if(openSeats > 0):
    extraSpace += math.ceil(openSeats / (K + 1))
  return extraSpace
