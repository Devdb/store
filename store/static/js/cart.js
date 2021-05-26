function deleteFromCart(){
    let formToSend = $('#cart');
    let formTbody = $('tbody', formToSend)[0];
    let trs = $('tr', formTbody)
    let data = {'deleted': []};
    for (let tr of trs) {
        let input = $('input', tr);
        if (input.prop("checked")) {
            let name = input.attr("name");
            let productId = Number(name.split('product_id__')[1]);
            data['deleted'].push(productId);
        }
    }
    sendForm(formToSend, data)
}

function sendForm(form, data){
    data['csrfmiddlewaretoken'] = getCookies(document.cookie)['csrftoken'];

    $.ajax({
        url: form.attr('action'),
        data: data,
        method: form.attr('method'),
    }).done(function(overall_sum) {
        $('tr.table-danger', 'form#cart').remove();
        $('#overall_sum').text(overall_sum);
        $('#notification').removeClass().addClass('alert alert-primary').text('Successfully deleted').fadeIn().delay(2000).fadeOut();
    }).fail(function(answerExc){
        $('#notification').removeClass().addClass('alert alert-danger').text(answerExc.responseText).fadeIn().delay(10000).fadeOut();
    });
}

$(document).ready(function() {
    $('#updateCartBtn').on('click', function(){
        deleteFromCart()
    })

    $('input[type=checkbox]', 'form#cart').on('click', function() {
        if (this.checked) {
            $(this.closest('tr')).addClass('table-danger');
        } else {
            $(this.closest('tr')).removeClass('table-danger');
        }
    });
});


