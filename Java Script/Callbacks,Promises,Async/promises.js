const getpromise = ()=>{
    new Promise((resolve,reject)=>{
    console.log("Promise");
    resolve("Promise resolved");
    });
};


let promise = getpromise();
promise.then(()=>{
    console.log("Promise fullfilled");
})


// promise.then((res)=>{
//     console.log("fulfilled",res);
// })
// p.catch(()=>{
//     console.log("failed");
// })


// function getData(data){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             console.log("Data ",data)
//             resolve("Success");
//         },5000)
//     });   
// }