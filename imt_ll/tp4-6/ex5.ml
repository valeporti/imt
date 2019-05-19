(* How could I maket this work? 
type 'a lwp =
| Empty 
| Header of 'a list
| Main of 'a
| Tail of 'a list;;

let build_lwp2 = function 
| [] -> Empty
| h::t -> Header []; Main h; Tail t;;
*)

type 'a lwp =
| Empty
| List of 'a list * 'a * 'a list

let build_lwp = function 
| [] -> Empty (* pourquoi?? Nous n'allons en réalité jamais avoir ce cas mais si l'on ne met ce cas là mais par exemple List([], Empty, []), le type est 'a lwp list -> 'a lwp lwp = <fun> *)
| h::t -> List([], h, t);;

(* V 2.0
type 'a lwp = List of 'a list * 'a * 'a list;;

let build_lwp = function 
| [] -> failwith "Empty list"
| h::t -> List([], h, t);;

*)

(* returns the current position element *)
let current = function
| Empty -> -1
| List(h, p, t) -> p;;

(* V 2.0 
let current = function
| List(h, p, t) -> p;;
*)

let mylist = build_lwp [1; 2; 3; 4; 5; 6];;
current mylist;;


let move_left = function 
| Empty -> ()
| List(left, pos, right) ->
if (right = []) then List(left, pos, right)
else left@[pos];  


(* Is there a better way to program these 4 func? *)
let remove_first = function
| [] -> []
| h::t -> t;; 

let get_first l = match l with 
| [] -> failwith "No first element in list"
| h::t -> h;;

let rec last_element = function
| [] -> failwith "No last element to remove"
| [just_one] -> just_one 
| first::rest_of_list -> last_element rest_of_list;;

let rec remove_last = function 
| [] -> failwith "No last element to remove"
| [just_one] -> []
| first::rest_of_list -> first::(remove_last rest_of_list);; (* or [first]@(...) *)


let move_right = function 
| Empty -> failwith "Error in moving right"
| List(left, pos, []) -> List(left, pos, [])
| List(left, pos, right) -> List(left@[pos], get_first right, remove_first right);;

(* V 2.0
let move_right = function 
| List (l, p, []) -> failwith "incorrect right move"
| List (l, p, rh::rt) -> List(l@[p], rh, rt);; 
*)

(*
let move_left = function 
| Empty -> Empty
| List(left, pos, right) ->
if (right = []) then List(left, pos, right)
else List(left@[pos], (function | [] -> [] | h::t -> h) right, remove_first right);; 
*)

let move_left = function 
| Empty -> failwith "Error in moving left"
| List([], pos, right) -> List([], pos, right)
| List(left, pos, right) -> List(remove_last left, last_element left, (last_element left)::right);;

let new_list = move_right mylist;;
let new_list = move_right new_list;;
let new_list = move_left new_list;;
let new_list = move_left new_list;;

(*
commment on peut lire
('a -> 'b) -> 'a list -> 'b list
avec un arbre ?
*)

