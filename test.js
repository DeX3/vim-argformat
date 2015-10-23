
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
