

(* The main function *)
let main () = 
  print_string "Hello!\n\n";
  try
    let str_pfx_test = "0 Push 2 Push 3 Add" in
    let file_pfx_test = "./tests/tp" in
    let file_expr_test = "./tests/tt" in
    let file_fun_9_pfx = "./tests/tpfun" in
    let wrong_str_pfx_test = "nothing" in
    let file_fun_lamda_pfx = "./tests/tpten" in
    let file_fun_lambda_simp_expr = "./tests/ttfunsimp" in
    let file_fun_lambda_comp_expr = "./tests/ttfun" in
      print_string " ---- OK Test For the ExprToPfx, Q 5 ----\n";
      TestFun.five file_expr_test; 
      print_string " ---- OK Test For the Lexer, Q 6.1 ----\n";
      TestFun.six_one str_pfx_test; 
      print_string " ---- WRONG Test For the Lexer, Q 6.1 ----\n";
      TestFun.six_one wrong_str_pfx_test; 
      print_string " ---- OK Test For the Parser, Q 6.2 ----\n";
      TestFun.six_two file_pfx_test;
      print_string " ---- OK Test For the Parser, Q 7 ----\n";
      TestFun.seven file_pfx_test;
      print_string " ---- OK Test For the Parser, Q 8 ----\n";
      TestFun.eight file_pfx_test []; (* file args *)
      print_string " ---- OK Test For the Parser with Args, Q 8 ----\n";
      TestFun.eight file_pfx_test [Int 2,Int 3]; (* file args *)
      print_string " ---- OK Test For the Parser, Q 9 ----\n";
      TestFun.eight file_fun_9_pfx []; 
      print_string " ---- OK Test For the Parser, Q 10.1 (\\x.x+1)(2)  ----\n";
      TestFun.eight file_fun_lamda_pfx []; 
      print_string " ---- OK Easy Test For generateV2, Q 10.3 (\\x.x+1)(2)  ----\n";
      TestFun.ten file_fun_lambda_simp_expr []; 
      print_string " ---- OK Complicated Test For generateV2, Q 10.3 ((\\x.7+x)(6))(\\y.y+8)  ----\n";
      TestFun.ten file_fun_lambda_comp_expr []; 
      
  with
    | _ -> print_string "Error on tests"
  

let () = main ()