let levelReached = 0;
let image = document.getElementById('girl')
let images = ["static/clicker/0points.png", "static/clicker/250kpoints.png", "static/clicker/500kpoints.png", "static/clicker/1kkpoints.png"]
image.src = images[0]


function onload_image(){
    fetch('/onload_image', {
        method: 'GET'
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {
        let userSavedScore = data.user.score
        change_image(userSavedScore)
    }).catch(error => console.log(error))
}


function call_click() {
    fetch('/call_click', {
        method: 'GET'
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {
        let score = data.user.score
        change_image(score)
        document.getElementById('score').innerText = data.user.score
    }).catch(error => console.log(error))
}


function change_image(score) {
    if((score < 10) && levelReached < 1){
        image.src = images[0]
    }
    else if(score < 20 && levelReached < 2){
        image.src = images[1]
        levelReached = 1
    }
    else if(score < 30 && levelReached < 3){
        image.src = images[2]
        levelReached = 2
    }
    else if(score >= 30){
        image.src = images[3]
        levelReached = 3
    }
}