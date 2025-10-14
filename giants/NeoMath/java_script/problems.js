// Global values
let ca = 0;
let actions = [];
let yourAnswer = 0;
let max = 5;
let points = 0;
let q_num = 0;
let n1 = 0;
let n2 = 0;
let action = 0;
let choices = [];

function start(level){
    $("#play").hide();
    $("#next").show();
    $("#finish").show();

    if(level == 1){
        actions = ['+', "-"];
    };

    gen();

    // Creates a question template
    let question = document.createElement("h1");
    question.id = "currQues";
    question.innerHTML = q_num + ". " + n1 + " " + action + " " + n2 + " = ?";
    $("#questions").append(question);
            
    for(let d = 0; d < 4; d++){
        div = document.createElement("div");
        div.id = "div_" + d;
        div.className = 'choices';
        div.innerHTML = choices[d];
        div.onclick = function(){set(choices[d])};

        $("#questions").append(div);
    }
}

function next(){
    gen();

    if (q_num == max){
        $("#next").hide();
    }

    $("#currQues").text(q_num + ". " + n1 + " " + action + " " + n2 + " = ?");

    for(let div = 0; div < 4; div++){
        $("#div_" + div).text(choices[div]);
        $("#div_" + div).onclick = function(){set(choices[div])};
    }
}

function set(value){
    yourAnswer = value;
    
    if(value == ca){
        points += 1;
        console.log("Correct! Points: " + points);
    } else {
        console.log("Incorrect!");
    };
}

function gen(){
    q_num += 1;
    n1 = 1 + Math.round(Math.random() * 9);
    n2 = 1 + Math.round(Math.random() * 9);
    action = actions[Math.round(Math.random() * (actions.length - 1))];

    if(action == '+'){
        ca = n1 + n2;
    } else if(action == '-'){
        ca = n1 - n2;
        if (n2 > n1){
            res = n2;
            n2 = n1;
            n1 = res;
        }
    }

    for(let ch = 0; ch < 4; ch++){
        let choice = Math.round(ca + 1 + Math.random() * 4) || Math.round(ca - 1 - Math.random() * 4);
        choices.push(choice);
    }

    var random = Math.floor(Math.random() * 4);
    choices[random] = ca;
}

function finish(){
    console.log("You got " + points + " out of " + max + "!");
}

function lvl2(){
    actions = ['*', '/']

    for(let i = 0; i < max; i++){
        let q_num = i + 1;
        let ca = 0;
        let n1 = 1 + Math.floor(Math.random() * 9);
        let n2 = 1 + Math.floor(Math.random() * 9);
        let action = actions[Math.round(Math.random())];
        answer_list.push(ca);
        
        if(action == '*'){
            ca = n1 * n2;
        } else if(action == '/'){
            n1 = n2 * (1 + Math.round(Math.random() * 9));
            ca = n1 / n2;
            if (n2 < 2){
                n2 += 1;
            } else if (n2 > n1){
                res = n2;
                n2 = n1;
                n1 = res;
            }
        }

        correct_list.push(ca);

        let choices = [];

        let question = document.createElement("h1");
        question.innerHTML = q_num + ". " + n1 + " " + action + " " + n2 + " = ?";
        $("#questions").append(question);

        for(let ch = 0; ch < 4; ch++){
            let choice = Math.round(ca + 1 + Math.random() * 4) || Math.round(ca - 1 - Math.random() * 4);
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
}

function lvl3(){
    actions = ['square', 'root']

    for(let i = 0; i < max; i++){
        let q_num = i + 1;
        let txt = "";
        let ca = 0;
        let n1 = 1 + Math.floor(Math.random() * 9);
        let action = actions[Math.round(Math.random())];
        answer_list.push(ca);

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
            choiceDiv.innerHTML = "<button class='choices' onclick='set(" + i + ", " + choices[div]  + ");'>" + (div + 1) + ")</button>" + "<span onclick='set(" + i + ", " + choices[div]  + ");' class='numbers'>" + choices[div] + "</span>";
            $("#questions").append(choiceDiv);
        }
    };
}

function lvl4(){
    actions = ['+', "-", "*", "/"]

    for(let i = 0; i < max; i++){
        let q_num = i + 1;
        let ca = 0;
        let n1 = (1 + Math.floor(Math.random() * 99)) / 10;
        let n2 = (1 + Math.floor(Math.random() * 99)) / 10;
        let action = actions[Math.floor(Math.random() * 4)];

        if(action == '+'){
            ca = n1 + n2;
        } else if(action == '-'){
            ca = n1 - n2;
            if (n2 > n1){
                res = n2;
                n2 = n1;
                n1 = res;
            }
        } else if(action == '*'){
            ca = n1 * n2;
        } else if(action == '/'){
            n1 = n2 * (1 + Math.floor(Math.random() * 99)) / 10;
            ca = n1 / n2;
            if (n2 < 0.1){
                n2 += 0.1;
            } else if (n2 > n1){
                res = n2;
                n2 = n1;
                n1 = res;
            }
        }

        correct_list.push(ca);

        let choices = [];

        let question = document.createElement("h1");
        question.innerHTML = q_num + ". " + n1 + " " + action + " " + n2 + " = ?";
        $("#questions").append(question);

        for(let ch = 0; ch < 4; ch++){
            let choice = Math.round(ca + 1 + Math.random() * 4) || Math.round(ca - 1 - Math.random() * 4);
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
}

function lvl5(){

    for(let i = 0; i < max; i++){
        let q_num = i + 1;
        let ca = 0;
        let n1 = 1 + Math.round(Math.random() * 49);
        let perc = 5 * (1 + Math.round(Math.random() * 19));

        ca = Math.round(n1 / 10 * perc) / 10;

        correct_list.push(ca);

        let choices = [];

        let question = document.createElement("h1");
        question.innerHTML = q_num + ". " + n1 + " → " + perc + "% = ?";
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
}