open ExprAst
open PfxAst

(*
let rec generate = function
  | Const c -> failwith "To implement"
  | Binop(op,e1,e2) -> failwith "To implement"
  | Uminus e -> failwith "To implement"
  | Var v -> failwith "Not yet supported"
*)

(* 5.2 *)
let rec generate = function
  | Const c -> [Push c]
  | Binop(Badd,e1,e2) -> [Push e2 Push e1 Add] 
  | Binop(Bsub,e1,e2) -> [Push e2 Push e1 Sub]
  | Binop(Bmul,e1,e2) -> [Push e2 Push e1 Mul]
  | Binop(Bdiv,e1,e2) -> [Push e2 Push e1 Div]
  | Binop(Bmod,e1,e2) -> [Push e2 Push e1 Mod]
(* Uminus ?? *)
  | Uminus e -> [-e]
  | Var v -> failwith "Not yet supported"
