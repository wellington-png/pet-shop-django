//configuração de formset
$('.itemformset_row').formset({
    addText: '<i class="mdi mdi-plus"></i>',
    deleteText: '<i class="mdi mdi-delete"></i>',
    prefix: 'itemcompra_set',
    addCssClass: 'btn btn-success form-item',
    deleteCssClass: 'btn btn-danger'
});

$('.itemcformset_row').formset({
    addText: '<i class="mdi mdi-plus"></i>',
    deleteText: '<i class="mdi mdi-delete"></i>',
    prefix: 'itemconsulta_set',
    addCssClass: 'btn btn-success form-item',
    deleteCssClass: 'btn btn-danger'
});


$('.itemsformset_row').formset({
    addText: '<i class="mdi mdi-plus"></i>',
    deleteText: '<i class="mdi mdi-delete"></i>',
    prefix: 'itemservico_set',
    addCssClass: 'btn btn-success form-item',
    deleteCssClass: 'btn btn-danger'
});


//estilo fomrset
add_button_item = document.getElementsByClassName("form-item");
add_button_item[0].onclick = function(){
    $('form').find(':input').addClass('form-control');
    $('form').find(':checkbox,:file').removeClass('form-control');
};
$('form').find(':input').addClass('form-control');
$('form').find(':checkbox,:file').removeClass('form-control');
