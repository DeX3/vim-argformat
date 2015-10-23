if !has( 'python' )
    echohl WarningMsg
    echom  "UltiSnips requires py >= 2.7 or py3"
    echohl None
endif

function! ArgFormat()
    pyfile py/index.py
endfunction
