class Car{
    constructor(brand){
        console.log("This is the constructor");
        this.brand = brand;
    }
    start(){
        console.log("Start");
    }
    stop(){
        console.log("Stop");
    }
}

let Fortuner = new Car("Fortuner");
Fortuner.start();
Fortuner.stop();

let Alto = new Car();

