$(document).ready(function () {
    $('button[data-target="modal"]').click(function (e) {
        var pk = $(e.currentTarget).data('pk');

        $.ajax({
            method: 'GET',
            url: `/api/books/${pk}/`,
            dataType: 'json',
            success: function (data, status) {
                $('span#tags').text(data.tags.join(', '));
                $('span#description').text(data.description);
            }
        })

    });
});