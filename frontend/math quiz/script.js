let a1 = 0;
let actions = ['+', "-", '*', '/']

let q1n1 = Math.round(Math.random() * 10);
let q1n2 = Math.round(Math.random() * 10);
if(q1n2 == 0){
    q1n2 = Math.round(Math.random() * 10);
};
let action = actions[Math.round(Math.random() * 3)];
if(action == '+'){
    q1ca = q1n1 + q1n2;
    q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
} else if(action == '-'){
    q1ca = q1n1 - q1n2;
    q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
} else if(action == '*'){
    q1ca = q1n1 * q1n2;
    q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
} else if(action == '/'){
    q1ca = q1n1 / q1n2;
    if (q1n2 < 2 || qi){
        q1n2 = Math.round(Math.random() * 10);
        q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
    }
}
$("#q1").text(q1txt);

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
