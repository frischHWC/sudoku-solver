import logging


def coordinate_list_for_square(coordinate, size):
  if size == 4:
    if(coordinate<=1):
      return [0, 1]
    else:
      return [2, 3]
  elif size == 9:
    if coordinate <= 2:
      return [0, 1, 2]
    elif coordinate <= 5:
      return [3, 4, 5]
    else:
      return [6, 7, 8]


def check_list(list_of_possibilities):
  if len(list_of_possibilities) == 1:
    return True
  else:
    return False


def check_matrix_is_finished(matrix, size):
  success = True
  for i in range(0, size):
    for j in range(0, size):
      if matrix[i][j] == 0:
        success = False
  return success

def print_matrix(matrix, size):
  logger = logging.getLogger("sudoku_solver")

  logger.info("Solution is :")
  if size == 4:
    for i in range(0, size):
      logger.info("%i %i %i %i", matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3])
  elif size == 9:
    for i in range(0, size):
      logger.info("%i %i %i %i %i %i %i %i %i", matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3], matrix[i][4], matrix[i][5], matrix[i][6], matrix[i][7], matrix[i][8])


def calculate_matrix_score(matrix, size):
  logger = logging.getLogger("sudoku_solver")

  score = 0
  for i in range(0, size):
    for j in range(0, size):
      if matrix[i][j] == 0:
        score += 1

  logger.info("*******************************")
  logger.info("There is %i empty cases", score)
  logger.info("There is %i full cases", size*size - score)
  logger.info("*******************************")

  return score

def get_duplicates_of_a_list(list_to_get_duplicate):
  list_of_duplicates = []
  number_seen = []
  for n in list_to_get_duplicate:
    if n in number_seen:
      list_of_duplicates.append(n)
    number_seen.append(n)
  return list(set(list_of_duplicates))
