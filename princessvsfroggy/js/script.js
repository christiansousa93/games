const princess = document.querySelector('.princess');
const froggy = document.querySelector('.froggy');


const jump = () => {
    princess.classList.add('jump');
    setTimeout(() =>{
        princess.classList.remove('jump');
    }, 500);
}

const loop = setInterval(() => {

    const froggyPosition = froggy.offsetLeft;
    const princessPosition = +window.getComputedStyle(princess).bottom.replace('px', '');


    if (froggyPosition >= 1000 && froggyPosition > 0 && princessPosition < 60)  {

        froggy.style.animation = 'none';
        froggy.style.left = `${froggyPosition}px`;

        princess.style.animation = 'none';
        princess.style.bottom = `${princessPosition}px`;

        princess.src = './images/princessdead.gif'

        clearInterval(loop);
    }
}, 10);

document.addEventListener('keydown', jump);
