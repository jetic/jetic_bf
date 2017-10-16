# jetic_bf
## Supported functions:
* Variables:
> from 'A' to 'Z', 'a' to 'z', and system variable '_', '^'.
* '+' and '-':
> '+x' will be '+' repeat x times. '1' in '+1' cannot be omitted.
* ' ':
> space is ignored, so feel free to add ' ' in jetic_bf code to make it easier to read.
* '~':
> '~x' will clear the value of x to 0.
* '=':
> '=ab' means b=a
* If condition '()':
> 'a(CODE)' means code inside can be attached only if a is not zero.
## Test case:
* s+32 i+99 j+10 i[a+1 j-1 ~A A-1 j(A+1) A(~a b+1 j+9) =bx x+48 x. =ax x+48 x. s. i-1 i]
* '>>>>>>>>>>>>>>>>>>>++++++++++++++++++++++++++++++++<<<<<<<<<<+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>++++++++++<[<<<<<<<<+>>>>>>>>>-<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[-]->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[-]>[-]>>>>>>>>>>>[<<<<<<<<<<<<+>+>>>>>>>>>>>-]<<<<<<<<<<<[>>>>>>>>>>>+<<<<<<<<<<<-]<>>>>>>>>>>>>[-]][-]<<<<<<<<<<<[-]<[>>>>>>>>>>>>+<<<<<<<<<<<+<-]>[<+>-]>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[-]>+>>>>>>>>+++++++++<<<<<<<<<<<<[-]>[-]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+>+<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<[-]][-]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[-]<[<<<<<<<<<<<<<<<<<<<<<<<<<<<<<+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+<-]>[<+>-]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[-]<<<<<<<<<<<<<<<<<<<<<<<<<[-]>>>[>>>>>>>>>>>>>>>>>>>>>>+<<<<<<<<<<<<<<<<<<<<<<<<<+>>>-]<<<[>>>+<<<-]>>>>>>>>>>>>>>>>>>>>>>>>>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<<<<<<<<<<<<<<[-]>>[>>>>>>>>>>>>>>>>>>>>>>>+<<<<<<<<<<<<<<<<<<<<<<<<<+>>-]<<[>>+<<-]>>>>>>>>>>>>>>>>>>>>>>>>>++++++++++++++++++++++++++++++++++++++++++++++++.<<<<<.<<<<<<<<<<-]'
* Try bf at https://tio.run/#brainfuck
