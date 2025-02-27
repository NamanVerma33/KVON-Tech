class Person{
    constructor(name){
        console.log("Parent Constructor");
        this.species = "Homo species";
        this.name=name;

    }
    eat(){
        console.log("Eats");
    }
    sleep(){
        console.log("Sleep");
    }
}
class Engineer extends Person{
    constructor(name,branch){
        console.log("Child enter")
        super(name);
        this.branch = branch;
        console.log("Child exit");
    }
    work(){
        super.eat();
        console.log("Bulid something new");
    }
}

let engObj = new Engineer("Naman","CSE");  