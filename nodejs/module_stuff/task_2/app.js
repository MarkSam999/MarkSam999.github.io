const superHero = "Iron Man"

function greet(){
    console.log("Hello,", superHero)
};

for(let i = 5; i > 0; i--){
    if(i == 1){
        greet();
    }else{
        console.log(i);
    }
};

