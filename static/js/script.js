const btnGen=document.querySelector("#btnGen")

btnGen.addEventListener("click",()=>{
    document.getElementById("hiden").style.display="block"
    alert("Insert details according to your medical prescription")
    btnGen.style.display="none"
    // console.log("hello")
})
// function form_handler(event){
//     event.preventDefault();
// }
const  sendData=()=>{
    console.log("clc")
    document.querySelector("form").addEventListener("submit",(e)=>{e.preventDefault();})

}
