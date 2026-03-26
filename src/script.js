let internetAccess=true

function syncInput(inputId,rangeId){
document.getElementById(inputId).value=document.getElementById(rangeId).value
}

function setToggle(name,val){
internetAccess=(val==="yes")
}

function predict(){

let study=parseFloat(document.getElementById("studytime").value)||0
let abs=parseFloat(document.getElementById("absences").value)||0
let fail=parseFloat(document.getElementById("failures").value)||0
let health=parseFloat(document.getElementById("health").value)||3
let edu=parseFloat(document.getElementById("paredu").value)||0

let score=5+(study*0.6)-(abs*0.2)-(fail*2)+(health*0.3)+(edu*0.4)

if(score>20)score=20
if(score<0)score=0

let grade="F"
if(score>=16)grade="A"
else if(score>=14)grade="B"
else if(score>=12)grade="C"
else if(score>=10)grade="D"

document.getElementById("result-content").style.display="block"
document.getElementById("score-num").innerHTML=score.toFixed(1)
document.getElementById("grade-letter").innerHTML=grade
}
