	
let f x = 2 * x;;

let rec map f l = match l with
|[] -> []
|h::t -> (f h)::(map f t);;

let rec mapv2 f l = (function
|[] -> []
|h::t -> (f h)::(map f t))l;;

let rec print_list = function 
|[] -> []
| e::l -> print_int e ; print_string " " ; print_list l;;

print_string "map v 1\n";;
let mapval1 = map f [2; 3];;
print_list mapval1;;
print_string "\n";;

print_string "map v 2\n";;
let mapval2 = mapv2 f [2; 3];;
print_list mapval2;;
print_string "\n";;
