vim-argformat
=============

This plugin enables the user to reformat argument lists in function
calls and function definitions. It was developed for Javascript, but it should
work for many C-Style languages (C, C++, Java, C#, etc...).

![argformat screen capture](http://i.imgur.com/2WpLG09.gif)

The plugin designed so that it supports any ','-separated list between '()'.
This enables it to work on function definitions as well. The plugin provides 3
commands, one for formatting an argument list into one of the 3 styles
respectively.

`argformat` will automatically detect your indentation settings for formatting
argument lists.

Styles
------

Currently, argformat supports 3 argument list styles:

    // 'concise'
    methodName( some, parameters, to, the, call, go, here );

    // 'multiline'
    methodName(
        some,
        parameters,
        to,
        the,
        call,
        go,
        here
    );

    // 'on par with call'
    methodName( some,
                parameters,
                to,
                the,
                call,
                go,
                here );

Installation
------------

Just use your favorite plugin manager (I recommend vim-plug,
https://github.com/junegunn/vim-plug).

Requirements
------------

argformat requires your vim to be compiled with python support (+python).

Commands
--------

    :ArgFormatConcise       Format the current argument list in the "concise"
                            style.

    :ArgFormatMultiline     Format the current argument list in the "multiline"
                            style

    :ArgFormatOnPar         Format the current argument list in the "on par with
                            call" style

Options
-------

argformat may be customized with the following options.


`g:argformat_spaces_around_arglist`: Default: 0. When set to 1, argformat will
add/keep spaces between the opening and closing parentheses of the argument
list.
