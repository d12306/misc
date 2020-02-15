##Vim Opeations:

0(moves to the left end of a line),$(moves to the right end),v（visual mode)

k,j(move up and down) h,l(moves left and right)

w,b:moves forward and backward in one word. 

e:moves to the end of the word. 

control u and d(move up and down in large steps)

o command, from the normal mode to the insert mode and insert a new line. 

O command, insert above

c(change, to the insert mode) and d(delete) u(undo) r(replace, need repress) control r(redo) y(copy) p(paste) v(选中）tilde(改变大小写）

x(delet a char) dw(delete a word) de(delete to the end of a word) dd(delete a line) cc(delete a line) yy(copy the line) yw(copy a word)

4j(count 4 times for j command) ci[(change inside the bracket) 7dw(delete 7 words)
G(go to the end of the file) gg(all the way up)

/:search sign

fo(find o behind)
Fo(find o before)

add in ~/.vimrc:
```
set number

set nocompatible

syntax on
```
