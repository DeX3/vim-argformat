import formatter

class ConciseFormatter( formatter.Formatter ):

  def __init__( self, *args, **kwargs ):
    self.spaces_around_arglist = kwargs.pop( "spaces_around_arglist", True )
    super( self.__class__, self ).__init__( *args, **kwargs )

  def apply( self ):

    ret = self.arglist_prefix()

    if self.spaces_around_arglist and ret[-1] != ' ':
      ret += ' '

    for arg in self.arglist.args[:-1]:
      ret += arg + ', '

    ret += self.arglist.args[-1]

    suffix = self.arglist_suffix();
    if self.spaces_around_arglist and ret [-1] != ' ' and suffix[0] != ' ':
      ret += ' '

    ret += suffix

    return ret


