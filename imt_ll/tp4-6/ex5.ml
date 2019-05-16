(* How could I maket this work? *)
type 'a lwp =
| Empty 
| Header of 'a list
| Main of 'a
| Tail of 'a list;;

(*
type ’a listpos =
| Empty
| List of ’a list * ’a * ’a list
*)

(* this one works for listpos *)
let build_lwp = function 
| [] -> Empty
| h::t -> List([], h, t);;

let build_lwp2 = function 
| [] -> Empty
| h::t -> Header []; Main h; Tail t;;

(* returns the current position element *)
let current = function
| Empty -> -1
| (h, p, t) -> p;;
