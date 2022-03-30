$(document).ready(function(){
    $('#password_wrap').hide()
    $('#password2_wrap').hide()
    $('#nickname_wrap').hide()
    $('#signup').hide()
    $('.email_checkicon_false').hide()
    $('.password_checkicon_false').hide()
    $('.nickname_checkicon_false').hide()
})

$('#id_email').on('input', function () {
    valid_check('email')
})

$('#id_password1').on('input', function () {
    valid_check('password1')
})

$('#id_password2').on('input', function () {
    repeat_valid_check()
})


$('#id_username').on('input', function() {
    valid_check('username')
})

function pwd_show(password){
    let type = $(`#id_${password}`).attr('type')
    if (type=="password"){
        $(`#id_${password}`).attr('type','text')
        $(`#${password}_show`).attr('viewBox', "0 0 640 512")
        $(`#${password}_show_path`).attr('d', "M150.7 92.77C195 58.27 251.8 32 320 32C400.8 32 465.5 68.84 512.6 112.6C559.4 156 590.7 207.1 605.5 243.7C608.8 251.6 608.8 260.4 605.5 268.3C592.1 300.6 565.2 346.1 525.6 386.7L630.8 469.1C641.2 477.3 643.1 492.4 634.9 502.8C626.7 513.2 611.6 515.1 601.2 506.9L9.196 42.89C-1.236 34.71-3.065 19.63 5.112 9.196C13.29-1.236 28.37-3.065 38.81 5.112L150.7 92.77zM189.8 123.5L235.8 159.5C258.3 139.9 287.8 128 320 128C390.7 128 448 185.3 448 256C448 277.2 442.9 297.1 433.8 314.7L487.6 356.9C521.1 322.8 545.9 283.1 558.6 256C544.1 225.1 518.4 183.5 479.9 147.7C438.8 109.6 385.2 79.1 320 79.1C269.5 79.1 225.1 97.73 189.8 123.5L189.8 123.5zM394.9 284.2C398.2 275.4 400 265.9 400 255.1C400 211.8 364.2 175.1 320 175.1C319.3 175.1 318.7 176 317.1 176C319.3 181.1 320 186.5 320 191.1C320 202.2 317.6 211.8 313.4 220.3L394.9 284.2zM404.3 414.5L446.2 447.5C409.9 467.1 367.8 480 320 480C239.2 480 174.5 443.2 127.4 399.4C80.62 355.1 49.34 304 34.46 268.3C31.18 260.4 31.18 251.6 34.46 243.7C44 220.8 60.29 191.2 83.09 161.5L120.8 191.2C102.1 214.5 89.76 237.6 81.45 255.1C95.02 286 121.6 328.5 160.1 364.3C201.2 402.4 254.8 432 320 432C350.7 432 378.8 425.4 404.3 414.5H404.3zM192 255.1C192 253.1 192.1 250.3 192.3 247.5L248.4 291.7C258.9 312.8 278.5 328.6 302 333.1L358.2 378.2C346.1 381.1 333.3 384 319.1 384C249.3 384 191.1 326.7 191.1 255.1H192z")
    } else {
        $(`#id_${password}`).attr('type','password')
        $(`#${password}_show`).attr('viewBox', "0 0 576 512")
        $(`#${password}_show_path`).attr('d', "M160 256C160 185.3 217.3 128 288 128C358.7 128 416 185.3 416 256C416 326.7 358.7 384 288 384C217.3 384 160 326.7 160 256zM288 336C332.2 336 368 300.2 368 256C368 211.8 332.2 176 288 176C287.3 176 286.7 176 285.1 176C287.3 181.1 288 186.5 288 192C288 227.3 259.3 256 224 256C218.5 256 213.1 255.3 208 253.1C208 254.7 208 255.3 208 255.1C208 300.2 243.8 336 288 336L288 336zM95.42 112.6C142.5 68.84 207.2 32 288 32C368.8 32 433.5 68.84 480.6 112.6C527.4 156 558.7 207.1 573.5 243.7C576.8 251.6 576.8 260.4 573.5 268.3C558.7 304 527.4 355.1 480.6 399.4C433.5 443.2 368.8 480 288 480C207.2 480 142.5 443.2 95.42 399.4C48.62 355.1 17.34 304 2.461 268.3C-.8205 260.4-.8205 251.6 2.461 243.7C17.34 207.1 48.62 156 95.42 112.6V112.6zM288 80C222.8 80 169.2 109.6 128.1 147.7C89.6 183.5 63.02 225.1 49.44 256C63.02 286 89.6 328.5 128.1 364.3C169.2 402.4 222.8 432 288 432C353.2 432 406.8 402.4 447.9 364.3C486.4 328.5 512.1 286 526.6 256C512.1 225.1 486.4 183.5 447.9 147.7C406.8 109.6 353.2 80 288 80V80z")
    }
}

async function valid_check(input_id) {
    let input_value = $(`#id_${input_id}`).val()
    let type = input_id + 'check'
    let key = input_id.toUpperCase()
    let data ={}
    data[key] = input_value
    const response = await fetch(`/api/v1/user/${type}`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
if (response['result'] == "success"){
    if (input_id == "email"){
        $('#password_wrap').show()
    } else if (input_id == "password1"){
        $('#password2_wrap').show()
    } else if (input_id == "nickname"){
    }
    $(`#${input_id}_check`).attr('value','True')
    $(`#${input_id}_check`).text('')
    $(`#${input_id}_check`).hide()
    $(`#${input_id}_icon`).attr('class','check_true')
    $(`#${input_id}_icon`).attr('viewBox', '0 0 448 512')
    $(`#${input_id}_icon_path`).attr("d", "M438.6 105.4C451.1 117.9 451.1 138.1 438.6 150.6L182.6 406.6C170.1 419.1 149.9 419.1 137.4 406.6L9.372 278.6C-3.124 266.1-3.124 245.9 9.372 233.4C21.87 220.9 42.13 220.9 54.63 233.4L159.1 338.7L393.4 105.4C405.9 92.88 426.1 92.88 438.6 105.4H438.6z")
    if ($('#email_check').attr('value') == 'True' & $('#password1_check').attr('value') == 'True' & $('#username_check').attr('value') == 'True' & $('#password2_check').attr('value') == 'True'){
        $('#signup').show()
    } 
} else {
    $(`#${input_id}_check`).attr('value','False')
    $(`#${input_id}_check`).text(response['message'])
    $(`#${input_id}_check`).show()
    $(`#${input_id}_icon`).attr('class','check_false')
    $(`#${input_id}_icon`).attr('viewBox', '0 0 320 512')
    $(`#${input_id}_icon_path`).attr("d", "M310.6 361.4c12.5 12.5 12.5 32.75 0 45.25C304.4 412.9 296.2 416 288 416s-16.38-3.125-22.62-9.375L160 301.3L54.63 406.6C48.38 412.9 40.19 416 32 416S15.63 412.9 9.375 406.6c-12.5-12.5-12.5-32.75 0-45.25l105.4-105.4L9.375 150.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 210.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-105.4 105.4L310.6 361.4z")
    $(`.${input_id}_checkicon_false`).show()
    if ($('#email_check').attr('value') != 'True' | $('#password1_check').attr('value') != 'True' | $('#username_check').attr('value') == 'True' | $('#password2_check').attr('value') != 'True'){
        $('#signup').hide()
    } 
}
}

function repeat_valid_check() {
    let input_value = $(`#id_password1`).val()
    let input2_value = $(`#id_password2`).val()
    if (input_value == input2_value) {
        $(`#password2_check`).attr('value','True')
        $(`#password2_check`).text('')
        $(`#password2_check`).hide()
        $(`#password2_icon`).attr('class', 'check_true')
        $(`#password2_icon`).attr('viewBox', '0 0 448 512')
        $(`#password2_icon_path`).attr("d", "M438.6 105.4C451.1 117.9 451.1 138.1 438.6 150.6L182.6 406.6C170.1 419.1 149.9 419.1 137.4 406.6L9.372 278.6C-3.124 266.1-3.124 245.9 9.372 233.4C21.87 220.9 42.13 220.9 54.63 233.4L159.1 338.7L393.4 105.4C405.9 92.88 426.1 92.88 438.6 105.4H438.6z")
        $('#nickname_wrap').show()
    }
    else{
        $(`#password2_check`).attr('value','False')
        $(`#password2_check`).text("입력한 첫번째 비밀번호와 다릅니다.")
        $(`#password2_check`).show()
        $(`#password2_icon`).attr('class','check_false')
        $(`#password2_icon`).attr('viewBox', '0 0 320 512')
        $(`#password2_icon_path`).attr("d", "M310.6 361.4c12.5 12.5 12.5 32.75 0 45.25C304.4 412.9 296.2 416 288 416s-16.38-3.125-22.62-9.375L160 301.3L54.63 406.6C48.38 412.9 40.19 416 32 416S15.63 412.9 9.375 406.6c-12.5-12.5-12.5-32.75 0-45.25l105.4-105.4L9.375 150.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 210.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25l-105.4 105.4L310.6 361.4z")
        $(`.password2_checkicon_false`).show()
    }

}
