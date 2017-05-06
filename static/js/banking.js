 /* -------------------Prepare JavaScript for the banking app----------------------------*/


 /* jQuery Pre loader
  -----------------------------------------------*/
$(window).load(function(){
    $('.preloader').fadeOut(1000);
});


 /* Page focusing on specific section On-Pageload
  -----------------------------------------------*/
$(window).load(function(){
    var url = window.location.href;
    if (url = "http://carlif.pythonanywhere.com/register/") {
        $.scrollTo("section[name = reg_form]");
    }
    if (url = "http://carlif.pythonanywhere.com/login/") {
        $.scrollTo("section[name = login_form]");
    }

    if (url = "http://carlif.pythonanywhere.com/account/") {
        $.scrollTo("section[name = account]");
    }

    if (url = "http://carlif.pythonanywhere.com/account/create/") {
        $.scrollTo("section[name = account_create]");
    }


});


/* Mobile Navigation
    -----------------------------------------------*/
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});


/* HTML document is loaded. DOM is ready.
-------------------------------------------*/
$(document).ready(function() {

  /* Hide mobile menu after clicking on a link
    -----------------------------------------------*/
    $('.navbar-collapse a').click(function(){
        $(".navbar-collapse").collapse('hide');
    });


 /* Parallax section
    -----------------------------------------------*/
  function initParallax() {
    $('#intro').parallax("100%", 0.1);
    $('#overview').parallax("100%", 0.3);
    $('#account').parallax("100%", 0.1);
    $('#login').parallax("100%", 0.2);
    $('#register').parallax("100%", 0.1);
    $('#about').parallax("100%", 0.2);

  }
  initParallax();

  /* Back top
  -----------------------------------------------*/
    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
        $('.go-top').fadeIn(200);
        } else {
          $('.go-top').fadeOut(200);
        }
        });
        // Animate the scroll to top
      $('.go-top').click(function(event) {
        event.preventDefault();
      $('html, body').animate({scrollTop: 0}, 300);
      })


  /* wow
  -------------------------------*/
  new WOW({ mobile: false }).init();

  });

