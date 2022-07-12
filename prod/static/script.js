var acc = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        var div = this.parentElement;
        div.style.opacity = "0";
        setTimeout(function(){ div.style.display = "none"; }, 600);
    }
}