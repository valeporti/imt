open ExprAst
open PfxAst

(*
let rec generate = function
  | Const c -> failwith "To implement"
  | Binop(op,e1,e2) -> failwith "To implement"
  | Uminus e -> failwith "To implement"
  | Var v -> failwith "Not yet supported"
*)

let rec generate = function
  | Const c -> [Push c]
  | Binop(Badd,e1,e2) -> 
  | Uminus e -> failwith "To implement"
  | Var v -> failwith "Not yet supported"
