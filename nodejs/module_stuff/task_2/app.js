const {greet} = require("./hero");
const {goodbye}  =require("./hero")

for(let i = 5; i > -1; i--){
    if(i == 0){
        goodbye();
    }else{
        console.log(i);
    }
};