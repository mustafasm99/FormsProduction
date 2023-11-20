// the javascript for the DASHBORD page 

// Glopel vars 
let oldInstractionPoint     = document.getElementById('instraction-point');
let oldMCQPoint             = document.getElementById('mcqpoint');
let oldField                = document.getElementById('field');

// Glopel functions 

function addCopy(obj){
    console.log(obj);
    parent      = obj.parentElement
    copy        = obj.cloneNode(true)
    lastchild   = parent.lastElementChild
    parent.insertBefore(copy , lastchild)
}

function newMcq(obj){
    oldmcq      = obj.parentElement.parentElement.querySelector('#mcqpoint')
    parent      = oldmcq.parentElement
    copy        = oldmcq.cloneNode(true)
    lastchild   = parent.lastElementChild
    parent.insertBefore(copy , lastchild)
}


// events 

let point          = document.getElementById('point').addEventListener('click' , ()=>{addCopy(oldInstractionPoint)})
let field          = document.getElementById('newfieldbutton').addEventListener('click' , ()=>{addCopy(oldField)})

//testing 

//? oldField.addEventListener('click' , ()=>{console.log("im clicked");}) ! giveing the same id for the field and the button that add the field 
