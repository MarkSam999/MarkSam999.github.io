let a1 = null;
let correct_list = [];
let answer_list = [];
let max = 10;

for(let i = 0; i < max; i++){
    let q_num = i + 1;
    let ca = 0;
    let n1 = 1 + Math.round(Math.random() * 49);
    let perc = 5 * (1 + Math.round(Math.random() * 19));

    ca = Math.round(n1 / 10 * perc) / 10;

    correct_list.push(ca);

    let choices = [];

    let question = document.createElement("h1");
    question.innerHTML = q_num + ". " + n1 + " -> " + perc + "% = ?";
    $("#questions").append(question);

    for(let ch = 0; ch < 4; ch++){
        let choice = Math.round(ca + 1 + Math.random() * 69) / 10 || Math.round(ca - 1 - Math.random() * 69) / 10;
        choices.push(choice);
    }

    let random = Math.floor(Math.random() * 4);
    choices[random] = ca;

    for (let div = 0; div < 4; div++){
        let choiceDiv = document.createElement("div");
        choiceDiv.innerHTML = "<button class='choices' onclick='set(" + i + ", " + choices[div]  + ");'>" + (div + 1) + ")</button>" + "<span onclick='set(" + i + ", " + choices[div]  + ");' class='numbers'>" + choices[div] + "</span>";
        $("#questions").append(choiceDiv);
    }
}

function set(question, value){
    answer_list[question] = value;
}

function check(){
    let points = 0;

    for(let c = 0; c < max; c++){
        if(answer_list[c] == correct_list[c]){
            points += 1;
        }
    }
    
    alert("You got " + points + " out of " + max + "!")
}