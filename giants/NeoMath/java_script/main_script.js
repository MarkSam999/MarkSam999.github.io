setTimeout(() => {
    document.getElementById('loader').style.display = 'none';
    document.body.style.visibility = 'visible';
    document.body.style.overflow = 'auto';
}, 6000);

$("#aboutTable").hide(0);
$("#aboutBtn").click(function(){
    $("#aboutTable").toggle(600);
});

