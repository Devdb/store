function sendForm() {
    let formToSend = $('#cart');
    let formTbody = $('tbody', formToSend)[0];
    let trs = $('tr', formTbody)
    let data = {'deleted': []};
    for (let tr of trs) {
        let input = $('input', tr);
        if (input.prop( "checked" )) {
            let name = input.attr("name");
            let productId = Number(name.split('product_id__')[1]);
            data['deleted'].push(productId);
        }
    }
    let url = formToSend.attr('action');
    console.log(data)

    $.ajax({
        url: url,
        context: data,
        method: 'get'
    }).done(function() {
        console.log('dsasaddsa');
    });
}


$(document).ready(function() {
    $('#updateCartBtn').on(
        'click', function (){sendForm()}
    )
});


