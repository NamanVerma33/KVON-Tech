document.querySelector('#loanform').addEventListener('submit',function(e){
    e.preventDefault();
    const loanAmount = parseInt(document.querySelector('#loan').value);
    const interestRate =parseInt(document.querySelector('#interest').value);
    const loanTerms = parseInt(document.querySelector('#terms').value);
    
    let monthlypayment='';
    let totalinterest='';
    if(loanAmount && interestRate && loanTerms){
        const monthlyinterest = interestRate / 100 / 12;
        const totalPayments = loanTerms;
        monthlypayment = (loanAmount * monthlyinterest)/(1-Math.pow(1+ monthlyinterest,-totalPayments));
        totalinterest = (monthlypayment * totalPayments) - (loanAmount);
    }
    const result = document.querySelector('#result');

    result.innerHTML = 'Total Interest is ' + totalinterest.toFixed(2) + '</br>'+ 'Monthly Interest is ' + monthlypayment.toFixed(2);
})