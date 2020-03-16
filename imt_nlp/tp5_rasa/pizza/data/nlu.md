## intent:greet
- hey, what can I do for you?
- hello, how can I help?
- hi, can I take your order?

## intent:goodbye
- bye
- goodbye
- see you later
- see you around

## intent:order_pizza
- I would like to order pizza
- I desire to order

## intent: inform/order_pizza
- I would like [two](pizza_quantity) pizzas
- I would like [one](pizza_quantity) pizza
- I would like [a](pizza_quantity:one) pizza

## intent: inform/determine_size
- I would like [a](pizza_quantity:one) [medium](pizza_size) pizza
- I would like [one](pizza_quantity) [big](pizza_size) pizza
- I would like [two](pizza_quantity) [small](pizza_size) pizzas
- I would like [three](pizza_quantity) [big](pizza_size) pizzas
- [two](pizza_quantity) [medium](pizza_size) pizzas
- [one](pizza_quantity) [small](pizza_size) pizza
- [small](pizza_size)
- [medium](pizza_size)
- [big](pizza_size)

## intent: inform/determine_type
- I would like [a](pizza_quantity:one) [mexicana](pizza_type)
- I would like [one](pizza_quantity) [4 formaggi](pizza_type)
- [two](pizza_quantity) [mexicanas](pizza_type)
- [three](pizza_quantity) [mexicanas](pizza_type)