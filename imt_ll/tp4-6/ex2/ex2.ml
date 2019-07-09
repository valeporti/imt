
let f x = x * 2;;

let rec iterate f n x = match n with
|0 -> x
|1 -> f x
|_ -> f (iterate f (n-1) x);;

let result = iterate f 2 2;;
print_int result;;
print_string "\n";;
