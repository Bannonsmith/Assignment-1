let express = require("express")
let app = express()
let mustacheExpress = require("mustache-express")


// tell express to use mustache templating engine
app.engine('mustache',mustacheExpress())
// the pages are located in views directory
app.set('views','./views')
// extension will be .mustache
app.set('view engine','mustache')


app.listen(3000, () => {
  console.log("Server is running.....")
})
