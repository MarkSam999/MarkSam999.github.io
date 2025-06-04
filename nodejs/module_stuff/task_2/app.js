const greet = require("./hero.greet()");
const goodbye  =require("./hero")

for(let i = 5; i > -1; i--){
    if(i == 0){
        greet();
    }else{
        console.log(i);
    }
};