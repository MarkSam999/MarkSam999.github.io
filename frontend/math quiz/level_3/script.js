let actions = ['square', 'root']
let correct_list = [];
let answer_list = [];

for(let i = 0; i < 5; i++){
    let q_num = i + 1;
    let txt = "";
    let ca = 0;
    let n1 = 1 + Math.floor(Math.random() * 9);
    let action = actions[Math.round(Math.random())];

    if(action == 'square'){
        ca = n1 ** 2;
        txt = q_num + ". "  + n1 + "<sup> 2</sup>" + " = ?";
    } else if(action == 'root'){
        ca = 1 + Math.floor(Math.random() * 9);
        n1 = ca ** 2;
        txt = q_num + ". "  + " √" + n1 + " = ?";
    }
    
    correct_list.push(ca);

    let choices = [];

    let question = document.createElement("h1");
    question.innerHTML = txt;
    $("#questions").append(question);

    for(let ch = 0; ch < 4; ch++){
        let choice = Math.round(ca + 1 + Math.random() * 4) || Math.round(ca - 1 - Math.random() * 4);
        choices.push(choice);
    }

    let random = Math.floor(Math.random() * 4);
    choices[random] = ca;

    for(let div = 0; div < 4; div++){
        let choiceDiv = document.createElement("div");
        choiceDiv.innerHTML = "<button class='choices' value='" + choices[div] + "'>" + (div + 1) + ")</button>" + "<span>" + choices[div] + "</span>";
        $("#questions").append(choiceDiv);
    }
    
};

$(".choices").addEventListener(alert(this.innerHTML);