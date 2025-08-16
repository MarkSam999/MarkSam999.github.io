function level1(){
    let a1 = null;
    let actions = ['+', "-"]
    let correct_list = [];
    let answer_list = [];
    let max = 5;

    for(let i = 0; i < max; i++){
        let q_num = i + 1;
        let ca = 0;
        let n1 = 1 + Math.floor(Math.random() * 9);
        let n2 = 1 + Math.floor(Math.random() * 9);
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

}

function level_3(){
    
}

function level_4(){
    
}

function level_5(){
    
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