let a1 = null;
let actions = ['*', '/']

for(let i = 0; i < 5; i++){
    let q_num = i + 1;
    let ca = 0;
    let n1 = Math.round(1 + Math.random(9));
    let n2 = Math.round(1 + Math.random(9));
    let action = actions[Math.round(Math.random())];
    if(action == '*'){
        ca = n1 * n2;
    } else if(action == '/'){
        n1 = n2 * Math.round(1 + Math.random(9));
        ca = n1 / n2;
        if (n2 < 2){
            n2 += 1;
        } else if (n2 > n1){
            res = n2;
            n2 = n1;
            n1 = res;
        }
    }
    let choices = [];
    for(let i = 0; i < 4; i++){
        let choice = Math.round(ca + Math.random() * 5) || Math.round(ca + Math.random() * 5);
        if (choice < 0){
            choice = 0;
        }
        if (choice == choices[i - 1]){
            choice = choice + 1 || choice - 1;
        }
        choices.push(choice);
    }
    let random = Math.floor(Math.random() * 4);
    choices[random] = ca;

    let question = document.createElement("h1");
    question.innerHTML = q_num + ". " + n1 + " " + action + " " + n2 + " = ?";
    $("#questions").append(question);

    for (let ch = 0; ch < 4; ch++){
        let choiceDiv = document.createElement("div");
        choiceDiv.innerHTML = "<button>" + (ch + 1) + ")</button>" + "<span>" + choices[ch] + "</span>";
        $("#questions").append(choiceDiv);
    }
}