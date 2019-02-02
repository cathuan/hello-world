"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" General
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

syntax on
set nocompatible
set showcmd

" Highlight search patterns
set hlsearch

" Always show current position
set ruler
" Highlight current line
set cul
" Show line numbers
set number
" use mouse
set mouse=a
" set to auto read when a file is changed from the outside
set autoread

set wildmenu                    " Show list instead of just completing
set wildmode=list:longest,full  " Command <Tab> completion, list matches, then longest common part, then all.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" space and tab and indent
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set autoindent
set smartindent
set tabstop=4    "  1 tab == 4 spaces
set shiftwidth=4 "  1 tab == 4 spaces
set expandtab    "  Use spaces instead of tabs
"" show ALL white spaces as dot
set listchars=trail:·
set list

" backspace works like in other editor
set backspace=indent,eol,start

highlight ColorColumn ctermbg=gray
set colorcolumn=120

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" move between lines and panes
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l

" move on wrapped lines
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk
nnoremap <Down> gj
nnoremap <Up> gk
vnoremap <Down> gj
vnoremap <Up> gk
inoremap <Down> <C-o>gj
inoremap <Up> <C-o>gk

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Plugins
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'altercation/vim-colors-solarized'
Plugin 'tomasr/molokai'
"Plugin 'davidhalter/jedi-vim'
Plugin 'vim-scripts/taglist.vim'
Plugin 'scrooloose/syntastic'
Plugin 'jiangmiao/auto-pairs'
Plugin 'vim-scripts/The-NERD-tree'
"Plugin 'klen/python-mode'
Plugin 'tell-k/vim-autopep8'
"Plugin 'Valloric/YouCompleteMe'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
Plugin 'Lokaltog/vim-powerline'
Plugin 'Shougo/neocomplete'

call vundle#end()

filetype on
filetype plugin indent on


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" set color scheme
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
syntax enable
set background=dark
"colorscheme molokai
"let g:rehash256=1
let g:solarized_termcolors=256
colorscheme solarized


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" set jedi
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"let g:jedi#goto_command            = "<leader>d"
"let g:jedi#goto_assignments_command = "<leader>g"
"let g:jedi#goto_definitions_command = "<leader>d"
"let g:jedi#documentation_command    = "K"
"let g:jedi#usages_command           = "<leader>n"
"let g:jedi#completions_command      = "<C-Space>"
"let g:jedi#rename_command           = "<leader>rname"


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" set taglist
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" automatically open the taglist window, when start Vim
let g:Tlist_Auto_Open = 1
"" close vim if the only window left open is taglist
let g:Tlist_Exit_OnlyWindow = 1


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" set NERDTree
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" open NERDTree automatically when vim starts up if no files were specified
"autocmd StdinReadPre * let s:std_in=1
"autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
"" close vim if the only window left open is NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
"" open a NERDTree automatically when vim starts up
"autocmd vimenter * NERDTree
"" ignore pyc file
let NERDTreeIgnore=['\.pyc']
nmap <C-n> :NERDTreeToggle<CR>


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" set Syntastic
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list            = 1
let g:syntastic_check_on_open            = 1
let g:syntastic_check_on_wq              = 0
let g:syntastic_python_checkers          = ['pyflakes', 'pep8']


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" customize PEP8
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" E128 continuation line under-indented for visual indent
" E501 line too long
let g:syntastic_python_pep8_args="--ignore=E128,E501,E226"
let g:autopep8_max_line_length=100


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" customize vim-markdown
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" disable folding configuration
let g:vim_markdown_folding_disabled = 1
" enable latex support
let g:vim_markdown_math = 1


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" customize neocomplete
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Disable AutoComplPop.
let g:acp_enableAtStartup = 0
" Use neocomplete.
let g:neocomplete#enable_at_startup = 1
" Use smartcase.
let g:neocomplete#enable_smart_case = 1
" Set minimum syntax keyword length.
let g:neocomplete#sources#syntax#min_keyword_length = 3
let g:neocomplete#lock_buffer_name_pattern = '\*ku\*'

" Define dictionary.
let g:neocomplete#sources#dictionary#dictionaries = {
    \ 'default' : '',
    \ 'vimshell' : $HOME.'/.vimshell_hist',
    \ 'scheme' : $HOME.'/.gosh_completions'
        \ }

" Define keyword.
if !exists('g:neocomplete#keyword_patterns')
    let g:neocomplete#keyword_patterns = {}
endif
let g:neocomplete#keyword_patterns['default'] = '\h\w*'

" Plugin key-mappings.
inoremap <expr><C-g>     neocomplete#undo_completion()
inoremap <expr><C-l>     neocomplete#complete_common_string()

" Recommended key-mappings.
" <CR>: close popup and save indent.
inoremap <silent> <CR> <C-r>=<SID>my_cr_function()<CR>
function! s:my_cr_function()
  return (pumvisible() ? "\<C-y>" : "" ) . "\<CR>"
  " For no inserting <CR> key.
  "return pumvisible() ? "\<C-y>" : "\<CR>"
endfunction
" <TAB>: completion.
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"
" <C-h>, <BS>: close popup and delete backword char.
inoremap <expr><C-h> neocomplete#smart_close_popup()."\<C-h>"
inoremap <expr><BS> neocomplete#smart_close_popup()."\<C-h>"
" Close popup by <Space>.
"inoremap <expr><Space> pumvisible() ? "\<C-y>" : "\<Space>"

" AutoComplPop like behavior.
"let g:neocomplete#enable_auto_select = 1

" Shell like behavior(not recommended).
"set completeopt+=longest
"let g:neocomplete#enable_auto_select = 1
"let g:neocomplete#disable_auto_complete = 1
"inoremap <expr><TAB>  pumvisible() ? "\<Down>" : "\<C-x>\<C-u>"

" Enable omni completion.
autocmd FileType css setlocal omnifunc=csscomplete#CompleteCSS
autocmd FileType html,markdown setlocal omnifunc=htmlcomplete#CompleteTags
autocmd FileType javascript setlocal omnifunc=javascriptcomplete#CompleteJS
autocmd FileType python setlocal omnifunc=pythoncomplete#Complete
autocmd FileType xml setlocal omnifunc=xmlcomplete#CompleteTags

" Enable heavy omni completion.
if !exists('g:neocomplete#sources#omni#input_patterns')
  let g:neocomplete#sources#omni#input_patterns = {}
endif
"let g:neocomplete#sources#omni#input_patterns.php = '[^. \t]->\h\w*\|\h\w*::'
"let g:neocomplete#sources#omni#input_patterns.c = '[^.[:digit:] *\t]\%(\.\|->\)'
"let g:neocomplete#sources#omni#input_patterns.cpp = '[^.[:digit:] *\t]\%(\.\|->\)\|\h\w*::'

" For perlomni.vim setting.
" https://github.com/c9s/perlomni.vim
let g:neocomplete#sources#omni#input_patterns.perl = '\h\w*->\h\w*\|\h\w*::'






