$(document).ready(function(){
    $("#search").focus(function() {
      $(".search-box").addClass("border-searching");
      $(".search-icon").addClass("si-rotate");
    });
    $("#search").blur(function() {
      $(".search-box").removeClass("border-searching");
      $(".search-icon").removeClass("si-rotate");
    });
    $("#search").keyup(function() {
        if($(this).val().length > 0) {
          $(".go-icon").addClass("go-in");
        }
        else {
          $(".go-icon").removeClass("go-in");
        }
    });
    $(".go-icon").click(function(){
      $(".search-form").submit();
    });
    $('.loading').hide()
});

var index = 0
let keyword = ''

function keyword_find(){
  return axios({
    url: `http://127.0.0.1:8001/api/v1/recommand/searchkeyword/${keyword}`,
  })
}

function crawling(){
  return axios({
    url: `http://127.0.0.1:8001/api/v1/recommand/crawling_data/`,
    method: 'post',
    data: {'KEYWORD': keyword}
  })
}

function get_data(){
  return axios({
    url: `http://127.0.0.1:8000/api/v1/repository/${keyword}/${index}`
  })
}

function search_keyword(e, step){
  if (e.keyCode == 13){
    $('.loading').show()
    if(step == 'search_second'){
      index = 0
      loading_max = false
    }
    keyword = $(`#${step}`).val()
    keyword_find(keyword)
    .then(function(response){
      const message = response.data.message
      if (message == 'none'){
        search_result_is_none(keyword)
      } else if (message == 'already'){
        search_result_is_already(keyword)
      }
    })
    if (step == 'search_second'){
      $('#repo_cards').empty()
    }
  }
}

function search_result_is_none(){
  crawling(keyword)
    .then(function (response){
      get_data(keyword)
      .then(function (response){
        $('.desktop-screen').hide()
        $('.search-result').show()
          repository_fill(response.data)
        })
    })
}

function search_result_is_already(){
  get_data(keyword)
  .then(function (response){
    $('.desktop-screen').hide()
    $('.search-result').show()
    repository_fill(response.data)
    if (response.data.length != 12){
      loading_max = true
    }
    index = index + 1
  })
}

async function repository_fill(respositories){
  for (let i= 0;  i < respositories.length; i++){
    let name = respositories[i]['repo_name']
    let stars = respositories[i]['stars']
    let language = respositories[i]['language']
    let id = respositories[i]['id']
    let author = respositories[i]['full_name'].split('/')[0]
    console.log(language)
    let image = await language_image(language)
    if (language == 'None'){
      language = ''
    }
    let temp_html = ` 
    <div class="repo-card" onclick="window.location.replace('/detail/${id}')">
            <img class="repo-image" id=${id} ></img>
            <div class="repo-summary">
                <div class="repo-items"><span class="material-icons-outlined">person</span>${author}</div>
                <div class="repo-items"><span class="material-icons-outlined">article</span>${name}</div>
                <div class="repo-items"><span class="material-icons-outlined">star_outline</span>${stars}</div>
                <div class="repo-items"><span class="material-icons-outlined">public</span>${language}</div>
            </div>
        </div>
        `
      $('#repo_cards').append(temp_html)
      $(`#${id}`).css({
        'background': `url(${image})`,
        'background-size': 'contain',
        'background-repeat': 'no-repeat',
        'background-position': 'center',
      })
  }
  $('.loading').hide()
  $('#result-title').text(`${keyword}에 관한 검색결과`)
}

async function language_image(language){
  const response = await axios(`http://127.0.0.1:8000/api/v1/repository/language/${language}`)
  return response.data.path
}
let loading_max = false
$('#repo_cards').scroll(function () {
  if(loading_max == true){
    return
  }
  
  if($(this).scrollTop() + $(this).innerHeight() + 0.3 >= $(this)[0].scrollHeight){ 
    $('.loading').show()    
    setTimeout(function() {
      search_result_is_already()
      $('.loading').hide()
    }, 2500);
  }
})