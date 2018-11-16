/*
 * Fix for button stuck on focus after mouse out
 * Stackoverflow ID 23443579
 */

$(".btn-xl").mouseup(function(){
    $(this).blur();
})

$(".page-scroll").mouseup(function(){
    $(this).blur();
})
