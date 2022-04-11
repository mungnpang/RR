$(window).on("load",function () {
    language_image()
  });

async function language_image(){
    let count = $('#length').attr('value')
    let language_list = []
    for (let i=0; i < count; i ++){
        let language = $(`#${i+1}`).attr('value')
        language_list.push(language)
    }
    
    await axios({
        'url': `https://gitlini.com/api/v1/repository/language_many/`,
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