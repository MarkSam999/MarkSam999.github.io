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
    for(let sc = 0; sc < 2; sc++){
        let scriptHTML = document.createElement('script');
        scriptHTML.src = "../java_script/" + scriptList[sc] + ".js";
        document.head.append(scriptHTML);
    };
};