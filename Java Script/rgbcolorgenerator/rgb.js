const redSlider = document.querySelector('#red');
const greenSlider = document.querySelector('#green');
const blueSlider = document.querySelector('#blue');

const redText = document.querySelector('#textR');
const greenText = document.querySelector('#textG');
const blueText = document.querySelector('#textB');


const color = document.querySelector('.result');
const text = document.querySelector('.rgb');

redSlider.addEventListener('input',updatecolor);
greenSlider.addEventListener('input',updatecolor);
blueSlider.addEventListener('input',updatecolor);


function updatecolor(){
    const red = redSlider.value;
    const green = greenSlider.value;
    const blue = blueSlider.value;

    const finalColor = `rgb(${red},${green},${blue})`;

    color.style.backgroundColor = finalColor;
    
    redText.textContent = red;
    greenText.textContent = green;
    blueText.textContent = blue;

    
    text.textContent = finalColor;

}
