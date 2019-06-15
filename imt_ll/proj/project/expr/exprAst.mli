(* The expression type *)
type expression =
    Const of int
  | Var of string
  | Binop of BinOp.t * expression * expression
  | Uminus of expression
  (* For function support *)
  | App of expression * expression
  | Fun of string * expression
  (* For Let Suppor *)
  | Let of expression

(* Free variables support *)
type free_v =
  | Fv of string
  | Pos of int

(* Converting an expression to a string for printing *)
val string_of_expr : expression -> string

val string_of_fvl : (free_v * free_v) list -> string