class Pair:
  def __init__( self, opener, closer=None, escape=None ):
    self.opener = opener
    self.closer = closer or opener
    self.escape = escape;

  def has_opener( self, ch ):
    return self.opener == ch

  def has_closer( self, ch ):
    return self.closer == ch

  def has_escape( self, ch ):
    return self.escape == ch

  def __str__( self ):
    return self.opener + ' ' + self.closer

class ArgList:
  def __init__( self, start_index = 0, args = [], end_index = 0 ):
    self.args = args
    self.start_index = start_index
    self.end_index = end_index

PAIRS = [
  Pair( '(', ')' ),
  Pair( '[', ']' ),
  Pair( '{', '}' ),
  Pair('"', '"', '\\'),
  Pair("'", "'", '\\')
]

SEPARATOR = ','
ARGLIST_CONTAINER = Pair( '(', ')' )

FMT_ONELINE = 0
FMT_MULTILINE = 1
FMT_MULTILINE_ON_PAR = 2 

def get_arglist_at( source,
                    i,
                    indent_style = 'spaces',
                    indent_size = '2' ):

  start = get_nearest_arglist_start( source, i )
  a, l = get_args( source[start:] )
  return ArgList( start, a, start + l )


def get_nearest_arglist_start( source, i ):

  while i > 0:
    if ARGLIST_CONTAINER.has_opener( source[i-1] ) :
      return i
    i -= 1

  return None


def get_args( argstr ):
  stack = []
  args = []

  total_args_length = 0
  current_arg = ""
  escaped = False

  for c in argstr:

    current_pair = None
    if len(stack) > 0:
      current_pair = stack[-1]

    if escaped:
      escaped = False
      current_arg += c
      continue

    new_pair = find_pair_with_opener( c )
    if current_pair is not None:
      if current_pair.has_escape( c ):
        escaped = True
        current_arg += c
        continue
      elif current_pair.has_closer( c ):
        stack.pop()
        current_arg += c
        continue
    elif c == ')':
      break

    if new_pair is not None:
      stack.append( new_pair )
      current_arg += c
    elif current_pair is None and c == SEPARATOR:
      total_args_length += len(current_arg)
      args.append( current_arg.strip() )
      current_arg = ''
    else:
      current_arg += c

  total_args_length += len( args ) + len( current_arg )
  args.append( current_arg.strip() )

  return args, total_args_length

def find_pair_with_opener( ch ):
  return next( (p for p in PAIRS if p.has_opener(ch)), None )
