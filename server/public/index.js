function submitRegistration() {
    var form;
    form = document.getElementById("signin_loginForm");
    
    if (form.elements[2].value === "") {
        return false;
    } else {
        return true;
    }
}
    
function signup() {
    "use strict";
    var form;
    var formElements;
    var verifyPasswordField;
    
    form = document.getElementById("signin_loginForm");
    formElements = form.elements;
    verifyPasswordField = document.createElement("input");
    verifyPasswordField.setAttribute("class", "inputField");
    verifyPasswordField.setAttribute("type", "password");
    verifyPasswordField.setAttribute("name", "passwordVerify");
    verifyPasswordField.setAttribute("placeholder", "Verify Password");
    verifyPasswordField.setAttribute("required", null);
    form.insertBefore(verifyPasswordField, formElements[2]);
    
    
    formElements[3].removeEventListener("onclick", formElements[3].onclick);
    formElements[3].onclick = null;
    formElements[3].setAttribute("formaction", "http://54.86.187.108:3000/register");
    formElements[3].setAttribute("formmethod", "post");
    formElements[3].setAttribute("onsubmit", "return submitRegistration()");
    
        
    return false;
}

//add a change function to first password field
//ass pattern to second field