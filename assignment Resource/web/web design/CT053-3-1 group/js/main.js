(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').css('top', '0px');
        } else {
            $('.sticky-top').css('top', '-100px');
        }
    });
    
    
    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";
    
    $(window).on("load resize", function() {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
            function() {
                const $this = $(this);
                $this.addClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "true");
                $this.find($dropdownMenu).addClass(showClass);
            },
            function() {
                const $this = $(this);
                $this.removeClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "false");
                $this.find($dropdownMenu).removeClass(showClass);
            }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
})(jQuery);






function toggleHelpMessage() {
    var helpMessage = document.getElementById('help-message');
    if (helpMessage.style.display === 'none') {
      helpMessage.style.display = 'block';
    } else {
      helpMessage.style.display = 'none';
    }
  }
 
    // Show and hide login modal with fade animation
    function showLoginForm() {
        $('#loginModal').modal('show');
    }

    function hideLoginForm() {
        $('#loginModal').modal('hide');
    }

    // Show and hide sign-up modal with fade animation
    function showSignUpForm() {
        $('#signUpModal').modal('show');
    }

    function hideSignUpForm() {
        $('#signUpModal').modal('hide');
    }

    function showClassSelection() {
        $('#classSelectionModal').modal('show');
    }

    function hideClassSelection() {
        $('#classSelectionModal').modal('hide');
    }

    function showBookingForm(course) {
        hideClassSelection();
        $('#bookingFormAWS, #bookingFormLiveProject, #bookingFormJavaScript').hide();
        if (course === 'AWS Class') {
            $('#bookingFormAWS').modal('show');
        } else if (course === 'Live Project of Web') {
            $('#bookingFormLiveProject').modal('show');
        } else if (course === 'JavaScript Class') {
            $('#bookingFormJavaScript').modal('show');
        }
    }

    function hideBookingForm() {
        $('#bookingFormAWS, #bookingFormLiveProject, #bookingFormJavaScript').modal('hide');
    }

    function submitBookingForm(event, course) {
        event.preventDefault(); // Prevent form submission
        // You can perform any additional form submission handling here if needed.
        // For demonstration purposes, let's hide the form and reset the fields after submission:
        hideBookingForm();
        event.target.reset(); // Reset the form fields
    }

