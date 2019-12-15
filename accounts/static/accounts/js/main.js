window.addEventListener('keyup', () => {
    let inputList = document.getElementsByTagName('input');
    for(let i = 0; i < inputList.length; i++){
        if(inputList[i].type != 'submit'){
            if(inputList[i].value == ''){
                inputList[i].style.backgroundColor = '#ededed';
            }else{
                inputList[i].style.backgroundColor = 'white';
            }
        }
    }
});

function focusToUserField(){
    document.getElementsByName('username')[0].focus();
}
focusToUserField();