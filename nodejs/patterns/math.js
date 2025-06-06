module.exports = (a, b) => {
    let raw = 
    let result = Math.round(a / b * 100);
    if(result >= 1){
        console.log(result + "%");
    } else {
        console.log("<1%")
    }
}
