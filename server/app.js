const express = require('express')
const mongoose = require('mongoose')
const choreModel = require('./models/chore-model')
const choreRouter = require('./routes/chore-routes')

const app = express();
mongoose.connect("mongodb+srv://asgrim:ER4GONm6-w105dx!@grim0.mnpenyr.mongodb.net")
    .then(() => {
        console.log(`Connected to MongoDB`)
    })
    .catch(() => {
        console.log("Error connecting to MongoDB")
    })

app.use(express.json())
// choreRouter.use('/chores')