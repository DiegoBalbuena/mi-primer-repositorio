const redSlider = document.getElementById('red');
const greenSlider = document.getElementById('green');
const blueSlider = document.getElementById('blue');
const body = document.body;

function updateColor() {
    const red = redSlider.value;
    const green = greenSlider.value;
    const blue = blueSlider.value;
    body.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
}

// Llamamos a la función al cargar la página y cada vez que se cambia un deslizador
updateColor();
redSlider.addEventListener('input', updateColor);
greenSlider.addEventListener('input', updateColor);
blueSlider.addEventListener('input', updateColor);