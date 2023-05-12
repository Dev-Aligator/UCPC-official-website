const targetDate = new Date("May 25, 2023 00:00:00").getTime();
const publicDate = new Date("April 29, 2023 00:00:00").getTime();

const timeDiff = targetDate - publicDate;
const daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));

const countdownInterval =  setInterval(function() {
    const now = new Date().getTime();
    const remainingTime = targetDate - now;
    if (remainingTime < 0) {
        clearInterval(countdownInterval);
        return;
    }
    let days = document.getElementById("days");
    let hours = document.getElementById("hours");
    let minutes = document.getElementById("minutes");
    let seconds = document.getElementById("seconds");

    let dd = document.getElementById("dd");
    let hh = document.getElementById("hh");
    let mm = document.getElementById("mm");
    let ss = document.getElementById("ss");

    let day_dot = document.querySelector('.day_dot');
    let hr_dot = document.querySelector('.hr_dot');
    let min_dot = document.querySelector('.min_dot');
    let sec_dot = document.querySelector('.sec_dot');


    let d = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
    let h = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let m = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
    let s = Math.floor((remainingTime % (1000 * 60)) / 1000);


    // add zero before single digit number
    d = ( d < 10 ) ? "0" + d : d;
    h = ( h < 10 ) ? "0" + h : h;
    m = ( m < 10 ) ? "0" + m : m;
    s = ( s < 10 ) ? "0" + s : s;

    
    days.innerHTML = d + "<br><span>Days</span>";
    hours.innerHTML = h + "<br><span>Hours</span>";
    minutes.innerHTML = m + "<br><span>Minutes</span>";
    seconds.innerHTML = s + "<br><span>Seconds</span>";

    dd.style.strokeDashoffset = -(440 * d) / 26;

    hh.style.strokeDashoffset = -(440 * h) / 24;

    mm.style.strokeDashoffset = -(440 * m) / 60;

    ss.style.strokeDashoffset = -(440 * s) / 60;


    day_dot.style.transform = `rotate(${d*(360/daysDiff)}deg)`;

    hr_dot.style.transform = `rotate(${h*15}deg)`;

    min_dot.style.transform = `rotate(${m*6}deg)`;

    sec_dot.style.transform = `rotate(${s*6}deg)`;
}, 1000)