let score = 0;
let betterClickCost = 20;
let clicks = 0;
let levelReached = 0;
let image = document.getElementById('girl')
let images = ["static/clicker/0points.png", "static/clicker/250kpoints.png", "static/clicker/500kpoints.png", "static/clicker/1kkpoints.png"]
image.src = images[0]

function buyClick() {
    if (score >= betterClickCost){
        score -= betterClickCost;
        clicks += 1;
        betterClickCost = Math.round(betterClickCost * 1.20);
        document.getElementById("score").innerHTML = score;
        document.getElementById("betterClickCost").innerHTML = betterClickCost;
        document.getElementById("clicks").innerHTML = clicks;
    }
}

function addToScore(amount) {
    score += amount;
    document.getElementById("score").innerHTML = score;
}

setInterval(function () {
    score += clicks;
    document.getElementById("score").innerHTML = score;
}, 1000)

image.onclick = function (){
    if((score < 9) && levelReached < 1){
        image.src = images[0]
    }
    else if(score < 19 && levelReached < 2){
        image.src = images[1]
        levelReached = 1
    }
    else if(score < 29 && levelReached < 3){
        image.src = images[2]
        levelReached = 2
    }
    else if(score < 39 && levelReached < 4){
        image.src = images[3]
        levelReached = 3
    }
}