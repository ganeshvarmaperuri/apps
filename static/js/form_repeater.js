//$(document).ready(function(){
//    $('.answer_div').hide();
//});
//
//$(document).on('change', '.answer_type', function(){
//    var prefix = $(this).closest('.question_item').attr('id')
//    var option_type = $('#id_'+prefix+'-option_type').val()
//    var answer_type = $('#id_'+prefix+'-answer_type').val()
//    if (option_type == ''){
//        alert("Please select the option type");
//    }else{
//
//        console.log($('#'+prefix+'_get_option').val())
//        console.log(answer_type)
//        $.ajax({
//            url: $('#'+prefix+'_get_option').val(),
//            type: 'GET',
//            data:{'option_type':option_type},
//            dataType: 'json',
//            success: function (data) {
//                console.log(data)
//                if (answer_type === 'Radio'){
//                    var $radioInput = $('<input>', {
//                      'type': 'radio'
//                    });
//                    $('#id_'+prefix+'_answer').replaceWith(
//                        $radioInput
//                    );
//                    $('#div_'+prefix+'_answer').show();
//                }
//
//            },
//        });
//
//    }
//
//});