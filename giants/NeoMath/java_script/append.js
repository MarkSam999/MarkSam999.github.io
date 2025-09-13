let styleList = [];
let scriptList = [];

function appendCSS(){
    styleList = ['header_signs', 'nav_signs', 'problems', 'progress_bar', 'style', 'text'];
    for(let st = 0; st < 6; st++){
        let styleHTML = document.createElement('link')
        styleHTML.rel = "stylesheet";
        styleHTML.type = "text/css";
        styleHTML.href = "../css/" + styleList[st] + ".css";
        document.head.append(styleHTML);
    };
};
function appendJS(){
    scriptList = ['main_script', 'problems'];
    for(let s = 0; s < 2; s++){
        let styleHTML = document.createElement('link')
        styleHTML.rel = "stylesheet";
        styleHTML.type = "text/css";
        styleHTML.href = "../css/" + styleList[s] + ".css";
        document.head.append(styleHTML);
    };
};