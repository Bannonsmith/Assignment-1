let express = require("express")
let cors = require("cors")
let application = express()
let bodyParser = require("body-parser")
application.use(cors())
application.use(bodyParser.json())


application.post("/task", function(req,res) {

  let title = req.body.title
  let priority = req.body.priority
  let dateCreated = req.body.dateCreated
  let dateCompleted = req.body.dateCompleted
  let isCompleted = req.body.isCompleted

  //res.status(200).send()

  res.json({success: true})

 // res.send("cat")
})

application.listen(3000,function () {
  console.log("Server is running.....")
})
