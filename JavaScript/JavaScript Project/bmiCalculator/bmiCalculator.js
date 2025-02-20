document.querySelector('#bmiform').addEventListener('submit',function(e){
    e.preventDefault();

    const gender = document.querySelector('#gender').value;
    const age = parseInt(document.querySelector('#age').value);
    const heightFeet = parseInt(document.querySelector('#height-feet').value);
    const  heightInches = parseInt(document.querySelector('#height-inches').value);
    const weight = parseInt(document.querySelector('#weight').value);

    if(gender && age && heightFeet && heightInches && weight){
        const heightmeters = ((heightFeet * 12) + heightInches) * 0.0254;
        const bmi = weight / (heightmeters * heightmeters);
    
    let category = '';
    if(bmi<18.4){
        category = "underweight";
    }
    else if(bmi>=18.5 && bmi<=24.9){
        category = "Normal";
    }
    else if(bmi>=25 && bmi<=39.9){
        category="Overweight";
    }
    else{
        category="obese";
    }


    const result = document.querySelector('#result');

    result.innerHTML = 'BMI is'+ bmi.toFixed(2)+ 'and category is ' + category;
}
})