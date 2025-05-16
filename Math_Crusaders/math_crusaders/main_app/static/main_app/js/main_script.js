alert($("body").id);

function handleMouseDown(event) {
    event.target.style.transform = "translateY(3px)";
};

function handleMouseUp(event) {
    setTimeout(() => {
        event.target.style.transform = "";
    }, 1);
};


$("#progress").animate({width: "100%"}, 2000);
setTimeout(() => {
    document.getElementById('loader').style.display = 'none';
    document.body.style.visibility = 'visible';
    document.body.style.overflow = 'auto';
}, 2200);

$("#aboutTable").hide(0);
$("#aboutBtn").click(function(){
    $("#aboutTable").toggle(600);
});

$("#profileTable").hide(0);
$("#profileBtn").click(function(){
    $("#profileTable").toggle(600);
});

