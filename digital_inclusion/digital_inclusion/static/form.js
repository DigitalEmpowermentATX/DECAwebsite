//Adding Multiple Services
$(document).ready(function() {
    var max_services = 8;
    var services = $(".services-wrapper");
    var add_button = $(".add-service");
    var services_count = 1;

    $(add_button).click(
      function(event){
        event.preventDefault();
        if(services_count < max_services){
            services_count++;
            $(services).append('<div class="form-group row"><label class= "col-sm-2 col-form-label"><a href="#" class="remove-service">Remove</a></label><div class="col-sm-10"><select class="form-control service-group" id="services' + services_count +'" name="services' + services_count +'"><option value="" selected disabled hidden>Choose a Service</option><option>Example Service 1</option><option>Example Service 2</option><option>Example Service 3</option><option>Example Service 4</option><option>Example Service 5</option></select><div class="invalid-feedback">No, you missed this one.</div></div></div>')
        }
        if (services_count == max_services) {
          $(add_button).css('background-color','red');
        }
    }
  );
  $(services).on("click",".remove-service", function(event){
      event.preventDefault();
      $(this).closest('div').remove();
      $(add_button).css('background-color','#003a5c');
      services_count--;

  })
});

//Adding Multiple Users
$(document).ready(function() {
    var max_users = 3;
    var users = $(".users-wrapper");
    var add_button = $(".add-user");
    var user_count = 1;

    $(add_button).click(
      function(event){
        event.preventDefault();
        if(user_count < max_users){
            user_count++;
            $(users).append('<div class="form-group row"><label class="col-sm-2 col-form-label">User ' + user_count +': <a href="#" class="remove-user">Remove </a></label><div class="col"><input type="text" id="user' + user_count +'" name="user' + user_count +'" class="form-control user-group" placeholder="Username" required><div class="invalid-feedback">No, you missed this one.</div></div><div class="col"><input type="text" id="phrase' + user_count +'"name="phrase' + user_count +'" class="form-control" placeholder="Question" required><div class="invalid-feedback">No, you missed this one.</div></div><div class="col"><input type="password" id="response' + user_count +'" name="response' + user_count +'" class="form-control" placeholder="Response" required><div class="invalid-feedback">No, you missed this one.</div></div></div>')
        }
        if (user_count == max_users) {
          $(add_button).css('background-color','red');
        }
    }
  );
  $(users).on("click",".remove-user", function(event){
      event.preventDefault();
      $(this).closest('div').remove();
      $(add_button).css('background-color','#003a5c');
      user_count--;

  })
});

//Form validation
$(document).ready(function() {

  //Custom validation methods
  jQuery.validator.addMethod("alphanumeric", function(value, element) {
    return this.optional(element) || /^[\w.]+$/i.test(value);});

  jQuery.validator.addMethod('phoneUS', function(phone_number, element) {
    phone_number = phone_number.replace(/\s+/g, '');
    return this.optional(element) || phone_number.length > 9 &&
      phone_number.match(/^(1-?)?(\([2-9]\d{2}\)|[2-9]\d{2})-?[2-9]\d{2}-?\d{4}$/);});


  jQuery.validator.addMethod("notEqualToGroup", function (value, element, options) {
        // get all the elements passed here with the same class
        var elems = $(element).parents('form').find(options[0]);
        // the value of the current element
        var valueToCompare = value;
        // count
        var matchesFound = 0;
        // loop each element and compare its value with the current value
        // and increase the count every time we find one
        jQuery.each(elems, function () {
            thisVal = $(this).val();
            if (thisVal == valueToCompare) {
                matchesFound++;
            }
        });
        // count should be either 0 or 1 max
        if (this.optional(element) || matchesFound <= 1) {
            //elems.removeClass('error');
            return true;
        } else {
            //elems.addClass('error');
        }
    });

  $("#registerForm").validate({
    rules: {
      orgName: {
        required: true,
      },
      description: {
        required: true
      },
      websiteURL: {
        required: true,
        url: true
      },
      user1: {
        required: true,
        minlength: 5
      },
      contactName1: {
        required: true,
      },
      phoneNumber: {
        required: true,
        phoneUS: true
      },
      email: {
        required: true,
        email: true
      },
      services1: {
        required: true,
        notEqualToGroup: ['.service-group']
      },
      services2: {
        required: true,
        notEqualToGroup: ['.service-group']
      },
      services3: {
        required: true,
        notEqualToGroup: ['.service-group']
      },
      user1: {
        required: true,
        alphanumeric: true,
        minlength:6,
        notEqualToGroup: ['.user-group']
      },
      phrase1:{
        required: true
      },
      response1: {
        required: true,
        minlength: 8
      },
      user2: {
        required: true,
        alphanumeric: true,
        minlength:6,
        notEqualToGroup: ['.user-group']
      },
      phrase2:{
        required: true
      },
      response2: {
        required: true,
        minlength: 8
      },
      user3: {
        required: true,
        alphanumeric: true,
        minlength:6,
        notEqualToGroup: ['.user-group']
      },
      phrase3:{
        required: true
      },
      response3: {
        required: true,
        minlength: 8
      }
    },
    messages: {
      orgName: {
        required: "Organization Name is required"
      },
      description: {
        required: "A description of your organization is required"
      },
      websiteURL: {
        required: "A url to your organization's website is required",
        url: "A valid url beginning with 'http://' or 'https://' is required"
      },
      contactName1: {
        required: "A Contact Name is required"
      },
      phoneNumber: {
        required: "A phone number is required",
        phoneUS: "A valid US Phone number is required"
      },
      email:{
        required: "An email address is required",
        email: "Email must be a valid email address"
      },
      services1: {
        required: "Select a service",
        notEqualToGroup: "No duplicate services"

      },
      services2: {
        required: "Select a service",
        notEqualToGroup: "No duplicate services"

      },
      services3: {
        required: "Select a service",
        notEqualToGroup: "No duplicate services"
      },
      user1: {
        required: "A username is required",
        alphanumeric: "Username may only consist of letters, numbers, underscores",
        minlength: "Username must be atleast 6 characters long",
        notEqualToGroup: "No duplicate usernames"
      },
      phrase1: {
        required: "A Question or phrase is required"
      },
      response1: {
        required: "A password or response is required",
        minlength: "Must be atleast 8 characters"
      },
      user2: {
        required: "A username is required",
        alphanumeric: "Username may only consist of letters, numbers, underscores",
        minlength: "Username must be atleast 6 characters long",
        notEqualToGroup: "No duplicate usernames"
      },
      phrase2: {
        required: "A Question or phrase is required"
      },
      response2: {
        required: "A password or response is required",
        minlength: "Must be atleast 8 characters"
      },
      user3: {
        required: "A username is required",
        alphanumeric: "Username may only consist of letters, numbers, underscores",
        minlength: "Username must be atleast 6 characters long",
        notEqualToGroup: "No duplicate usernames"
      },
      phrase3: {
        required: "A Question or phrase is required"
      },
      response3: {
        required: "A password or response is required",
        minlength: "Must be atleast 8 characters"
      }
    }
  });
});
