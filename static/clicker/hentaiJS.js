let score = 0;
let betterClickCost = 20;
let clicks = 0;
let levelReached = 0;
let image = document.getElementById('girl')
let images = ["static/clicker/0points.png", "static/clicker/250kpoints.png", "static/clicker/500kpoints.png", "static/clicker/1kkpoints.png"]
image.src = images[0]

function call_click() {
    fetch('/call_click', {
        method: 'GET'
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {
        document.getElementById('score').innerText = data.user.score
    }).catch(error => console.log(error))
}

