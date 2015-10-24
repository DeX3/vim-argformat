#!/usr/bin/env python


# make sure the parent directory is available
import os,sys,inspect
currentdir = os.path.dirname(
  os.path.abspath(
    inspect.getfile(inspect.currentframe())
  )
)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import unittest
import argformat
import formatter
import multiline
import concise
import onpar

source = '''
var fs = require( 'fs' );

module.exports = function( a, b, c ) {

    console.log( "testaroni", 3, { foo: bar } );
    return anotherHelper(
        44,
        12,
        88
    );
};

function helper( test,
                 suff,
                 bla ) {

  return 3;
}

funtion anotherHelper(
    foo,
    bar,
    baz
) {
    return helper( baz, bar, foo );
}
'''.strip()

class TestFormatter( unittest.TestCase ):

  # def test_multiline1( self ):
  #   index = 100

  #   arglist = argformat.get_arglist_at( source, index )
  #   fmt = multiline.MultilineFormatter( source, arglist )
  #   print( fmt.apply() )

  # def test_concise1( self ):
  #   index = 100

  #   arglist = argformat.get_arglist_at( source, index )
  #   fmt = concise.ConciseFormatter( source, arglist )
  #   print( fmt.apply() )

  def test_onpar1( self ):
    index = 100

    arglist = argformat.get_arglist_at( source, index )
    fmt = onpar.OnParFormatter( source, arglist )
    print( fmt.apply() )
    
if __name__ == '__main__':
  unittest.main()
