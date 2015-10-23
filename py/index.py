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

index = vimutils.pos_to_index( vim.current.buffer, vim.current.window.cursor )
source = vimutils.unlines( vim.current.buffer )

arglist = argformat.get_arglist_at( source, index )
arglist_startpos = vimutils.index_to_pos( source, arglist.start_index )

fmt = multiline.MultilineFormatter( source, arglist )

print( fmt.apply() )
