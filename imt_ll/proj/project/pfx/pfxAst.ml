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
(* Functions Support *) 
| Q of command list (* it could be (Q) or [] -- Executable sequence *)
| Exec
| Get
| Int of int (* We need this to homologate stack list types *)


type program = int * command list

(* add here all useful functions and types  related to the AST: for instance  string_of_ functions *)

(*let rec string_of_command = function
  | DefineMe -> "to be done" *)

let rec string_of_command = function
| Pop -> "Pop"
| Push i -> "Push "^(string_of_int i)
| Swap -> "Swap"
| Add -> "Add"
| Sub -> "Sub"
| Mul -> "Mul"
| Div -> "Div"
| Rem -> "Rem"
(* Function Support *)
| Q q -> "Seq ["^(String.concat " " (List.map string_of_command q))^"]" (*"Executable Sequence: ["^(String.concat " " (List.map string_of_command q))^"]"*)
| Exec -> "Exec"
| Get -> "Get"
| Int i -> "Int "^(string_of_int i)

let string_of_commands cmds = String.concat " " (List.map string_of_command cmds)

open Printf
let string_of_program (args, cmds) =
  sprintf "%i args: %s\n" args (string_of_commands cmds)
