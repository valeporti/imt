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
  | (Int i)::_, _ -> Error("Integer in Q", state)
  (*
  | (Add|Mul|Div|Sub|Rem|Swap)::_, (a::b::s) when a, b != Int i, Int j -> Error("Not an Int Data type", state)
  *)
  (* Valid configurations *)
  | Pop::q, _::s -> Ok (q, s)
  | Push(i)::q, s -> Ok (q, [Int i]@s) 
  | Swap::q, i::j::s -> Ok (q, j::i::s)
  | Add::q, (Int i)::(Int j)::s -> Ok (q, [Int (j + i)]@s)
  | Sub::q, (Int i)::(Int j)::s -> Ok (q, [Int (j - i)]@s)
  | Mul::q, (Int i)::(Int j)::s -> Ok (q, [Int (j * i)]@s)
  | Div::q, (Int i)::(Int j)::s -> if (i != 0) then Ok (q, [Int (j / i)]@s) else Error("Division by zero", state)
  | Rem::q, (Int i)::(Int j)::s -> if (i != 0) then Ok (q, [Int (j mod i)]@s) else Error("Remainder by zero", state)
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
        else Ok(q, [List.nth s ((List.length s) - i - 1)]@s) (* Read the stack from right to left *) 
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



(* ------------------- PRINTING VALUES VERSION OF step ------------------- *)
(* ------------------- See how the stack behaves ------------------- *)

let steppp state =
  match state with
  | [], _ -> Error("Nothing to step", state)
  | (Pop|Exec)::_, [] -> Error("Nothing in pile", state)
  | (Add|Mul|Div|Sub|Rem|Swap|Get)::_, (_::[]|[]) -> Error("Not enough elements", state)
  | (Int i)::_, _ -> Error("Integer in Q", state)
  (*
  | (Add|Mul|Div|Sub|Rem|Swap)::_, (a::b::s) when a, b != Int i, Int j -> Error("Not an Int Data type", state)
  *)
  (* Valid configurations *)
  | Pop::q, _::s -> print_string ((string_of_state state)^"\n"); Ok (q, s)
  | Push(i)::q, s -> print_string ((string_of_state state)^"\n"); Ok (q, [Int i]@s) 
  | Swap::q, i::j::s -> print_string ((string_of_state state)^"\n"); Ok (q, j::i::s)
  | Add::q, (Int i)::(Int j)::s -> print_string ((string_of_state state)^"\n"); Ok (q, [Int (j + i)]@s)
  | Sub::q, (Int i)::(Int j)::s -> print_string ((string_of_state state)^"\n"); Ok (q, [Int (j - i)]@s)
  | Mul::q, (Int i)::(Int j)::s -> print_string ((string_of_state state)^"\n"); Ok (q, [Int (j * i)]@s)
  | Div::q, (Int i)::(Int j)::s -> print_string ((string_of_state state)^"\n"); Ok (q, [Int (j / i)]@s)
  | Rem::q, (Int i)::(Int j)::s -> print_string ((string_of_state state)^"\n"); Ok (q, [Int (j mod i)]@s)
  (* Question 9, executable sequence, exec, get -> function and application support *)
  | Q(ins)::q, s -> print_string ((string_of_state state)^"\n"); Ok (q, [Q ins]@s)
  | Exec::q, exe::s ->
      begin
        print_string ((string_of_state state)^"\n");
        match exe with
        | Q ins -> Ok (ins@q, s) (* e is a list, so [..]@[..] *)
        | _ -> Error("No Sequence to Execute", state)
      end 
  | Get::q, (Int i)::s -> 
      begin
        print_string ("Get element: "^(string_of_int i)^"\n");
        print_string ("Get s len: "^(string_of_int (List.length s))^"\n");
        print_string ("Get -> : "^(string_of_command (List.nth s ((List.length s) - i - 1)))^"\n");
        print_string ((string_of_state state)^"\n");
        if List.length s <= i then Error("Stack not large enough for Get("^(string_of_int i)^")", state)
        else Ok(q, [List.nth s ((List.length s) - i - 1)]@s) (* Read the stack from right to left *) 
      end

let eval_program_pp (numargs, cmds) args =
  let rec execute = function
    | [], []    -> Ok None
    (* | [], v::_  -> Ok (Some v) *)
    | [], (Int v)::_  -> Ok (Some v)
    | state ->
        begin
          match steppp state with
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
(*let insert_args cmds args = match cmds, args with*)


