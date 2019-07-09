open PfxAst
open Printf

type state = command list * int list

(*
let string_of_stack stack = sprintf "[%s]" (String.concat ";" (List.map string_of_int stack))
*)
let string_of_stack stack = sprintf "[%s]" (String.concat ";" (List.map string_of_command stack))

let string_of_state (cmds,stack) =
  (match cmds with
   | [] -> "no command"
   | cmd::_ -> sprintf "executing %s" (string_of_command cmd))^
    (sprintf " with stack %s" (string_of_stack stack))

(* Question 4.2 *)
let step state =
  match state with
  | [], _ -> Error("Nothing to step", state)
  | (Pop|Exec)::_, [] -> Error("Nothing in pile", state)
  | (Add|Mul|Div|Sub|Rem|Swap|Get)::_, (_::[]|[]) -> Error("Not enough elements", state)
  (*
  | (Add|Mul|Div|Sub|Rem|Swap)::_, (a::b::s) when a, b != Int i, Int j -> Error("Not an Int Data type", state)
  *)
  (* Valid configurations *)
  | Pop::q, _::s -> Ok (q, s)
  | Push(i)::q, s -> Ok (q, [Int i]@s) 
  | Swap::q, i::j::s -> Ok (q, j::i::s)
  | Add::q, (Int i)::(Int j)::s -> Ok (q, [Int (i + j)]@s)
  | Sub::q, (Int i)::(Int j)::s -> Ok (q, [Int (i - j)]@s)
  | Mul::q, (Int i)::(Int j)::s -> Ok (q, [Int (i * j)]@s)
  | Div::q, (Int i)::(Int j)::s -> Ok (q, [Int (i / j)]@s)
  | Rem::q, (Int i)::(Int j)::s -> Ok (q, [Int (i mod j)]@s)
  (* Question 9, executable sequence, exec, get -> function and application support *)
  | Q(ins)::q, s -> Ok (q, [Q ins]@s)
  | Exec::q, exe::s ->
      begin
        match exe with
        | Q ins -> Ok (ins@q, s) (* e is a list, so [..]@[..] *)
        | _ -> Error("No Sequence to Execute", state)
      end 
  | Get::q, (Int i)::s -> 
      begin
        if List.length s <= i then Error("Stack not large enough for Get("^(string_of_int i)^")", state)
        else Ok(q, [List.nth s i]@s) 
      end
      

let eval_program (numargs, cmds) args =
  let rec execute = function
    | [], []    -> Ok None
    (* | [], v::_  -> Ok (Some v) *)
    | [], (Int v)::_  -> Ok (Some v)
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
