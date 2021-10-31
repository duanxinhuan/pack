package main

import (
	"fmt"
	"go-server/go-helper"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func homeLink(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome home!")
}

func main() {
	helper.PrintIt()
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/", homeLink)
	router.HandleFunc("/orders", getAllOrders)
	log.Fatal(http.ListenAndServe(":8080", router))

}
