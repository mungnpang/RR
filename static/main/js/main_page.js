let sublinetext = document.querySelector(".subtitle_item_wrapper")
let content = "Git Lini";
let text = document.querySelector(".text")
let i = 0;
function typing(){
    if (i < content.length) {
    let txt = content.charAt(i);
    text.innerHTML += txt;
    i++;
    }
}
setInterval(typing,300);




// window.addEventListener('scroll',function(){
//     let value = window.scrollY;
//
//     if(value>1720){
//         tutorials_box.style.animation="disappear 1s ease-out forwards"
//     }
//     else if(value>920){
//         tutorials_box.style.animation="slide_from_left  1s ease-out forwards"
//     }
// });