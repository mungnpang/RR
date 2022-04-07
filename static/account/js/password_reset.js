$(document).ready(function(){
    $('#email_check_btn').hide()
})


$('#id_email').on('input', function () {
    email_validation()
})

async function email_validation(){
    let email = $('#id_email').val()
    
    await axios({
        url: 'https://gitlini.com/api/v1/user/email_db_check',
        method: 'post',
        data: {
            "EMAIL" : email
        },
    })
    .then(function(response){
        $('#email_check_btn').show()
        $('#check_false').text('')
        $('#email_check_btn').attr('disabled', false);
    })
    .catch(function(error){
        $('#email_check_btn').hide()
        $('#check_false').text(error.response.data.detail)
        $('#email_check_btn').attr('disabled', true);
    })
}
