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
| [] -> Empty
| h::t -> List([], h, t);;

(* returns the current position element *)
let current = function
| Empty -> -1
| List(h, p, t) -> p;;

let mylist = build_lwp [4; 3; 3; 9; 3; 9];;
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
| first::rest_of_list -> first::(remove_last rest_of_list);;


let move_right = function 
| Empty -> failwith "Error in moving right"
| List(left, pos, []) -> List(left, pos, [])
| List(left, pos, right) -> List(left@[pos], get_first right, remove_first right);;

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


