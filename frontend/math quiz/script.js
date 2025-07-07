let answer1 = 0;
let points = 0;

q1n1 = Math.round(Math.random() * 10);
$("#q1").te

function oneA(){
    answer1 = 63;
}

function oneB(){
    answer1= 50;
}

function oneC(){
    answer1 = 70;
}

function oneD(){
    answer1 = 66;
}

function twoA(){
    answer2 = 12;
}

function twoB(){
    answer2= 15;
}

function twoC(){
    answer2 = 14;
}

function twoD(){
    answer2 = 17;
}

function threeA(){
    answer3 = 15;
}

function threeB(){
    answer3= 16;
}

function threeC(){
    answer3 = 11;
}

function threeD(){
    answer3 = 12;
}

function fourA(){
    answer4 = 9;
}

function fourB(){
    answer4= 8;
}

function fourC(){
    answer4 = 12;
}

function fourD(){
    answer4 = 15;
}

function fiveA(){
    answer5 = 32;
}

function fiveB(){
    answer5= 31;
}

function fiveC(){
    answer5 = 30;
}

function fiveD(){
    answer5 = 28;
}

function check(){
    if (answer1 === 63){
        points += 1;
    }
    if (answer2 === 14){
        points += 1;
    }
    if (answer3 === 12){
        points += 1;
    }
    if (answer4 === 8){
        points += 1;
    }
    if (answer5 === 30){
        points += 1;
    }
    alert("You got " + points + "/5!")
}
