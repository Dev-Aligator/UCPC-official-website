document.addEventListener("DOMContentLoaded", function () {

    let deadline = "May 26, 2022 00:00:00"
    let countDown = new Date(deadline).getTime()
    let x = setInterval(function () {
        let now = new Date().getTime()
        let distance = countDown - now
        document.querySelector("#days").innerHTML = Math.floor(distance / (1000 * 60 * 60 * 24)),
        document.querySelector("#hours").innerHTML = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        document.querySelector("#minutes").innerHTML = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
        document.querySelector("#seconds").innerHTML = Math.floor((distance % (1000 * 60)) / 1000);
        if (distance < 0) {
            document.querySelector("#days").innerHTML = 00,
            document.querySelector("#hours").innerHTML = 00,
            document.querySelector("#minutes").innerHTML = 00,
            document.querySelector("#seconds").innerHTML = 00;
        }
    }, 0)
})