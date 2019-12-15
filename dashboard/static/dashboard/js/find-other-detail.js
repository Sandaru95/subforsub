function spawnCommentBox(){
    document.getElementById('commenting-box').style.display = 'block';
}
function postComment(){
    console.log('Posting Comment...');
    let commentValue = document.getElementById('comment-input').value;
    let currentUserPk = currentDetailUserPk;
    $.ajax({
        type: "POST",
        url: `/dashboard/findOther/detail/${currentUserPk}/comment/`,
        data: {
            'comment-value':commentValue,
            'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function(json) {
            console.log('Success!');
            let newCommentObj = {};
            newCommentObj['commentText'] = commentValue;
            newCommentObj['owner'] = currentLoggedUserName;
            ownerComments.push(newCommentObj);
            updateCommentList();
        },
        error: function(json){
            console.log(json);
        }
    });
}
function updateCommentList(){
    // 'comment-show-space'
    let tempView = ``;
    if (ownerComments.length > 0){
        for (let i = 0; i < ownerComments.length; i++){
            tempView += `
                <p>${ownerComments[i]['commentText']} by ${ownerComments[i]['owner']}</p>
            `;
            
        };
    }else{
        tempView = '<p>No Comments to show Yet!</p>'
    }
    document.getElementById('comment-show-space').innerHTML = tempView;
};
updateCommentList();