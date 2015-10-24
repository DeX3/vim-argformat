import formatter

class MultilineFormatter( formatter.Formatter ):

  def __init__( self, *args, **kwargs ):
    super( self.__class__, self ).__init__( *args, **kwargs )

  def apply( self ):

    if len(self.arglist.args) < 1:
      return

    prefix = self.arglist_prefix()
    original_indent = self.starting_indent()

    indent = ' ' * self.indent_size
    if self.indent_style == formatter.INDENT_STYLE_TABS:
      indent = '\t'

    new_indent = original_indent + indent;

    ret = prefix + '\n'
    
    for arg in self.arglist.args[:-1]:
      ret += new_indent + arg + ',\n'

    ret += new_indent + self.arglist.args[-1] + '\n'
    ret += original_indent + self.arglist_suffix()

    return ret


