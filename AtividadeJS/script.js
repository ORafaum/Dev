let button = document.querySelector("#but");
let broken = false;

but.addEventListener("mouseover",e =>{
    if(!broken)
    but.style.background="blue";
});

but.addEventListener("mouseout",e =>{
    if(!broken)
    but.style.background="green";
});

but.addEventListener("click",e =>{
    but.style.background="red";
    but.innerHTML="quebrei";
    broken=true;
});