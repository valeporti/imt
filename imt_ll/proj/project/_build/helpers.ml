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
| EOF -> print_string "EOF"
| INT i -> print_string ("INT: "^(string_of_int i))

(*
rule count value = parse
  | [^'a']*  { count value lexbuf }
  | 'a'    { count (value + 1) lexbuf }
  | eof    { value }

{
  let count_a s = let buffer = Lexing.from_string s in count 0 buffer
}
*)
