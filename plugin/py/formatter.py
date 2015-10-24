import re
import vimutils

INDENT_STYLE_SPACES = 'spaces'
INDENT_STYLE_TABS = 'tabs'

class Formatter(object):

  def __init__( self,
                source,
                arglist,
                indent_style = INDENT_STYLE_SPACES,
                indent_size = 2 ):
    self.source = source
    self.arglist = arglist
    self.indent_style = indent_style
    self.indent_size = indent_size

  def starting_indent( self ):
    line = self.starting_line()
    m = re.match( '\\s*', line )
    return m.group( 0 )

  def starting_line( self ):
    return self.line_at( self.arglist.start_index )

  def arglist_prefix( self ):
    start = self.source.rfind( '\n', 0, self.arglist.start_index ) + 1
    return self.source[start:self.arglist.start_index]

  def arglist_suffix( self ):
    end = self.source.find( '\n', self.arglist.end_index )
    return self.source[self.arglist.end_index:end]

  def line_at( self, i ):
    start = self.source.rfind( '\n', 0, i ) + 1

    end = self.source.find( '\n', i )
    if end == -1:
      end = 0

    return self.source[start:end]


