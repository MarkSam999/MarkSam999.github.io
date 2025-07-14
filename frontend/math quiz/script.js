let a1 = null;
let actions = ['+', "-", '*', '/']

let q1n1 = Math.round(Math.random() * 10);
let q1n2 = Math.round(Math.random() * 10);
if(q1n2 == 0){
    q1n2 += 1;
};
let action = actions[Math.round(Math.random() * 3)];
if(action == '+'){
    q1ca = q1n1 + q1n2;
    q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
} else if(action == '-'){
    q1ca = q1n1 - q1n2;
    if (q1n2 > q1n1){
        q1res = q1n2;
        q1n2 = q1n1;
        q1n1 = q1res;
        q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
    }
    q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
} else if(action == '*'){
    q1ca = q1n1 * q1n2;
    q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
} else if(action == '/'){
    q1ca = q1n1 / q1n2;
    if (q1n2 < 2){
        q1n2 += 1;
        q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
    } else if (q1n2 > q1n1){
        q1res = q1n2;
        q1n2 = q1n1;
        q1n1 = q1res;
        q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
    }
    q1txt = "1. "+ q1n1 + " " + action + " " + q1n2 + " = ?";
}
$("#q1").text(q1txt);

let choices = [];
for(let i = 0; i < 4; i++){
    let choice = Math.round(q1ca + Math.random() * 5 || q1ca - Math.random() * 5);
    if ()
    choices.push(choice);
}

console.log(choices);

function check(){
    if(a1 == q1ca){
        alert("Yes!")
    } else{
        alert("No")
    }
}