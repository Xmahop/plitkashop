AOS.init();
$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() >= 120) {
            $('#navbar-main').addClass(' fixed-top ');
        } else {
            $('#navbar-main').removeClass(' fixed-top ');
        }
    });
});