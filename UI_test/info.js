var div = document.getElementById('help');
div.style.display = "none";
var opacity =0;
    var intervalID=0;
    function fadeOut()
    {
    intervalID=setInterval(hide,20);
    }
    function fadeIn()
    {
    intervalID=setInterval(show,20);
    }
    function show()
    {
    var img = document.getElementById("help");
    opacity = Number(window.getComputedStyle(img).getPropertyValue("opacity"));
    if(opacity<1)
    {
    opacity=opacity+0.1;
    img.style.opacity=opacity;
    console.log(opacity);
    }
    else
    {
    clearInterval(intervalID);
    }
    }
    function hide()
    {
    var img = document.getElementById("help");
    opacity = Number(window.getComputedStyle(img).getPropertyValue("opacity"));
    if(opacity>0)
    {
    opacity=opacity-0.1;
    img.style.opacity=opacity;
    console.log(opacity);
    }
    else
    {
    clearInterval(intervalID);
    document.getElementById('help').style.display = "none";
    }
}


function togglehelpbox(){
    var div = document.getElementById('help');
    if (div.style.display !== 'none') {
        fadeOut();
    }
    else {
        div.style.display = 'block';
        div.style.opacity = 0;
        fadeIn();
    }
    
    }