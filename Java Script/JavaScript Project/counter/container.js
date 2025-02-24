let currvalue = document.getElementById('number');


let displayValue = 0;
function add(){
    displayValue++;
    display();
}

function sub(){
    if(displayValue>0){
        displayValue--;
    }
    display();
}

function reset(){
    displayValue=0;
    display();
}


function display(){
    currvalue.textContent = displayValue;
}