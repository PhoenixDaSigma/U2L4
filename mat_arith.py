# Phoenix Valent
  # U2L4
    # Make a program that solves matrix addition and multiplication problems

def mat_sum(m1, m2):
  m1Rows = len(m1)
  m1Cols = len(m1[0])
  m2Rows = len(m2)
  m2Cols = len(m2[0])
  
  if m1Rows == m2Rows and m1Cols == m2Cols:
    newMat = [["" for i in range(m1Rows)] for i in range(m1Cols)]
    for r in range(m1Rows):
      for c in range(m1Cols):
        newMat[r][c] = m1[r][c] + m2[r][c]
    return newMat
  return "NO SOLUTION"


def mat_mul(m1, m2):

  if len(m1[0]) == len(m2):
    newMat = [[0 for k in range(len(m2[i]))] for i in range(len(m1))]
    for x in range(len(m1)):
      for y in range(len(m1[x])): # less weird than i, j and k. I can do i and j, but k??? What even is that
        for z in range(len(m2[y])):
          newMat[x][z] += m1[x][y] * m2[y][z]
    return newMat
  return "No solution"