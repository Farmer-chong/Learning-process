window.onscroll = function() {scrollFunction()};

function scrollFunction() {console.log(121);
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 30) 
    {
        document.getElementById("rock").style.display = "block";
    } else {
        document.getElementById("rock").style.display = "none";
    }
}


function changpage(){
   
}

function page(){
    var page = document.getElementById("page");
    var next = document.getElementById("next");
    var num = document.getElementById("iframe").src;
    var re = new RegExp("page="+"[0-9]");
    if(re.exec(num) == "page=1")
    {
        page.style.display = "none";
        next.style.display= "no";
        next.href = "video_2.html";
    }
    if(re.exec(num) == "page=2"){
        page.style.display = "no";
        page.href = "video.html"
        next.style.display= "no";
        next.href = "video_3.html";
    }
    if(re.exec(num) == "page=3"){
        page.style.display = "no";
        page.href = "video_2.html";
        next.style.display= "none";
    }
}

