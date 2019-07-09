(* colors of cards *)
type color = Spades | Hearts | Diamonds | Clubs;;
type card = Ace of color | King of color| Queen of color | Jack of color | Base_card of color * int;;

let all_the_cards color = 
[Ace color;  
Base_card (color,2);
Base_card (color,3);
Base_card (color,4);
Base_card (color,5);
Base_card (color,6);
Base_card (color,7);
Base_card (color,8);
Base_card (color,9);
Base_card (color,10);
Jack color;
Queen color;
King color
];;

let color_string = function
| Spades -> "Spades"
| Hearts -> "Hearts"
| Diamonds -> "Diamonds"
| Clubs -> "Clubs";;

let string_of_cards = function 
| Ace color -> "Ace of " ^ color_string color
| Base_card (color, v) -> (color_string color) ^ " of " ^ (string_of_int v)
| Jack color -> "Jack of " ^ color_string color
| Queen color -> "Queen of " ^ color_string color
| King color -> "King of " ^ color_string color;;

