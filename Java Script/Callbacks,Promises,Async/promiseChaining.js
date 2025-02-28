function async1(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            console.log("Data 1");
            resolve("Successfull ");
        },5000)
    });
};
function async2(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            console.log("Data 2");
            resolve("Successfull ");
        },5000)
    });
};

console.log("Fetching Data 1....");
let p1 = async1();
let p2 = async2();
p1.then((res)=>{
    console.log("Resolved ",res);
})

p2.then((res)=>{
    console.log("Resolved ", res)
})
