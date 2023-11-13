const mongoose = require('mongoose');
const uniqueValidator = require('mongoose-unique-validator')

const choreSchema = mongoose.Schema({
    name: {type: String, required: true, unique: true},
    weekday: {type: String, required: true},
    description: {type: String}
})

choreSchema.plugin(uniqueValidator);

module.exports = mongoose.model("ChoreModel", choreSchema);