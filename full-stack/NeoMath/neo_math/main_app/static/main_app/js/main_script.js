function handleMouseDown(event) {
    event.target.style.transform = "translateY(3px)";
};

function handleMouseUp(event) {
    setTimeout(() => {
        event.target.style.transform = "";
    }, 1);
};


$("#progress").animate({width: "100%"}, 2300);
setTimeout(() => {
    document.getElementById('loader').style.display = 'none';
    document.body.style.visibility = 'visible';
    document.body.style.overflow = 'auto';
}, 2500);

$("#aboutTable").hide(0);
$("#aboutBtn").click(function(){
    $("#aboutTable").toggle(600);
});

