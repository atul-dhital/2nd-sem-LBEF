$(document).on('click', 'li', function(){
    $('li').removeClass('active');
    $('ul').toggleClass('expanded');
    $(this).addClass('active');
    var tab_id = $(this).attr('data-tab');
    $('.tab-content').removeClass('current');
    $(this).addClass('current');
    $('#'+tab_id).addClass('current');
  });
  
  