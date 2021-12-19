package order

type Order struct {
	Id      int `json:"id"`
	FoodId  int `json:"food_id"`
	DrinkId int `json:"drink_id"`
}
