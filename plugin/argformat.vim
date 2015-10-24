if !has( 'python' )
    echohl WarningMsg
    echom  "argformat requires py >= 2.7 or py3"
    echohl None
endif

let g:argformat_spaces_around_arglist = 0

let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! ArgFormat( style )
    execute 'pyfile ' . s:path . '/py/index.py'
endfunction

command! ArgFormatConcise call ArgFormat( 'concise' )
command! ArgFormatMultiline call ArgFormat( 'multiline' )
command! ArgFormatOnPar call ArgFormat( 'onpar' )
