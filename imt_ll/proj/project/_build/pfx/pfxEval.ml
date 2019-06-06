open PfxAst
open Printf

type state = command list * int list

let string_of_stack stack = sprintf "[%s]" (String.concat ";" (List.map string_of_int stack))

let string_of_state (cmds,stack) =
  (match cmds with
   | [] -> "no command"
   | cmd::_ -> sprintf "executing %s" (string_of_command cmd))^
    (sprintf " with stack %s" (string_of_stack stack))

(* Question 4.2 *)
let step state =
  match state with
  | [], _ -> Error("Nothing to step", state)
  | Pop::_, [] -> Error("Nothing in pile", state)
  | (Add|Mul|Div|Sub|Rem|Swap)::_, (_::[]|[]) -> Error("Not enough elements", state)
  (* Valid configurations *)
  | Pop::q, _::s -> Ok (q, s)
  | Push(i)::q, s -> Ok (q, i::s) 
  | Swap::q, i::j::s -> Ok (q, j::i::s)
  | Add::q, i::j::s -> Ok (q, (i + j)::s)
  | Sub::q, i::j::s -> Ok (q, (i - j)::s)
  | Mul::q, i::j::s -> Ok (q, (i * j)::s)
  | Div::q, i::j::s -> Ok (q, (i / j)::s)
  | Rem::q, i::j::s -> Ok (q, (i mod j)::s)

let eval_program (numargs, cmds) args =
  let rec execute = function
    | [], []    -> Ok None
    | [], v::_  -> Ok (Some v)
    | state ->
       begin
         match step state with
         | Ok s    -> execute s
         | Error e -> Error e
       end
  in
  if numargs = List.length args then
    match execute (cmds,args) with
    | Ok None -> printf "No result\n"
    | Ok(Some result) -> printf "= %i\n" result
    | Error(msg,s) -> printf "Raised error %s in state %s\n" msg (string_of_state s)
  else printf "Raised error \nMismatch between expected and actual number of args\n"
