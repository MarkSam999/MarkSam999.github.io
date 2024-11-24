function Press(){
    document.querySelectorAll(".header_signs").forEach(element => {
        element.addEventListener("mousedown", 
            () => {
            element.style.transform = 
            "translateY(3px)";
        }); // Move down
        element.addEventListener("mouseup", 
            () => {
            setTimeout(() => {
                element.style.transform = 
                "";
            }, 1);
        }); // return back
    });
    
}

    