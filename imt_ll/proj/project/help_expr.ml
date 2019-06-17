open ExprLexer

let go tk lx = tk lx

let print_tk_expr = function 
| PLUS   -> print_string "PLUS"      
| MINUS  -> print_string "MINUS"      
| DIV    -> print_string "DIV"    
| TIMES  -> print_string "TIMES"      
| MOD    -> print_string "MOD"    
| LPAR   -> print_string "LPAR"      
| RPAR   -> print_string "RPAR"      
(* For function support *)
| FUN    -> print_string "FUN"    
| RA     -> print_string "RA"    
(* Let Suppor *)
| LET    -> print_string "LET"    
| IN     -> print_string "IN"    
| ASSIGN -> print_string "ASSIGN"  