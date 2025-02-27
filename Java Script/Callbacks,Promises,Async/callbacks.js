function sum(a,b){
    console.log(a+b);
}

function calculateSum(a,b,sumCallback){
    sumCallback(a,b);
}

calculateSum(5,6,sum);

function calculateSauare(x,square){
    square(x);
}


calculateSauare(5,(x)=>{
    console.log(x*x);
})