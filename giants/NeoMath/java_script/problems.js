// Starts the game
function start(level){
    $("#play").hide();
    $("#next").show();
    $("#finish").show();
    $("#timebar").show();

    // Chooses the possible actions based on the chosen level
    if(level == 1){
        actions = ['+', "-"];
    } else if (level == 2){
        actions = ["*", "/"];
    } else if(level == 3){
        actions = ["+", "-", "*", "/"];
    } else if(level == 4){
        actions = ["^", "√"];
    } else if(level == 5){
        actions = ["%"];
    };

    gen();

    // Creates a question template
    let question = document.createElement("h1");
    question.id = "currQues";
    if(action == "^"){
        question.innerHTML = q_num + ". "  + n1 + "<sup> 2</sup>" + " = ?";
    } else if(action == "√"){
        question.innerHTML = q_num + ". "  + " √" + n1 + " = ?";
    } else if (action == "%"){
        question.innerHTML = q_num + ". " + n1 + " → " + perc + "% = ?";
    } else {
        question.innerHTML = q_num + ". " + n1 + " " + action + " " + n2 + " = ?";
    }
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

// Replaces the innerHTML of the existing elements
function next(){
    gen();

    if(q_num == max){
        $("#next").hide();
    }

    if(action == "^"){
        $("#currQues").html(q_num + ". "  + n1 + "<sup> 2</sup>" + " = ?");
    } else if(action == "√"){
        $("#currQues").html(q_num + ". "  + " √" + n1 + " = ?");
    } else if(action == "%"){
        $("#currQues").text(q_num + ". " + n1 + " → " + perc + "% = ?");
    } else {
        $("#currQues").text(q_num + ". " + n1 + " " + action + " " + n2 + " = ?");
    }
    
    for(let div = 0; div < 4; div++){
        $("#div_" + div).text(choices[div]);
        $("#div_" + div).click(function(){
            set(choices[div]);
        });
    }
}

// Generates the question and the available choices
function gen(){
    q_num += 1;
    seconds = 5;
    $("#time").css("width", "100%");

    n1 = 1 + Math.round(Math.random() * 9);
    n2 = 1 + Math.round(Math.random() * 9);
    action = actions[Math.round(Math.random() * (actions.length - 1))];
    
    if(action == '+'){
        ca = n1 + n2;
    } else if(action == '-'){
        ca = n1 - n2;
        if (n2 > n1){
            nx = n2;
            n2 = n1;
            n1 = nx;
            ca = n1 - n2;
        }
    } else if(action == "*"){
        ca = n1 * n2;
    } else if(action == "/"){
        n1 = n2 * (1 + Math.round(Math.random() * 9));
        ca = n1 / n2;
        if (n2 < 2){
            n2 += 1;
        } else if (n2 > n1){
            res = n2;
            n2 = n1;
            n1 = res;
        };
    } else if(action == "^"){
        ca = n1 ** 2;
    } else if(action == "√"){
        ca = 1 + Math.floor(Math.random() * 9);
        n1 = ca ** 2;
    } else if(action == "%"){
        perc = 5 * (1 + Math.round(Math.random() * 19));
        ca = Math.round(n1 / 10 * perc) / 10;
    };

    for(let ch = 0; ch < 4; ch++){
        let choice = Math.round(ca + 1 + Math.random() * 4) || Math.round(ca - 1 - Math.random() * 4);
        choices[ch] = choice;
    };

    var random = Math.floor(Math.random() * 4);
    choices[random] = ca;

    timer();
};

// Shows how many points did a player get and gives an opportunity to play again
function finish(){
    alert("You got " + points + " out of " + max + "!");
    $("#replay").show();
};

// Launches the game straight from the beginning
function replay(){
    q_num = 0;
    points = 0;
    $("#replay").hide();
    $("#next").show();
    next();
};

// Launches the timer
function timer(){
    let time = setInterval(function(){
        seconds--;
        $("#time").css("width", (100 * seconds / 5) + "%");
        $("#seconds").text(seconds);

        if(seconds < 0){
            clearInterval(time);
            seconds++;
            $("#seconds").text(seconds);
            
            show();
        };
    }, 1000);
};

// Sets an answer chosen by a player
function set(value){
    yourAnswer = value;

    $(".choices").css("cursor", "not-allowed");
    var choiceClass = $(".choices");
    choiceClass.click()

    show();
    
    if(value == ca){
        points += 1;
        console.log("Correct! Points: " + points);
    } else {
        console.log("Incorrect!");
    };
}


// Shows which choice is correct by changing the lightning color
function show(){
    for(let ch = 0; ch < 4; ch++){
        if($("#div_" + ch).text() == ca){
            $("#div_" + ch).css("text-shadow", "0 0 5px green, 0 0 15px green, 0 0 25px green, 0 0 35px green, 0 0 45px green");
        } else {
            $("#div_" + ch).css("text-shadow", "0 0 5px red, 0 0 15px red, 0 0 25px red, 0 0 35px red, 0 0 45px red");
        }
    };
}

// Global values in alphabetical order
let actions = [];
let action = 0;
let ca = 0;
let choices = [0, 0, 0, 0];
let max = 5;
let n1 = 0;
let n2 = 0;
let perc = 0;
let points = 0;
let q_num = 0;
let seconds = 0;
let txt = "";
let yourAnswer = 0;