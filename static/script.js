const related = async ()=>{
    if($('#home').text() != "Home"){
        var topic = $("#topic").text() 
        const response = await fetch("/related/" + topic )
        const text = await response.text()
        $("#related").html(text)
        $("textarea").css("height", $("textarea").prop('scrollHeight') + "px" )
    }  
}

const search = function(){
    $("form").trigger("submit")
}
const openSearch = function(){
    $("nav .bi-search").attr({"class":"bi bi-x-lg", "onclick" : "closeSearch()"})
    $("#search").css("height", "80px")
}
const closeSearch = function(){
    $("nav .bi-x-lg").attr({"class":"bi bi-search", "onclick": "openSearch()"})
    
    $("#search").css("height", "0px")
}

const openNav = function(){
    $("#mobile-nav").css("width" , "75%")
}
const closeNav = function(){
    $("#mobile-nav").css("width" , "0%")
}

$("head").prepend("<!--hello-->")
