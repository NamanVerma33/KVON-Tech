const accesskey = 'EMQBVxLP7FyI-2_fqXCNuqXmDxiXvz4cnxP7cEfO5HQ';
const form = document.querySelector('form');
const Searchinput = document.querySelector('.input');
const images = document.querySelector('.images-container');
const load = document.querySelector('.submit');


const fetchimages = async (input,page) =>{
    try {
        if(page===1){
            images.innerHTML = '';
    
        }
        const url = `https://api.unsplash.com/search/photos/?query=${input}&per_page=28&page=${page}&client_id=${accesskey}`;
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
    
    
    
        if(data.results.length>0){
            data.results.forEach(photo => {
                // Image container
                const imageBox = document.createElement('div');
                imageBox.classList.add('imagediv')
                imageBox.innerHTML = `<img src=${photo.urls.regular}>`
            
                // Overlay effect 
                const overlay = document.createElement('div');
                overlay.classList.add('overlay');
                
            
                // Overlay text 
                const overlayText = document.createElement('h3');
                overlayText.classList.add('overlayText')
                overlayText.innerText = `${photo.description}`
            
            
                overlay.appendChild(overlayText);
                imageBox.appendChild(overlay);
                images.appendChild(imageBox);
                });
            
                if(data.total_pages === page){
                    load.style.display="none";  
                }
                else{
                    load.style.display="block";
                }
        }
        else{
            images.innerHTML = `<h1>Image Not found.</h1>`
            load.style.display="none";  
        }
    } catch (error) {
        images.innerHTML = `<h1>Failed.Please try to fetch image later.</h1>`
        
    }
    
   
}
let page = 1;
form.addEventListener('submit',(e)=>{
    e.preventDefault();
    const input = Searchinput.value.trim();
    if(input != ''){
        page = 1;
        fetchimages(input,page);
    }
    else{
        images.innerHTML = `<h1>Enter the search query.</h1>`
        if(load.style.display="block"){
            load.style.display="none";
        }
    }
})


load.addEventListener('click',()=>{
    fetchimages(Searchinput.value.trim(),++page);
})