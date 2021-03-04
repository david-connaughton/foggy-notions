$(document).ready(function(){
    $(".cover-text").css("display", "none");
    $(".cover-text").fadeIn(2000);
    $("#site-button").mouseover(function(){
        $("#site-button").css("color", '#141411'); 
    });
    $("#site-button").mouseout(function(){
        $("#site-button").css("color", '#ED0000'); 
    });
    $("#form").validate(); 
})
