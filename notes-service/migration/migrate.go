package main

import (
	"notes/initializers"
	"notes/models"
)

func init() {
	initializers.LoadEnvVariables()
	initializers.ConnectToDB()
}

func main() {
	initializers.DB.AutoMigrate(models.Note{})
}
