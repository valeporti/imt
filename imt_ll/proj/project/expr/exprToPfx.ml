open ExprAst
open PfxAst

(*
let rec generate = function
  | Const c -> failwith "To implement"
  | Binop(op,e1,e2) -> failwith "To implement"
  | Uminus e -> failwith "To implement"
  | Var v -> failwith "Not yet supported"
*)

(* 5.2 *)
(*
let rec generate = function
  | Const c -> [Push c]
  | Binop(Badd,e1,e2) -> [Push e2; Push e1; Add] 
  | Binop(Bsub,e1,e2) -> [Push e2; Push e1; Sub]
  | Binop(Bmul,e1,e2) -> [Push e2; Push e1; Mul]
  | Binop(Bdiv,e1,e2) -> [Push e2; Push e1; Div]
  | Binop(Bmod,e1,e2) -> [Push e2; Push e1; Mod]
  | Uminus e -> [-e]
  | Var v -> failwith "Not yet supported"
*)
let soi i = string_of_int i

(*
let rec findSize t s = function (* temp size *)
| [] -> print_string ("end("^(soi s)^")\n"); s
| Exec::tl -> print_string ("Exec("^(soi t)^")\n"); t
| (Add|Mul|Div|Sub|Rem|Swap)::tl -> print_string ("***("^(soi t)^","^(soi s)^")\n"); findSize (t-1) (s-1) tl (* Decrease one once applied *) 
| Push(c)::tl -> print_string ("Push("^(soi t)^","^(soi s)^")\n"); findSize (t+1) (s+1) tl (* Increase one *)
| Pop::tl -> print_string ("Pop("^(soi t)^","^(soi s)^")\n"); findSize (t-1) (s-1) tl (* Decrease one *)
| Get::tl -> print_string ("Get("^(soi t)^","^(soi s)^")\n"); findSize t s tl (* do nothing since it pops and add to stak *)
| Q(ins)::tl -> print_string ("Q("^(soi t)^","^(soi s)^")\n"); findSize (findSize 0 s ins) s tl (* start counting "internally" temp *) 
*)

let rec getFV p n l = match l with
| [] -> p
| (Fv name, Pos pos)::tl ->
  begin
    if name = n then
      begin
        if pos = p then pos
        else if pos < p then pos (* Handle scope *)
        else if pos > p then failwith "error in searching pos"
        else getFV p n tl
      end
    else getFV p n tl
  end

let rec generateV3 t p fvl = (* t-for inner positions, p- for general position, fvl - free variables list *)  
  function
  | Const c -> print_string ("Push "^(soi c)^"("^(soi t)^"+1,"^(soi p)^"+1)\n"); [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
      (* []@[]@[] -> pos+1 pos+1 and pos-1 *)
			| Badd -> print_string ("Add ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3 (t+1) (p+1) fvl e1)@(generateV3 (t+1) (p+1) fvl e2)@[Add]
			| Bsub -> print_string ("Sub ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3 (t+1) (p+1) fvl e1)@(generateV3 (t+1) (p+1) fvl e2)@[Sub]
			| Bmul -> print_string ("Mul ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3 (t+1) (p+1) fvl e1)@(generateV3 (t+1) (p+1) fvl e2)@[Mul]
			| Bdiv -> print_string ("Div ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3 (t+1) (p+1) fvl e1)@(generateV3 (t+1) (p+1) fvl e2)@[Div]
			| Bmod -> print_string ("Mod ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3 (t+1) (p+1) fvl e1)@(generateV3 (t+1) (p+1) fvl e2)@[Rem]
		end		
  | Uminus e -> (generateV3 (t+1) (p+1) fvl e)@(generateV3 (t+1) (p+1) fvl (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) -> 
    print_string ("App ("^(soi t)^","^(soi p)^")\n"); 
    (generateV3 t p fvl e2)@(generateV3 t p fvl e1)
  (* begin
      match e1, e2 with 
      (* Handle simple App(\x.e , expression) *)
      | Fun(v, e), _ -> 
        print_string ("Fun ("^(soi t)^"+1,"^(soi p)^"+1)\n"); 
        (generateV3 t p fvl e2)@(generateV3 t p fvl e)
      (* Means, that we don't have a direct function definition in the expression but sub application *)
      (*| e, Const c -> print_string "CO1!\n"; [Push c]@[Q (generateV3 0 p fvl e)]@[Exec]@[Swap]@[Pop]*)
      | _ , Const c -> print_string ("ConstApp "^(soi c)^"\n"); [Push c]@[Q (generateV3 0 p fvl e1)]@[Exec]@[Swap]@[Pop]
      | _, _ -> 
        print_string ("Other ("^(soi t)^"+1,"^(soi p)^"+1)\n"); 
        (generateV3 (t+1) (p+1) fvl e1)@(generateV3 (t+1) (p+1) fvl e2)
    end *)
  | Fun(v, e) -> 
    print_string ("Fun ("^(soi 0)^","^(soi p)^")\n"); 
    [Q (generateV3 0 p ([((Fv v), (Pos (p-t)))]@fvl) e)]@[Exec]@[Swap]@[Pop]
  | Var v -> 
    print_string ("Var "^v^" Push("^(soi p)^"-"^(soi t)^")\n"); 
    print_string (soi (getFV p v fvl)); 
    print_string "\n"; 
    print_string (string_of_fvl fvl);
    [Push (getFV p v fvl)]@[Get]


let rec generateV2 t p = (* t-for inner positions, p- for general position *)  
  function
  | Const c -> [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
      (* []@[]@[] -> pos+1 pos+1 and pos-1 *)
			| Badd -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Add]
			| Bsub -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Sub]
			| Bmul -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Mul]
			| Bdiv -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Div]
			| Bmod -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Rem]
		end		
  | Uminus e -> (generateV2 (t+1) (p+1) e)@(generateV2 (t+1) (p+1) (Const 0))@[Sub]
  (* Function Support *)
  (* need it to be : Push c [ Push (position c) Get Push 2 Add ] Exec *)
  (* left exp is the function, right exp the argument *)
  | App(e1, e2) -> (generateV2 t p e2)@(generateV2 t p e1)
  | Fun(v, e) -> [Q (generateV2 0 p e)]@[Exec]@[Swap]@[Pop]
  | Var v -> [Push (p-t)]@[Get]

let rec generate = 
  (*let sumOne x = x + 1 in
  let pos = -1 in*)
  function
  | Const c -> [Push c]
  | Binop(op,e1,e2) -> 
		begin
			match op with
			| Badd -> (generate e1)@(generate e2)@[Add]
			| Bsub -> (generate e1)@(generate e2)@[Sub]
			| Bmul -> (generate e1)@(generate e2)@[Mul]
			| Bdiv -> (generate e1)@(generate e2)@[Div]
			| Bmod -> (generate e1)@(generate e2)@[Rem]
		end		
  | Uminus e -> (generate e)@(generate (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) -> failwith "First Generate Version does not support App"
  | Fun(v, e) -> failwith "First Generate Version does not support Fun"
  | Var v -> failwith "First Generate Version does not support Var"


(* PRINT ALL VAUES generateV2 Version  *)
(*
let rec generateV2 t p = (* t-for inner positions, p- for general position *)  
  function
  | Const c -> print_string ("Push "^(soi c)^"("^(soi t)^"+1,"^(soi p)^"+1)\n"); [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
      (* []@[]@[] -> pos+1 pos+1 and pos-1 *)
			| Badd -> print_string ("Add ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Add]
			| Bsub -> print_string ("Sub ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Sub]
			| Bmul -> print_string ("Mul ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Mul]
			| Bdiv -> print_string ("Div ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Div]
			| Bmod -> print_string ("Mod ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Rem]
		end		
  | Uminus e -> (generateV2 (t+1) (p+1) e)@(generateV2 (t+1) (p+1) (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) -> (* need it to be : Push c [ Push (position c) Get Push 2 Add ] Exec *)
    begin
      match e1, e2 with 
      (* Handle simple App(\x.e , expression) *)
      | Fun(v, e), _ -> print_string ("Fun ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 t p e2)@[Q (generateV2 0 p e)]@[Exec]@[Swap]@[Pop]
      | _, _ -> failwith "Not Supported App Case"
      (*
      | ea, eb -> 
        print_string "  ||  "; 
        print_string (string_of_expr ea); 
        print_string "  ||  "; 
        print_string (string_of_expr eb); 
        print_string "\n"; 
        [Push 0]; *)
    end
  | Fun(v, e) -> print_string ("FunFun ("^(soi 0)^","^(soi p)^")\n"); failwith "Not Supported Function Case"; (generateV2 0 p e)
  | Var v -> print_string ("Var "^v^" Push("^(soi p)^"-"^(soi t)^")\n"); [Push (p-t)]@[Get]
*)
