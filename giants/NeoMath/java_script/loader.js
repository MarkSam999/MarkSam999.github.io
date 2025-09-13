document.body.header.style.display = "none";

setTimeout(() => {
    document.getElementById('loader').style.display = 'none';
    document.body.style.visibility = 'visible';
    document.body.header.display = "inline";
    document.body.style.overflow = 'auto';
}, 3000);

