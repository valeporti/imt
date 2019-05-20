{
  type token =
    | EOF | PLUS | MINUS | TIMES | DIV | MOD | LPAR | RPAR
    | INT of int | IDENT of string

  let mk_int nb =
    try INT (int_of_string nb)
    with Failure _ -> failwith (Printf.sprintf "Illegal integer '%s': " nb)
}

let newline = (['\n' '\r'] | "\r\n")
let blank = [' ' '\014' '\t' '\012']
let digit = ['0'-'9']
let letter = ['a'-'z' 'A'-'Z']

rule token = parse
  (* newlines *)
  | newline + { token lexbuf }
  (* blanks *)
  | blank + { token lexbuf }
  (* end of file *)
  | eof      { EOF }
  (* integers *)
  | digit+ as nb           { mk_int nb }
  (* commands *)
  | "+"      { PLUS }
  | "-"      { MINUS }
  | "/"      { DIV }
  | "*"      { TIMES }
  | "%"      { MOD }
  | "("      { LPAR }
  | ")"      { RPAR }
  (* identifiers *)
  | letter (letter | digit | '_')* as id { IDENT id }
  (* illegal characters *)
  | _ as c  { failwith (Printf.sprintf "Illegal character '%c': " c) }


