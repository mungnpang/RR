$(document).ready(function(){
    card_image()
    recommand()
    bookmark()
    create_history_repo()
    $('.reply-nav').hide()
    $('.hide-reply').hide()
    $('#cancle').hide()
    $('.more_option').hide()
    $('.more_option_reply').hide()
})

async function bookmark(){
    let id = window.location.href.split('/')[4]
    await axios({
        'url':`https://gitlini.com/api/v1/bookmark/read_get_one/${id}`
    })
    .then(function(response){
        if (response.data.result == 'success'){
            $('#bookmark').text('bookmark')
            $('#bookmark').attr('onclick','delete_bookmark()')
        }
    })
    .catch(function(error){
    })
}

async function language_image(language){
    const response = await axios(`https://gitlini.com/api/v1/repository/language/${language}`)
    return response.data.path
  }

async function card_image(){
    const language = $('#language').attr('value')
    let path = await language_image(language)
    $('#image').attr('src',path)    
}

async function recommand(){
    const repo_id = $('#repo').attr('value')
    const response = await axios({
        url: 'https://api.gitlini.com/api/v1/recommand/create',
        method: 'post',
        data: {
            "REPO_ID" : repo_id
        },
    })
    fill_recommand_cards(response.data)
}

let recommand_list = []

async function fill_recommand_cards(repo){
    for (let i=0; i < repo.length ; i ++){
        let id = repo[i].id
        let repo_id = repo[i].repo_id
        let name = repo[i].repo_name
        let stars = repo[i].stars
        let language = repo[i].language
        let image = await language_image(language)
        if (language == null){
            language = ''
        }
        let author = repo[i].full_name.split('/')[0]
        let temp_html = `
        <div id="repo" value=${repo_id}></div>
        <div class="repo-card" onclick="window.location.href='/detail/${id}'">
                <img class="repo-image" id=${id} ></img>
                <div class="repo-summary">
                <div class="repo-items"><span class="material-icons-outlined">person</span>${author}</div>
                    <div class="repo-items"><span class="material-icons-outlined">article</span>${name}</div>
                    <div class="repo-items"><span class="material-icons-outlined">star_outline</span>${stars}</div>
                    <div class="repo-items"><span class="material-icons-outlined">public</span>${language}</div>
                </div>
            </div>
            `
        $('.repo-container').append(temp_html)
        $(`#${id}`).css({
              'background': `url(${image})`,
              'background-size': 'contain',
              'background-repeat': 'no-repeat',
              'background-position': 'center',
            })
        recommand_list.push(id)
    }
    await create_history_reco()
}

async function create_history_repo(){
    let id = window.location.href.split('/')[4]

    await axios({
        'url': 'https://gitlini.com/api/v1/mypage/create/repo',
        'method':'post',
        'data': {
            "REPOSITORY": id
        }
    })
}

async function create_history_reco(){

    await axios({
        'url': 'https://gitlini.com/api/v1/mypage/create/reco',
        'method':'post',
        'data': {
            "RECOMMAND": recommand_list,
        }
    })
}

async function create_comment(){
    let id = window.location.href.split('/')[4]
    let content = $('#comment_create').val()
    if (content.length == 0){
        alert('빈칸은 입력하실 수 없습니다.')
        $('#comment_create').focus()
        return
    }
    await axios({
        url: 'https://gitlini.com/api/v1/comment/create/',
        method: 'post',
        data : {
            'CONTENT': content,
            'REPO_ID': id,
        }
    })
    .then(function(response){
        alert('작성을 완료하였습니다.')
        window.location.reload()
    })
}

async function create_reply(parent){
    let id = window.location.href.split('/')[4]
    let content = $(`#${parent}`).val()
    if (content.length == 0){
        alert('빈칸은 입력하실 수 없습니다.')
        $(`#${parent}`).focus()
        return
    }
    await axios({
        url: 'https://gitlini.com/api/v1/comment/create/',
        method: 'post',
        data : {
            'CONTENT': content,
            'REPO_ID': id,
            'PARENT_COMMENT_ID' : parent
        }
    })
    .then(function(response){
        alert('작성을 완료하였습니다.')
        window.location.reload()
    })
}

function reply_run(id){
    $(`#${id}_reply`).show()
}

function reply_cancle(id){
    $(`#${id}_reply`).hide()
    $(`#${id}`).val('')
}

function show_reply(id){
    $(`.reply_for_${id}`).css({
        "display":"block"
    })
    $(`#show_${id}`).hide()
    $(`#hide_${id}`).show()
}

function hide_reply(id){
    $(`.reply_for_${id}`).css({
        "display":"none"
    })
    $(`#show_${id}`).show()
    $(`#hide_${id}`).hide()
}

let focus_id = ''

$('html').click(function(e){ 
    id = (e.target.id).split('_')[2]
    if(id != focus_id){ 
        $(`#more_option_${focus_id}`).css({
            'display':'none'
        })
        $(`#more_icon_${focus_id}`).removeAttr('style')
    } else if(id == focus_id) {
        $(`#more_option_${id}`).css({
            'display' : "flex",
            'z-index' : "999"
        })
        $(`#more_icon_${id}`).css({
            'animation' : "fade-in 0.1s"
        })
    }
    focus_id = id 
})

function delete_comment_confirm(id){
    var confirm_result = confirm("정말 삭제하시겠습니까?")
    if(confirm_result == true){
        delete_comment_run(id)
    }
}

async function delete_comment_run(id){
    await axios({
        'url':'https://gitlini.com/api/v1/comment/delete',
        'method':'delete',
        'data':{
            "COMMENT_ID" : id
        }
    })
    .then(function(response){
        if (response.data.result == "success"){
            alert("삭제가 완료되었습니다.")
            window.location.reload()
        } else {
            alert(response.data.message)
        }
    })
}


function update_comment_set(id,reply){
    let text = ''
    if (reply == true){
        text = $(`#reply_${id}`).text().split("$ ")[1]
    } else if (reply == false){
        text = $(`#comment_${id}`).text().split("$ ")[1]
    }

    $('#comment_create').val(text)
    $('#submit').attr("onclick",`update_comment_run(${id})`)
    $('#cancle').show()
    $('#submit').text("수정")
    let username = $('.username').text().split(' $')[0]
    $('.username').text(username + " $ (Editing)")
}

function update_comment_cancle(username){
    $('#cancle').hide()
    $('#submit').text("작성")
    $('#comment_create').val('')
    $('#submit').attr("onclick","create_comment()")
    $('.username').text(username + ' $')
}

function update_comment_confirm(id){
    var confirm_result = confirm("정말 수정하시겠습니까?")
    if(confirm_result == true){
        update_comment_run(id)
    }
}

async function update_comment_run(id){
    let content = $('#comment_create').val()
    if (content.length == 0){
        alert('빈칸은 입력하실 수 없습니다.')
        $('#comment_create').focus()
        return
    }
    await axios({
        url: 'https://gitlini.com/api/v1/comment/update',
        method: 'put',
        data : {
            'CONTENT': content,
            'COMMENT_ID': id,
        }
    })
    .then(function(response){
        if (response.data.result == 'success'){
            alert('수정을 완료하였습니다.')
            window.location.reload()
        } else {
            alert(response.data.message)
        }

    })
}

async function create_bookmark(){
    let id = window.location.href.split('/')[4]
    await axios({
        'url':'https://gitlini.com/api/v1/bookmark/create/',
        'method': 'post',
        'data': {
            "REPO_ID" : id
        }
    })
    .then(function(response){
        if (response.data.result == 'success'){
            alert('북마크가 등록되었습니다.')
            window.location.reload()
        } else {
            alert(response.data.message)
            window.location.reload()
        }
    })
    .catch(function(error){
        let confirm_result = confirm("로그인이 필요한 서비스입니다. 로그인페이지로 이동하시겠습니까?")
        if (confirm_result == true){
            window.location.href=`/accounts/login/?next=/detail/${id}`
        }
    })
}

async function delete_bookmark(){
    let id = window.location.href.split('/')[4]
    await axios({
        'url':'https://gitlini.com/api/v1/bookmark/delete',
        'method': 'delete',
        'data' : {
            "REPO_ID" : id
        }
    })
    .then(function(response){
        if (response.data.result == 'success'){
            alert('북마크가 삭제되었습니다.')
            window.location.reload()
        } else {
            alert(response.data.message)
            window.location.reload()
        }
    })
    .catch(function(error){
        alert('error')
    })
}

function login_confirm(id){
    let confirm_result = confirm("로그인이 필요한 서비스입니다. 로그인페이지로 이동하시겠습니까?")
    if (confirm_result == true){
        window.location.href=`/accounts/login/?next=/detail/${id}`
    }
}
