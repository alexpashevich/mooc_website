function loadDescriptionFull() {
    console.log('we are here')
    $.get('/load_description_full', {
        'mooc_id': $('#mooc_id').val()
    }).done(function(data) {
        console.log('and we are here finally')
        // var table = $('#lessons');
        // table.html('');
        // data.lessons.forEach(function (lesson) {
        //     var row = $('<tr>');
        //     row.append($('<td>').text(lessons.id));
        //     row.append($('<td>').text(lessons.title));
        //     row.append($('<td>').text(lessons.description));
        //     table.prepend(row);
        // });
        // table.prepend($('<tr> <th>#</th> <th>Название</th> <th>Описание</th></tr>'));
    });
}