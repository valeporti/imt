(* 4.1 *)
type command = 
| Pop
| Push of int
| Swap
| Add
| Sub
| Mul
| Div
| Rem

type program = int * command list

(* add here all useful functions and types  related to the AST: for instance  string_of_ functions *)

(*let rec string_of_command = function
  | DefineMe -> "to be done" *)

let rec string_of_command = function
| Pop -> "Pop"
| Push i -> "Push of "^(string_of_int i)
| Swap -> "Swap"
| Add -> "Add"
| Sub -> "Sub"
| Mul -> "Mul"
| Div -> "Div"
| Rem -> "Rem"

let string_of_commands cmds = String.concat " " (List.map string_of_command cmds)

open Printf
let string_of_program (args, cmds) =
  sprintf "%i args: %s\n" args (string_of_commands cmds)
