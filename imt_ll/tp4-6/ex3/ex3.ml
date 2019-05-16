type 'a binary_tree =
    | Empty
    | Node of 'a * 'a binary_tree * 'a binary_tree;;

let rec add_node x tree = match tree with
| Empty -> Node(x, Empty, Empty)
| Node(v, left, right) ->
if (v = x) then tree (* this would eliminate the repetition of a same case; that is not what we want though *)
else if (x < v) then Node(v, add_node x left, right)
else Node(v, left, add_node x right);;

let rec build_binary_tree list = match list with
|[] -> Empty
|h::t -> add_node h (build_binary_tree t);;

(* WRONG *)
let rec sort_from_binary tree = match tree with
| Empty -> []
| Node (v, Empty, Empty) -> [v]
| Node (v, left, right) -> left@v@right;;

let rec sort_from_binary tree = match tree with
| Empty -> []
| Node (v, left, right) -> (sort_from_binary left)@(v :: sort_from_binary right);;
(* I don't understand the difference between the las command of sort binary tree *)

(*

it can also bee written as:

let rec sort_from_binary  = function
| Empty -> []
| Node (v, left, right) -> (sort_from_binary left)@(v :: sort_from_binary right);;
*)

let t =  Node(3, Node(2, Empty, Empty), Node(5, Empty, Empty));;
add_node 4 t;;
let mytr = build_binary_tree [3;2;5;7;1];;
sort_from_binary mytr;;

