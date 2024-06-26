if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

// Addition
function add() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('#add').onclick = add;
});

// Subtraction
function subtract() {
    let counter = localStorage.getItem('counter');
    counter = counter - 1;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('#subtract').onclick = subtract;
});