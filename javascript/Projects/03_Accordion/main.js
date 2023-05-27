
let target;

window.addEventListener('click', (e) => {
    target = e.target;
    // console.log(target);
    if (target.classList.contains('btn')){
        if (target.parentElement.parentElement.classList.contains('show')){
            target.parentElement.parentElement.classList.remove('show');
            target.innerText = '+'
        }
        else{
            target.parentElement.parentElement.classList.add('show');
            target.innerText = '-'
        }
    }
})


/*
let btn = document.getElementsByClassName('btn');
let faq = document.getElementsByClassName('faq');

for(let i = 0; i < btn.length; i++){
    btn[i].addEventListener('click', () => {
        if (faq[i].classList.contains('show')){
            faq[i].classList.remove('show');
            btn[i].innerText = '+'
        }
        else{
            faq[i].classList.add('show');
            btn[i].innerText = '-'
        }
    })
}
*/