let linkList = [];
let styleList = [];
let scriptList = [];

/* the function that adds an html-code to any page where this function is called */
function appendHTML(link_path){
    /* Adds a page that simulates the loading process */
    let loaderDiv = document.createElement("div");
    loaderDiv.id = "loader";
    document.body.append(loaderDiv);

    let loaderText = document.createElement("p");
    loaderText.innerHTML = "Loading...";
    loaderText.id = "loader_text";
    loaderDiv.append(loaderText);

    let progressDiv = document.createElement("div");
    progressDiv.id = "progress_div";
    loaderDiv.append(progressDiv);

    let progressBar = document.createElement("div");
    progressBar.id = "progress_bar";
    progressDiv.append(progressBar);


    /* Adds the header with the links */
    linkList = ['home', 'about', 'course']
    let header = document.createElement("header");
    document.body.append(header);

    for(let l = 0; l < 3; l++){
        let link = document.createElement("a");
        link.className = "header_links";

        if(linkList[l] == 'course'){
            link.href = "education/" + linkList[l] + ".html";
        } else {
            link.href = link_path + linkList[l] + ".html";
        }
        
        header.append(link);

        let linkLogo = document.createElement("div");
        linkLogo.className = "header_signs";
        linkLogo.id = linkList[l];

        link.append(linkLogo);
    }
}

/* this function adds all listed stylesheets to an html-page */
function appendCSS(relt ){
    styleList = ['header_signs', 'nav_signs', 'problems', 'loader', 'style', 'text'];
    for(let st = 0; st < 6; st++){
        let styleHTML = document.createElement('link')
        styleHTML.rel = "stylesheet";
        styleHTML.type = "text/css";
        styleHTML.href = relt    + "css/" + styleList[st] + ".css";
        document.head.append(styleHTML);
    };
};

/* the function that adds all listed js-files to an html-page */
function appendJS(relt){
    scriptList = ['loader', 'problems'];
    for(let sc = 0; sc < 2; sc++){
        let scriptHTML = document.createElement('script');
        scriptHTML.src = relt + "java_script/" + scriptList[sc] + ".js";
        document.head.append(scriptHTML);
    };
};