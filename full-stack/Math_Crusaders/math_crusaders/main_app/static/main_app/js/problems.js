let answer_list = [];
let correct_list = [];
let actions = [];
let max = 5;

function level_1(){
    actions = ['+', "-"]

    for(let i = 0; i < max; i++){
        let q_num = i + 1;
        let ca = 0;
        let n1 = 1 + Math.round(Math.random() * 9);
        let n2 = 1 + Math.round(Math.random() * 9);
        let action = actions[Math.round(Math.random())];

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

function level_2(){
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

function level_3(){
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

function level_4(){
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

function level_5(){

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