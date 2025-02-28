const getpromise = ()=>{
    return new Promise((resolve,reject)=>{
        console.log("This is the Promise");
        // resolve("Promise resolved");
        reject("Network error");
    });
};

let promise = getpromise();
promise.then((res)=>{
    console.log("Fullfilled : ",res)
});

promise.catch((err)=>{
    console.log("Rejected : ",err);
});

// function getData(data){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             console.log("Data ",data)
//             resolve("Success");
//         },5000)
//     });   
// }





