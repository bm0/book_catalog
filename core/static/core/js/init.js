$(document).ready(function () {
    Materialize.updateTextFields();
    $('.button-collapse').sideNav();
    $('select').material_select();
    $('.tooltipped').tooltip({delay: 50});
    $('.modal').modal();

    $.extend($.fn.pickadate.defaults, {
        monthsFull: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        monthsLetter: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
        monthsShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],

        weekdaysFull: ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'],
        weekdaysLetter: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
        weekdaysShort: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],

        labelMonthNext: "Следующий месяц",
        labelMonthPrev: "Предыдущий месяц",
        labelMonthSelect: "Выберите месяц ",
        labelYearSelect: "Выберите год",

        today: '<i class="material-icons waves-effect">today</i>',
        clear: '<i class="material-icons waves-effect">delete</i>',
        close: '<i class="material-icons waves-effect">done</i>',
        format: 'mm/dd/yyyy',
        hiddenPrefix: undefined,
        hiddenSuffix: undefined,
        hiddenName: undefined
    });

    $('.datepicker').pickadate({
        selectMonths: true,
        selectYears: 15,

        closeOnSelect: true
    });
});
