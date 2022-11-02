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
    let fd =new FormData(document.querySelector("form"))
    let xhr=new XMLHttpRequest()
    xhr.open('POST','/predict',true)
    const disPredict=document.getElementById("disPredict")
    disPredict.innerHTML="Wait we are Predicting !!!!"
    document.getElementById("hiden").style.display="none"
    
    xhr.onreadystatechange = function(){
        if(xhr.readyState == XMLHttpRequest.DONE){
            document.getElementById('disPredict').innerHTML="Prediction: "+xhr.responseText;

        }
    };

    xhr.onload= function(){};

    xhr.send(fd);

}
