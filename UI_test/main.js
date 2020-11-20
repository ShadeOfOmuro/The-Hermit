function go_another() {
    location.replace("info.html");
    console.log("done");
}
var intervalID = setInterval(loop_increase,1)
var num = Number(document.getElementById("el").innerHTML);
function loop_increase() {
    var obj = document.getElementById("el")
    if(num == 122222265){
        clearInterval(intervalID);
    }
    else{
        obj.innerHTML = String(num);
        num += 1;
    }
}