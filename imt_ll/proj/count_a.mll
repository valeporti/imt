rule count value = parse
  | [^'a']*  { count value lexbuf }
  | 'a'    { count (value + 1) lexbuf }
  | eof    { value }

{
  let count_a s = let buffer = Lexing.from_string s in count 0 buffer
}
