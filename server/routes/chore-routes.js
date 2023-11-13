const express = require('express')
const choreRouter = express.Router()
const ChoreModel = require('../models/chore-model')

choreRouter.use(express.json())

// GET all Chores
choreRouter.get('/', async (req, res, next) => {
    try{
        const allChores = await ChoreModel.findAll();
        res.json(allChores);
    } catch(err){
        next(err)
    }
}) 

choreRouter.get('/:id', async (res, req, next) => {
    try{
        const found = await ChoreModel.findByPk(req.params.id);
        res.json(found);
    } catch(err){
        next(err);
    }
})

choreRouter.post('/chores', async(req, res, next) => {
    try{
        const created = await new ChoreModel({
            name:req.body.name, 
            weekday:req.body.weekday, 
            description:req.body.description
        });
        res.json(created)
    } catch (err){
        next(err);
    }
})

choreRouter.delete('/:id', async(req, res, next) => {
    try{
        const deleted = await ChoreModel.findByPk(req.params.id)
        await Chore.destroy(deleted)
        res.json(200)
    } catch (err){
        next(err)
    }
})


module.exports = peopleRouter;