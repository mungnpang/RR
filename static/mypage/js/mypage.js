$(window).on("load",function () {
    language_image()
  });

async function language_image(){
    let count = $('#length').attr('value')
    let language_list = $(`#${count}`).attr('value')
    console.log(language_list)
    await axios({
        'url': `http://127.0.0.1:8000/api/v1/repository/language_many/`,
        'method':'post',
        'data':{
            'DATA':language_list
        }
    })
    .then(function(response){
        for (let i=0; i < count ; i ++){
            $(`#${i+1}`).css({
                "background-image": `url(${response.data[i]})`
            })
        }
    })
  }