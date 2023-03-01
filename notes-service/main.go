package main

import (
	"notes/controllers"
	"notes/initializers"

	"github.com/gin-gonic/gin"
)

func init() {
	initializers.LoadEnvVariables()
	initializers.ConnectToDB()

}

func main() {

	r := gin.Default()
	r.POST("/notes", controllers.NotesCreate)
	r.PUT("/notes/:id", controllers.UpdateNotes)
	r.GET("/notes", controllers.GetNotes)
	r.GET("/notes/:id", controllers.GetNotesById)
	r.DELETE("/notes/:id", controllers.DeleteNotes)
	r.Run() // listen and serve on 0.0.0.0:8080
}
