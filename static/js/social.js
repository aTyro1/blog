tinymce.init({
    selector: "#mytextarea",
    plugins: "emoticons autoresize",
    toolbar: "emoticons",
    toolbar_location: "bottom",
    menubar: false,
    statusbar: false
  });

function addlike()
{
    new_child=document.createElement('img');
    new_child.src='static/dislike.svg';
    parent=document.getElementById('dislikebutton');
    parent.removeChild(parent.firstChild);
    parent.appendChild(new_child);
    node=document.getElementById('likebutton');
    node.innerHTML=`<img src="static/like_filled.png">`;
}
function dislike()
{
    new_child=document.createElement('img');
    new_child.src='static/like.png';
    parent=document.getElementById('likebutton');
    parent.removeChild(parent.firstChild);
    parent.appendChild(new_child);
    node=document.getElementById('dislikebutton');
    node.innerHTML=`<img src="static/dislike_filled.png">`
   
}
function addComment()
{
    if(document.getElementById('comments').style.visibility=='visible')
    {
        document.getElementById('comments').style.visibility='hidden';
    }
    else
    {
        document.getElementById('comments').style.visibility='visible';
    }
}
function share()
{
    if(document.getElementById('share').style.visibility=='visible')
    {
        document.getElementById('share').style.visibility='hidden';
    }
    else
    {
        document.getElementById('share').style.visibility='visible';
    }
}