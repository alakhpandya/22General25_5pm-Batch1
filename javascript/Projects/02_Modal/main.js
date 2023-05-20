let modalBtn = document.querySelector('.modal-btn');
let modalContainer = document.querySelector('.modal-container');
let closeBtn = document.getElementById('close-btn');
let bgImg = document.querySelector('.bg-img');
let target;

modalBtn.addEventListener('click', () => {
    modalContainer.style.animationName = 'moveModal';
    modalContainer.style.display = 'block';
    bgImg.style.opacity = 0.5;
})

window.addEventListener('click', (e) => {
    target = e.target
    if (target == closeBtn || (target != modalContainer && target != modalBtn)){
        modalContainer.style.display = 'none';
        bgImg.style.opacity = 1;
    }
})