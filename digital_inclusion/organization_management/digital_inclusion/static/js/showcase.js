$(document).ready(function() {
    $('#other').css('display', 'none');
  
     $('#issue').change(function(){
      if ($(this).val() === 'Other') {
        $('#other').css('display', 'inline');
      } else {
        $('#other').css('display', 'none');
      }
    });
  });