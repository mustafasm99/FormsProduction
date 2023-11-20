// Globel Variables
let courses     = document.querySelectorAll('.data')
let buttons     = document.querySelector('#next')
let inputs      = document.querySelectorAll('input[type = "checkbox"]')
let search      = document.getElementById('search')
let courses_div = document.querySelectorAll('.cource')
let navs        = document.querySelectorAll('.filter')

//  loop for adding the event  listener to all courses 
courses.forEach(e=>{
    e.addEventListener('click', function(){
        var input = e.querySelector('input[type="checkbox"')
        if(input.checked){
            input.checked = false
        }else{
            input.checked = true
        }
        // calling the [ update ] function so update the button 
        update()
       })
})

// function for update the state of the buttons 
function update(){
    for(let i = 0 ; i < inputs.length ; i++)
    {
        if(inputs[i].checked == true){
            buttons.style.display = "block"
            return
        }
    }
    console.log("None");
    buttons.style.display = "none;"
}

// search function // 

search.addEventListener('input' , function(){
    let text = search.value
    courses_div.forEach(e=>{
        if(!e.innerText.toLowerCase().includes(text.toLowerCase()))
        {
            e.style.display = "none";
        }else{
            e.style.display = "block";
        }
    })
})

navs.forEach(function(link){
    link.addEventListener('click' , function(ev){
        ev.preventDefault()

        
        let targetId = this.querySelector('a').dataset.target
        let target   = document.getElementById(targetId)
        console.log(target , targetId);
        document.getElementById('filters-holder').scrollTo(
            {
                left     : target.offsetLeft - 10,
                behavior : 'smooth'
            }
        )
    })
});