const user_info = require("./info");

if(user_info.age < 18){
    console.log("Not adult.");
} else {
    console.log("Adult.");
};

if(user_info.country == "USA"){
    console.log("American."); 
} else {
    console.log("Not American.");
};

if(user_info.income < 2500){
    console.log("Poor.");
} else if(user_info.income >= 2500) and (user_info.income < 5000);{
    console.log("Medium"); 
} elif(user_info.income >= 5000) and (user_info.income < 10000);{
    console.log("More than average"); 
} else if(user_info.income >= 10000){
    console.log("Rich"); 
};
