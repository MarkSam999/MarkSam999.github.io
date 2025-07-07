let a1 = 0;
let points = 0;
let actions = ['+', "-", '*', '/']

let q1n1 = Math.round(Math.random() * 10);
let q1n2 = Math.round(Math.random() * 10);
let action = actions[Math.round(Math.random() * 3)];
if(action == '+'){
    q1ca = 
}
$("#q1").text(action);

function oneA(){
    a1 = 63;
}

function oneB(){
    a1= 50;
}

function oneC(){
    a1 = 70;
}

function oneD(){
    a1 = 66;
}

function twoA(){
    a2 = 12;
}

function twoB(){
    a2= 15;
}

function twoC(){
    a2 = 14;
}

function twoD(){
    a2 = 17;
}

function threeA(){
    a3 = 15;
}

function threeB(){
    a3= 16;
}

function threeC(){
    a3 = 11;
}

function threeD(){
    a3 = 12;
}

function fourA(){
    a4 = 9;
}

function fourB(){
    a4= 8;
}

function fourC(){
    a4 = 12;
}

function fourD(){
    a4 = 15;
}

function fiveA(){
    a5 = 32;
}

function fiveB(){
    a5= 31;
}

function fiveC(){
    a5 = 30;
}

function fiveD(){
    a5 = 28;
}

function check(){
    if (a1 === 63){
        points += 1;
    }
    if (a2 === 14){
        points += 1;
    }
    if (a3 === 12){
        points += 1;
    }
    if (a4 === 8){
        points += 1;
    }
    if (a5 === 30){
        points += 1;
    }
    alert("You got " + points + "/5!")
}
