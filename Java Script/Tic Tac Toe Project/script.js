const box = document.querySelectorAll('.boxes');
const reset = document.querySelector('#reset') 
const win = document.querySelector('.hide');
const winning = 
[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
];

let Player1 = true;

box.forEach((box) =>{
    box.addEventListener('click',()=>{
        if(Player1){
            box.innerText = "O";
            Player1=false;
        }
        else{
            box.innerText='X';
            Player1=true;
        }
        box.disabled='true';
        checkwin();
    })
});


function checkwin(){
    for(let pattern of winning){
        let position1 = box[pattern[0]].innerText;
        let position2 = box[pattern[1]].innerText;
        let position3 = box[pattern[2]].innerText;
        if(position1!='' && position2!='' && position3!=''){
            if(position1===position2 && position2===position3){
                disabled();
                win.innerText = `Winner is ${position1}`
                win.style.display = 'inline-block';
                win.style.background= 'white';
            }
        }
    }
}

function disabled(){
    box.forEach((box) =>{
            box.disabled='true';
    });
}


function resetgame(){
    box.forEach((box) =>{
        box.disabled=false;
        box.innerText='';
});
}