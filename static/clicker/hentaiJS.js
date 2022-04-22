let score = 0;
let betterClickCost = 20;
let clicks = 0;

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