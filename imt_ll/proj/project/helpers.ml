open PfxLexerTest

let go tk lx = tk lx


let print_token = function
| _ -> print_string "hello2"

let print_tk = function
| PLUS -> print_string "Add"
| MINUS -> print_string "Sub"
| TIMES -> print_string "Mul"
| DIV -> print_string "Div"
| PUSH -> print_string "Push"
| POP -> print_string "Pop"
| SWAP -> print_string "Swap"
| EOF -> print_string "EOF"
| INT i -> print_string ("INT: "^(string_of_int i))

