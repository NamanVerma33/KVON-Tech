
function myfunction(){
    const bill =  document.querySelector('#amount');
    const rating = document.querySelector('#rating');
    const people = document.querySelector('#people');
    const type = document.querySelector('#type');

    const total = document.querySelector('#totalamount');
    const pay = document.querySelector('#tippay');
    const amountperperson = document.querySelector('#amountperperson');

    let billAmount = parseFloat(bill.value);
    let totalpeople = parseInt(people.value);
    let mealtype = type.value;
    let serviceRating = parseFloat(rating.value);
    if( isNaN(billAmount) || isNaN(totalpeople)){
        total.textContent = "Please enter valid numbers";
        pay.textContent = 'he';
        amountperperson.textContent = 'jhs';
        return;
    }
    let tip;
    switch(serviceRating){
        case 1:
             tip = billAmount * 0.05;
            break;
        case 2:
             tip = billAmount * 0.10;
            break;
        case 3:
             tip = billAmount * 0.15;
            break;
        case 4:
             tip = billAmount * 0.20;
            break;
}

let totalAmount = billAmount + tip;
let amountPerPerson = totalAmount / ;

if(mealType === "dinner"){
    tip += 5;
    totalAmount += 5;
    amountPerPerson +=5;
}

    
}


document.querySelector('#submit').addEventListener('click',myfunction);