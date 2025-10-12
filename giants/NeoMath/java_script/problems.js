// Global values
let ca = 0;
let yourAnswer = 0;
let actions = [];
let max = 5;
let points = 0;
let q_num = 0;

function start(level){
    $("#play").hide();
    $("#answer").show();

    if(level == 1){
        actions = ['+', "-"];
    }
    next();
}

function next(){
    if (q_num == max){
        finish();
    } else {
        q_num += 1;
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

        let choices = [];

        for(let ch = 0; ch < 4; ch++){
            let choice = Math.round(ca + 1 + Math.random() * 4) || Math.round(ca - 1 - Math.random() * 4);
            choices.push(choice);
        }

        let random = Math.floor(Math.random() * 4);
        choices[random] = ca;

        if(q_num == 1){
            let question = document.createElement("h1");
            question.id = "currQues";
            question.innerHTML = q_num + ". " + n1 + " " + action + " " + n2 + " = ?";
            $("#questions").append(question);

            let choiceTable = document.createElement("table");
            choiceTable.id = "table_" + q_num;
            $("#questions").append(choiceTable);
            
            for(let cell = 0; cell < 4; cell++){
                let cellHTML = document.createElement("td");
                cellHTML.id = "cell_" + (cell + 1);
                cellHTML.className = "cells";
                cellHTML.onclick = "set(" + choices[cell] + ");";

                if(cell == 0){
                    let row = document.createElement("tr");
                    row.id = "row_1";
                    $("#table_" + q_num).append(row);
                } else if(cell == 2){
                    let row = document.createElement("tr");
                    row.id = "row_2";
                    $("#table_" + q_num).append(row);
                }

                if(cell < 2){
                    $("#row_1").append(cellHTML);
                } else {
                    $("#row_2").append(cellHTML);
                }

                
            }

            for (let div = 0; div < 4; div++){
                    let choiceDiv = document.createElement("div");
                    choiceDiv.innerHTML = "<div class='choices' onclick='set(" + choices[div]  + ");'>" + choices[div] + "</div>";

                    $("#cell_" + (div + 1)).append(choiceDiv);
            }
        } else {
            $("#currQues").text = q_num + ". " + n1 + " " + action + " " + n2 + " = ?";
            alert($("#currQues").text);

            for(let cell = 0; cell < 4; cell++){
                $("#cell_" + (cell + 1)).innerHTML = choices[cell];
                $("#cell_" + (cell + 1)).onclick = "set(" + choices[cell] + ");";
            }
        }
        
        
        
    }
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

function set(value){
    yourAnswer = value;
    
    if(value == ca){
        points += 1;
        alert("Correct! Points: " + points);
    } else {
        alert("Incorrect!");
    };
    next();
}

function finish(){
    alert("You got " + points + " out of " + max + "!")
}