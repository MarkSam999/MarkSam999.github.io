let actions = ['square', 'root']

for(let i = 0; i < 100; i++){
    let q_num = i + 1;
    let txt = "";
    let ca = 0;
    let n1 = 1 + Math.floor(Math.random(9));
    let action = actions[Math.round(Math.random())];
    if(action == 'square'){
        ca = n1 ** 2;
        txt = q_num + ". "  + n1 + "<sup> 2</sup>" + " = ?";
    } else if(action == 'root'){
        ca = Math.round(Math.random() * 10);
        n1 = ca ** 2;
        txt = q_num + ". "  + " √" + n1 + " = ?";
    }
    let choices = [];
    for(let i = 0; i < 4; i++){
        let choice = Math.round(ca + 1 + Math.random() * 4) || Math.round(ca -1 - Math.random() * 4);
        choices.push(choice);
    }
    let random = Math.floor(Math.random() * 4);
    choices[random] = ca;

    let question = document.createElement("h1");
    question.innerHTML = txt;
    $("#questions").append(question);

    for (let ch = 0; ch < 4; ch++){
        let choiceDiv = document.createElement("div");
        choiceDiv.innerHTML = "<button>" + (ch + 1) + ")</button>" + "<span>" + choices[ch] + "</span>";
        $("#questions").append(choiceDiv);
    }
}