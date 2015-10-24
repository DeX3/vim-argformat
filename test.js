
var fs = require( 'fs' );

module.exports = function( a, b, c ) {

    console.log( "testaroni", 3, { foo: bar } );

    test( a );

    return anotherHelper(
        44,
        12,
        88
    );
};

function helper( test,
                 suff,
                 suff ) {

  return 3;
}

funtion anotherHelper(
    foo,
    bar,
    baz
) {
    return helper( baz, bar, foo );
}
