let styleList = [];
function appendCSS(){
    styleList = ['header_signs', 'nav_signs', 'problems', 'progress_bar', 'style', 'text'];
    for(let s = 0; s < 6; s++){
        let styleHTML = document.createElement('link')
        styleHTML.rel = "stylesheet";
        styleHTML.type = "text/css";
        styleHTML.href = "../css/" + styleList[s] + ".css"
    };
};