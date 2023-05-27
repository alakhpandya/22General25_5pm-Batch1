// setInterval:
/*
const hello = () => {
    console.log("Hello Devanshu!");
    console.log("How are you?");
}
let timerControl = setInterval(hello, 2000);
let btn = document.querySelector('.play-pause-btn');

btn.addEventListener('click', () => {
    clearInterval(timerControl);
})
*/

let playPauseBtn = document.querySelector('.play-pause-btn');
let ms=0, s=0, min=0, h=0;
var timerInterval;
let timerText = document.querySelector('.timer-text');
let resetBtn = document.querySelector('.reset-btn')

const stopwatch = () => {
    ms++;
    if (ms == 100){
        ms = 0;
        s++;
        if (s == 60){
            s = 0;
            min++
            if (min == 60){
                min = 0;
                h++;
            }
        }
    }
    timerText.innerText = `${h.toString().padStart(2, '0')} : ${min.toString().padStart(2, '0')} : ${s.toString().padStart(2, '0')} : ${ms.toString().padStart(3, '0')}`;
}

playPauseBtn.addEventListener('click', () => {
    if (playPauseBtn.classList.contains('fa-play')){
        timerInterval = setInterval(stopwatch, 10);
        playPauseBtn.classList.remove('fa-play');
        playPauseBtn.classList.add('fa-pause');
    }
    else{
        clearInterval(timerInterval);
        playPauseBtn.classList.remove('fa-pause');
        playPauseBtn.classList.add('fa-play');
    }
})

resetBtn.addEventListener('click', () => {
    h = 0, min = 0, s = 0, ms = 0;
    `${h.toString().padStart(2, '0')} : ${min.toString().padStart(2, '0')} : ${s.toString().padStart(2, '0')} : ${ms.toString().padStart(3, '0')}`;
})