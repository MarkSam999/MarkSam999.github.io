$("header").visibility = none;

setTimeout(() => {
    document.getElementById('loader').style.display = 'none';
    document.body.style.visibility = 'visible';
    document.body.style.overflow = 'auto';
}, 3000);

