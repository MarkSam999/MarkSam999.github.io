module.exports = (a, b) => {
    let raw = a / b * 100;
    let result = Math.round(a / b * 100);
    if(result >= 1){
        console.log(result + "%");
    } else {
        console.log("<1%")
    }
}
