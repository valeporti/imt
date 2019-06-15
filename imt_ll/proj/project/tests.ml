

(* The main function *)
let main () = 
  print_string "Hello!\n\n";
  try
    let str_pfx_test = "0 Push 2 Push 3 Add" in
    let file_pfx_test = "./tests/tp" in
    let file_pfx_test_args = "./tests/tpargs" in
    let file_expr_test = "./tests/tt" in
    let file_fun_9_pfx = "./tests/tpfun" in
    let wrong_str_pfx_test = "nothing" in
    let file_fun_lamda_pfx = "./tests/tpten" in
    let file_fun_lambda_simp_expr = "./tests/ttfunsimp" in
    let file_fun_lambda_comp_expr = "./tests/ttfun" in
    let file_fun_lambda_comp_expr2 = "./tests/ttfuncomp2" in
      print_string " ---- OK Test For the ExprToPfx, Q 5 ( 3+2-(4/2) = 3 )----\n";
      TestFun.five file_expr_test; 
      print_string " ---- OK Test For the Lexer, Q 6.1 ('0 Push 2 Push 3 Add') ----\n";
      TestFun.six_one str_pfx_test; 
      print_string " ---- WRONG Test For the Lexer, Q 6.1 ('nothing') ----\n";
      TestFun.six_one wrong_str_pfx_test; 
      print_string " ---- OK Test For the Lexer, Q 6.2  Print all tokens: ( 0 Push 1 Push 1 Add Push 3 Add Push 2 Mul Push 2 Div = 5) ----\n";
      TestFun.six_two file_pfx_test;
      print_string " ---- OK Test For the Parser, Q 7 (Optimized Location errors) ----\n";
      TestFun.seven file_pfx_test;
      print_string " ---- OK Test For the Parser, Q 8 pfxPArser test ----\n";
      TestFun.eight file_pfx_test []; (* file args *)
      print_string " ---- OK Test For the Parser with Args, Q 8 (Args are 3, 7, 2) -> result = 5 ----\n";
      TestFun.eight file_pfx_test_args [Int 3; Int 7]; (* file args *)
      print_string " ---- OK Test For the Parser, Q 9 (Testing the adaptation of pfxParser and PfxLexer) ----\n";
      TestFun.eight file_fun_9_pfx []; 
      print_string " ---- OK Test For the Parser, Q 10.1 (\\x.x+1)(2) = 3 ----\n";
      TestFun.eight file_fun_lamda_pfx []; 
      print_string " ---- OK Easy Test For generateV2, Q 10.3 (\\x.x+1)(2) = 3 ----\n";
      TestFun.ten file_fun_lambda_simp_expr []; 
      print_string " ---- OK Complicated Test 1 For generateV2, Q 10.3 (fun y -> (fun x->(20-x))(6) + y)(7) = 21  ----\n";
      TestFun.ten file_fun_lambda_comp_expr []; 
      print_string " ---- OK Complicated Test 2 For generateV2, Q 10.3 (fun y -> (fun x->(4*x))(6) / y)(2) = 12  ----\n";
      TestFun.ten file_fun_lambda_comp_expr2 []; 
  with
    | _ -> print_string "Error on tests"
  

let () = main ()