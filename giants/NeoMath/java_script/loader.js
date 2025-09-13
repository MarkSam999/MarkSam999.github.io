$("header").style.display = "none";

setTimeout(() => {
    document.getElementById('loader').style.display = 'none';
    document.body.style.visibility = 'visible';
    $("header").style.display = "";
    document.body.style.overflow = 'auto';
}, 3000);

