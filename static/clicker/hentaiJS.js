// Тут мы даем хентай-девочке инфу о том, в что ей нужно одеться
let image = document.getElementById('girl')
let images = ["static/clicker/girls/0points.png", "static/clicker/girls/250kpoints.png", "static/clicker/girls/500kpoints.png", "static/clicker/girls/1kkpoints.png"]
image.src = images[0]


// Функция, которая предзагружает картинку (А то наша хентай-девочка
// будет появляться в одежде и потребует удар, чтобы обновиться)
function onload_image(){
    fetch('/onload_image', {
        method: 'GET'
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {
        // Проверяем, нужно ли обновить одежду хентай-девочки
        let userSavedLevel = data.user.level
        change_image(userSavedLevel)
    }).catch(error => console.log(error))
}


// Функция, которая кликает
function call_click() {
    fetch('/call_click', {
        method: 'GET'
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {
        // Проверям, нужно ли обновить одежду хентай-девочки
        let level = data.user.level
        change_image(level)

        // Тут мы обновляем значение Счёта(Hits) вместе с кликом
        document.getElementById('score').innerText = data.user.score
    }).catch(error => console.log(error))
}

// Функция, которая отвечает за покупку тентаклины
function update_power(i){
    fetch(`/update_power${i}`, {
        method: 'GET'
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {

        // Тут мы обновляем количество тентаклей вместе с покупкой
        document.getElementById('tentacle1_count').innerText = data.user.tentacle1_count
        document.getElementById('tentacle2_count').innerText = data.user.tentacle2_count
        document.getElementById('tentacle3_count').innerText = data.user.tentacle3_count
        document.getElementById('tentacle4_count').innerText = data.user.tentacle4_count
        document.getElementById('tentacle5_count').innerText = data.user.tentacle5_count

        // Тут мы обновляем стоимость тентакля вместе с покупкой
        document.getElementById('tentacle1_cost').innerText = data.user.tentacle1_cost
        document.getElementById('tentacle2_cost').innerText = data.user.tentacle2_cost
        document.getElementById('tentacle3_cost').innerText = data.user.tentacle3_cost
        document.getElementById('tentacle4_cost').innerText = data.user.tentacle4_cost
        document.getElementById('tentacle5_cost').innerText = data.user.tentacle5_cost

        // Тут мы обновляем значения Hits Per Click и Счёта(Hits) вместе с покупкой
        document.getElementById('HPC').innerText = data.user.click_power
        document.getElementById('score').innerText = data.user.score
    }).catch(error => console.log(error))
}

// Функция, которая присваивает уровню пользователя соответствующую картинку
function change_image(level) {
    if(level < 1){
        image.src = images[0]
    }
    else if(level < 2){
        image.src = images[1]
    }
    else if(level < 3){
        image.src = images[2]
    }
    else if(level === 3){
        image.src = images[3]
    }
}