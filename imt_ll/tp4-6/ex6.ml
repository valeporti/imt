type expression = 
| Const of float
| Sum of expression * expression
| Diff of expression * expression 
| Prod of expression * expression
| Div of expression * expression;;

(*
let eval = function
| "" -> ""
| a ^ "+" ^ b -> Sum(a, b);;

let eval = function
| "^$" -> ""
| "(\d+.*\d*)+(\d+.*\d*)" -> Sum(a, b);;
*)

let rec eval env = function
| Const c -> c
| Sum(a, b) -> eval env a +. eval env b
| Diff(a, b) -> eval env a -. eval env b
| Prod(a, b) -> eval env a *. eval env b
| Div(a, b) -> eval env a /. eval env b;;

