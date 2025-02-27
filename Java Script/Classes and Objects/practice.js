class User{
    constructor(name,email){
        this.name = name;
        this.email = email;
    }
    viewData(){
        console.log("Visit")
    }
}


class Admin extends User{
    constructor(name,email){
        super(name,email);
    }
    editData(){
        console.log("Edit");
    }
}

let user = new User("Naman","fnfds@gmail.com");
let user1 = new User("Detective","detective@gmail.com");
let admin = new Admin("Adminm","Ffff");

