import formatter

class OnParFormatter( formatter.Formatter ):

  def __init__( self, *args, **kwargs ):
    self.spaces_around_arglist = kwargs.pop( "spaces_around_arglist", True )
    super( self.__class__, self ).__init__( *args, **kwargs )

  def apply( self ):

    if len(self.arglist.args) < 2:
      return

    prefix = self.arglist_prefix()
    original_indent = self.starting_indent()

    ret = prefix

    insert_additional_space = (self.spaces_around_arglist and ret[-1] != ' ')
    if insert_additional_space:
      ret += ' '

    indent = ""
    if self.indent_style == formatter.INDENT_STYLE_TABS:
      size = original_indent.count( '\t' ) * self.indent_size
      size += original_indent.count( ' ' )
      if insert_additional_space:
        size += 1
      target_size = size + self.indent_size
      target_tab_count = target_size / self.indent_size
      target_space_count = target_size % self.indent_size
      indent = target_tab_count * '\t' + target_space_count * ' '
    else:
      indent = len(prefix) * ' '
      if insert_additional_space:
        indent += ' '
    
    ret += self.arglist.args[0] + ',\n'

    for arg in self.arglist.args[1:-1]:
      ret += indent + arg + ',\n'
      
    suffix = self.arglist_suffix()
    ret += indent + self.arglist.args[-1] 

    if self.spaces_around_arglist and ret [-1] != ' ' and suffix[0] != ' ':
      ret += ' '

    ret += suffix

    return ret


