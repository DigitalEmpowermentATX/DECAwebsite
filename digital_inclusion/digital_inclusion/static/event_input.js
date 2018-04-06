$(document).ready(function() {
    //Open registration form
    $("#organization").change(function() {
      location = $("#organization option:selected").val();
    });

    var today = new Date().toISOString().split('.')[0];
    $('#eventDate').val(today);

    //Don't allow date before today
    $("#eventDate").attr('min', today);
});

//Form validation
$(document).ready(function() {

  $("#eventInputForm").validate({
    rules: {
      organization: {
        required: true,
      },
      eventName: {
        required: true
      },
      eventDate: {
        required: true
      },
      eventDescription: {
        required: true
      }
    },
    messages: {
      organization: {
        required: "Please select an organization name or register your organization",
      },
      eventName: {
        required: "Please include an event name"
      },
      eventDate: {
        required: "A valid date and time is required"
      },
      eventDescription: {
        required: "Please include a description of your event"
      }
    }
  });
});
