/* ================================ Survey Item Submission =================================== */
// Variables for holding if survey items had beed clicked
let surveyItemId1Clicked = false;
let surveyItemId2Clicked = false;
let surveyItemId3Clicked = false;
let surveyItemId4Clicked = false;
let surveyItemId5Clicked = false;
// SANDA
function surveyItemSubmission(surveyItemId){
    if (surveyItemId == 1){
        surveyItemId1Clicked = true;
    }else if(surveyItemId == 2){
        surveyItemId2Clicked = true
    }else if(surveyItemId == 3){
        surveyItemId3Clicked = true
    }else if(surveyItemId == 4){
        surveyItemId4Clicked = true
    }else if(surveyItemId == 5){
        surveyItemId5Clicked = true
    }
    
    if (surveyItemId1Clicked && surveyItemId2Clicked && surveyItemId3Clicked && surveyItemId4Clicked){
        document.getElementById('complete-step-div').style.display = 'inline-block';
    }
}
/* ========================== Function on clicking the complete Step button ====================== */
function completeTheStep(){
    console.log('Step completion');
    $.ajax({
        type: "POST",
        url: "/dashboard/subscribersSurvey/",
        data: {
            'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function(json) {
            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
            })
              
            Toast.fire({
                icon: 'Survey Ended!',
                title: `Survey Points + 1 ! You'll get Your subscribers soon`
            }).then((value) => {
                window.location.assign('/dashboard/');
            })
            
        },
    });
}
/* ========================= Function to open Every YouTube Channel In New Window ================== */
function openTheYouTubeChannel(url){
    window.open(url,  '_blank', 'toolbar=yes,scrollbars=yes,resizable=yes,top=500,left=500,width=1000,height=800');
}