$(document).ready(function(){
    $('.contents-box').hide()
    $('#history-intro').show()
});

$('.history-intro').click(function(){
    var intro = $(this).attr('class');
    $('.contents-box').hide()
    $(`#${intro}`).show()
});

$('li').click(function(){
    var tab = $(this).attr('class');
    $('.contents-box').hide()
    $(`#${tab}`).show()
    $('li').css({
        'font-weight':'normal'
    })
    $(`.${tab}`).css({
        'font-weight':'bold'
    })
});