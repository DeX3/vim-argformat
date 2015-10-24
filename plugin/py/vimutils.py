def unlines( lines ):
  return '\n'.join( lines )

def pos_to_index( lines, pos ):
  row, col = pos
  row -= 1
  total = reduce( lambda sum, line: sum + len(line), lines[0:row], 0 )
  return total + row + col

def index_to_pos( lines, i ):

  total = 0
  line = 0
  col = i
  l = 0

  while total <= i and line < len(lines):
    l = len( lines[line] )
    line += 1
    total += l + 1

  return (line, i - (total - l - 1))
