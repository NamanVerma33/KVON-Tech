function getData(data,getnextData){
    setTimeout(()=>{
        console.log("Data ",data);
        if(getnextData){
            getnextData();
        }
    },2000);
}

getData(1,()=>{
    getData(2,()=>{
        getData(3,()=>{
            getData(4);
        });
    });
});


