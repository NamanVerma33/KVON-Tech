const employee = {
    calcTax(){
        console.log("Tax is 10%");
    }
}
const employee2 = {
    calcTax : function(){
        console.log("Tax is 20%");
    }
}

const person = {
    fullName : "Naman ",
    salary : 100000,
    calcTax(){
        console.log(`Tax for ${this.fullName} is 30%`);
    }
}

person.__proto__ = employee;

