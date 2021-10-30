package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

type order struct {
	OrderName       string    `json:"oderName"`
	Company         string    `json:"company"`
	CustomerName    string    `json:"customerName"`
	OrderDate       time.Time `json:"orderDate"`
	DeliveredAmount float32   `json:"deliveredAmount"`
	TotalAmount     float32   `json:"totalAmount"`
}

type orders []order

var localOrders = orders{
	{
		OrderName:       "#0003k",
		Company:         "happy PLT",
		CustomerName:    "Peter Sun",
		OrderDate:       parseDate("2021-11-12T11:45:26.371Z"),
		DeliveredAmount: 33.2,
		TotalAmount:     55.7,
	},

	{
		OrderName:       "#0003f",
		Company:         "piggy PLT",
		CustomerName:    "Luise Kim",
		OrderDate:       parseDate("2020-10-12T11:45:26.371Z"),
		DeliveredAmount: 22.5,
		TotalAmount:     55.7,
	},
}

func getAllOrders(w http.ResponseWriter, r *http.Request) {
	fmt.Println(localOrders)
	json.NewEncoder(w).Encode(localOrders)
}

func parseDate(s string) time.Time {
	layout := "2006-01-02T15:04:05.000Z"
	t, err := time.Parse(layout, s)
	if err != nil {
		fmt.Println(err)
		return time.Now()
	}
	fmt.Println(t)
	return t
}
