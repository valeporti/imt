(* The expression type *)
type expression =
    Const of int
  | Var of string
  | Binop of BinOp.t * expression * expression
  | Uminus of expression
  (* For function support *)
  | App of expression * expression
  | Fun of string * expression
  (* For Let Support *)
  | Let of string * expression

(* Free variables support *)
type env_v =
  | Empty
  | Fv of string
  | Pos of int

(* Converting an expression to a string for printing *)
val string_of_expr : expression -> string

val string_of_env : (env_v * env_v) list -> string

val string_of_e : expression -> string