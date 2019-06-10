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
(*
let rec generate = function
  | Const c -> [Push c]
  | Binop(Badd,e1,e2) -> [Push e2; Push e1; Add] 
  | Binop(Bsub,e1,e2) -> [Push e2; Push e1; Sub]
  | Binop(Bmul,e1,e2) -> [Push e2; Push e1; Mul]
  | Binop(Bdiv,e1,e2) -> [Push e2; Push e1; Div]
  | Binop(Bmod,e1,e2) -> [Push e2; Push e1; Mod]
  | Uminus e -> [-e]
  | Var v -> failwith "Not yet supported"
*)

let rec generate = function
  | Const c -> [Push c]
  | Binop(op,e1,e2) -> 
		begin
			match op with
			| Badd -> (generate e2)@(generate e1)@[Add]
			| Bsub -> (generate e2)@(generate e1)@[Sub]
			| Bmul -> (generate e2)@(generate e1)@[Mul]
			| Bdiv -> (generate e2)@(generate e1)@[Div]
			| Bmod -> (generate e2)@(generate e1)@[Rem]
		end		
  | Uminus e -> (generate e)@(generate (Const 0))@[Sub]
  | Var v -> failwith "Not yet supported"
