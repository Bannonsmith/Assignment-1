let title = document.getElementById('title')
let priority = document.getElementById('priority')
let dateCreated = document.getElementById('dateCreated')
let dateCompleted = document.getElementById("dateCompleted")
let isCompleted = document.getElementById("isCompleted")
let button = document.getElementById("button")

button.addEventListener("click", function (){

  let userInput = {title: title.value, priority: priority.value,
    dateCreated: dateCreated.value, dateCompleted: dateCompleted.value,
  isCompleted: isCompleted.value}
  console.log(JSON.stringify(userInput))

  fetch("http://localhost:3000/task", {
    method: "POST",
    headers: {
      "Content-Type" : "application/json"
    },
    body: JSON.stringify(userInput)
  }).then(function(response) {
      return response.json()
    }).then(function(json){
        console.log(json.success)
  })

})
