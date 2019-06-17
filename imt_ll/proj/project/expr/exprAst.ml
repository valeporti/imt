type expression =
  | Const of int
  | Var of string
  | Binop of BinOp.t * expression * expression
  | Uminus of expression
  (* For function support *)
  | App of expression * expression
  | Fun of string * expression
  (* For Let Suppor *)
  | Let of string * expression

(* Free variables support *)
type free_v =
  | Fv of string
  | Pos of int

let rec string_of_expr exp =
  match exp with
  | Const c -> string_of_int c
  | Var v -> v
  | Binop(op, e1, e2) ->
      "(" ^(string_of_expr e1)^ (BinOp.string_of op) ^(string_of_expr e2)^ ")"
  | Uminus e -> "( -"^(string_of_expr e)^ ")"
  (* For function support *)
  | App(e1,e2) -> (string_of_expr e1)^" "^(string_of_expr e2)
  | Fun(v,e) -> "fun "^v^" -> "^(string_of_expr e)
  | Let(v, e1) -> "let "^v^" = "^(string_of_expr e1)^" in "

let string_of_e exp =
  match exp with
  | Const c -> string_of_int c
  | Var v -> v
  | Binop(op, e1, e2) -> "(Binop)"
  | Uminus e -> "( - Uminus )"
  (* For function support *)
  | App(e1,e2) -> "App("^(string_of_expr e1)^", "^(string_of_expr e2)^")"
  | Fun(v,e) -> "fun "^v^" -> "^(string_of_expr e)
  | Let(v, e1) -> "let "^v^" = "^(string_of_expr e1)^" in "

let rec string_of_env = function
| [] -> "EMP\n"
| (Fv(s), Pos(p))::t -> "( "^(s)^", "^(string_of_int p)^" ) || "^(string_of_fvl t)^"\n"