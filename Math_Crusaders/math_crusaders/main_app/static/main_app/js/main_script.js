function Press() {
    document.querySelectorAll(".header_signs").forEach(element => {
        element.removeEventListener("mousedown", handleMouseDown);
        element.removeEventListener("mouseup", handleMouseUp);
    });
};

function handleMouseDown(event) {
    event.target.style.transform = "translateY(3px)";
};

function handleMouseUp(event) {
    setTimeout(() => {
        event.target.style.transform = "";
    }, 1);
};

function toggleTable(tableId) {
    const table = document.getElementById(tableId);
    if (table.classList.contains('active')) {
        table.classList.remove('active');
    } else {
        document.querySelectorAll('.page_lists').forEach(el => el.classList.remove('active'));
        table.classList.add('active');
    }
}

document.addEventListener('click', (event) => {
    if (!event.target.closest('.header_buttons')) {
        document.querySelectorAll('.page_lists').forEach(el => el.classList.remove('active'));
    }
});

setTimeout(() => {
    document.getElementById('loader').style.display = 'none';
    document.body.style.visibility = 'visible';
    document.body.style.overflow = 'auto';
}, 1500);