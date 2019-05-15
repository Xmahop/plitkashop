$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() >= 120) {
            $('#navbar-main').addClass(' fixed-top ');
        } else {
            $('#navbar-main').removeClass(' fixed-top ');
        }
    });
});
var a = document.title
if (document.title == 'Главная') {
    var b = $('.navbar-item').eq(0)
    b.addClass(' navbar-item-active ')
}
if (document.title == 'О нас') {
    var b = $('.navbar-item').eq(1)
    b.addClass(' navbar-item-active ')
}
if (document.title == 'Галерея работ') {
    var b = $('.navbar-item').eq(2)
    b.addClass(' navbar-item-active ')
}
if (document.title == 'Каталог продукции') {
    var b = $('.navbar-item').eq(3)
    b.addClass(' navbar-item-active ')
}
if (document.title == 'Услуги') {
    var b = $('.navbar-item').eq(4)
    b.addClass(' navbar-item-active ')
}
if (document.title == 'Прайс лист') {
    var b = $('.navbar-item').eq(5)
    b.addClass(' navbar-item-active ')
}
if (document.title == 'Контакты') {
    var b = $('.navbar-item').eq(6)
    b.addClass(' navbar-item-active ')
}