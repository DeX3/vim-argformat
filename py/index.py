import os,sys,inspect
currentdir = os.path.dirname(
  os.path.abspath(
    inspect.getfile(inspect.currentframe())
  )
)
parentdir = os.path.dirname(currentdir)

sys.path.insert(0,currentdir)
import vim
import argformat
import vimutils
import multiline
import concise
import onpar

indent_style = ['tabs', 'spaces'][ int(vim.eval('&expandtab')) ]

indent_size = 2
if indent_style == 'tabs':
  indent_size = vim.eval( '&tabstop' )
else:
  indent_size = vim.eval( '&shiftwidth' )


spaces_around_arglist = 0
if vim.eval('g:argformat_spaces_around_arglist') == '1':
  spaces_around_arglist = 1

index = vimutils.pos_to_index( vim.current.buffer, vim.current.window.cursor )
source = vimutils.unlines( vim.current.buffer )

arglist = argformat.get_arglist_at( source, index + 1 )

style = vim.eval( 'a:style' )
fmt = None
if style == 'concise':
  fmt = concise.ConciseFormatter( source, arglist, spaces_around_arglist )
elif style == 'onpar':
  fmt = onpar.OnParFormatter( source, arglist, spaces_around_arglist )
elif style == 'multiline':
  fmt = multiline.MultilineFormatter( source, arglist )

if fmt is not None:

  affected_start, col = vimutils.index_to_pos( vim.current.buffer, arglist.start_index )
  affected_end, _ = vimutils.index_to_pos( vim.current.buffer, arglist.end_index )

  formatted = fmt.apply()

  if formatted is not None:
    lines = formatted.split( '\n' )

    vim.current.buffer[affected_start - 1 : affected_end] = lines
    vim.current.window.cursor = (affected_start, col)

else:
  print( "'" + style + "' is not a valid format!" )
