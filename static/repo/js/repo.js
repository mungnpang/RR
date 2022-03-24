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
});

function search(e){
  if (e.keyCode == 13){
    let keyword = $('.search__input').val()
    axios({
      url: 'http://127.0.0.1:8001/api/v1/recommand/crawling_data/',
      method: 'post',
      data: {
          "KEYWORD" : keyword
      }
    })
    .then(function(response) {
    response = response.json()
    alert(response)
    }
    )
    
  }
}
