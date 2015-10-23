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

class TestGetArguments( unittest.TestCase ):

  def test_get_args1( self ):
    source = '''a, b, c'''
    self.assertEqual(
      argformat.get_args( source ),
      ( ['a','b','c'], len( source ) )
    )

  def test_get_args2( self ):
    source = 'a, { a: b }, c'
    self.assertEqual(
      argformat.get_args( source ),
      ( ['a','{ a: b }','c'], len(source) )
    )

  def test_get_args3( self ):
    source = 'a, [1, 2, 3], c'
    self.assertEqual(
      argformat.get_args( source ),
      ( ['a','[1, 2, 3]','c'], len(source) )
    )

  def test_get_args4( self ):
    source = 'a, [1, 2, 3], function( a, b ) { return( 3-a+b ); }'
    self.assertEqual(
      argformat.get_args( source ),
      ( ['a','[1, 2, 3]','function( a, b ) { return( 3-a+b ); }'], len(source) )
    )

  def test_get_args5( self ):
    source = 'a, [1, { a: [2,3] }, 3], c'
    self.assertEqual(
      argformat.get_args( source ),
      ( ['a','[1, { a: [2,3] }, 3]','c'], len(source) )
    )

  def test_get_args6( self ):
    source = 'a, "b, c", c'
    self.assertEqual(
      argformat.get_args( source ),
      ( ['a','"b, c"','c'], len(source) )
    )

  def test_get_args6( self ):
    source = 'a, "b, \\"c, muaha", c'
    self.assertEqual(
      argformat.get_args( source ),
      ( ['a','"b, \\\"c, muaha"','c'], len(source) )
    )

  def test_get_args7( self ):
    source = 'a, [1, { a: [2,3] }, 3], c, d ), e'
    self.assertEqual(
      argformat.get_args( source ),
      ( ['a','[1, { a: [2,3] }, 3]','c', 'd'], len(source) - 4 )
    )


  def test_apply_format1():
    source = '''
var some_code = bla;
call( a, b, c );
another_call( d, e );
'''.strip()

    self.assertEqual(
      argformat.apply_format( argformat.FMT_MULTILINE, source, 20 ),
      '''
var some_code = bla;
call(
  a,
  b,
  c
);
another_call( d, e );
    )
# 
#   def test_get_args_in_source2( self ):
#     self.assertEqual(
#       argformat.get_args_in_source('''
# var some_code = bla;
# call( a, b, c );
# another_call( d, e );
#       ''', 57),
#       [ 'd', 'e' ]
#     )

if __name__ == '__main__':
  unittest.main()
