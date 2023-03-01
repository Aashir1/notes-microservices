package controllers

import (
	"fmt"
	"notes/initializers"
	"notes/models"

	"github.com/gin-gonic/gin"
)

func NotesCreate(c *gin.Context) {

	//Get data

	var body struct {
		Title string
		Body  string
	}

	c.Bind(&body)

	//Create notes
	note := models.Note{Title: body.Title, Body: body.Body}

	result := initializers.DB.Create(&note) // pass pointer of data to Create

	fmt.Println("result: ", result)

	if result.Error != nil {
		c.Status(400)
		return // returns error

	}

	//Return

	c.JSON(200, gin.H{
		"note": note,
	})
}

func GetNotes(c *gin.Context) {
	var notes []models.Note

	initializers.DB.Find(&notes)

	c.JSON(200, gin.H{
		"notes": notes,
	})
}

func GetNotesById(c *gin.Context) {

	var id = c.Param("id")

	var note models.Note

	initializers.DB.First(&note, id)

	c.JSON(200, gin.H{
		"note": note,
	})
}

func UpdateNotes(c *gin.Context) {
	//param
	var id = c.Param("id")

	//get data from req body
	var body struct {
		Title string
		Body  string
	}

	c.Bind(&body)

	//find note from db
	var note models.Note
	initializers.DB.First(&note, id)

	//update
	initializers.DB.Model(&note).Updates(models.Note{Title: body.Title, Body: body.Body})

	c.JSON(200, gin.H{
		"note": note,
	})
}

func DeleteNotes(c *gin.Context) {

	var id = c.Param("id")

	var note models.Note

	initializers.DB.Delete(&note, id)

	c.Status(200)
}
