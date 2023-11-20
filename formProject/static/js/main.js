videos = document.querySelectorAll('.video')


videos.forEach(ele=>{
    fatherDiv = ele.parentNode;
        inputs = fatherDiv.querySelectorAll('input')
        inputs.forEach(e =>{
            e.style= "opacity:0;"
        })
})


videos.forEach(ele => {
    ele.querySelector('video').addEventListener('ended',function(){
        fatherDiv = ele.parentNode;
        inputs = fatherDiv.querySelectorAll('input')
        inputs.forEach(e =>{
            e.style= "display:block;"
        })
    })
});