const usernameField = document.querySelector(".username")
const usernameError = document.querySelector(".username-error")
const usernameSuccess = document.querySelector(".username-success")
const emailField = document.querySelector(".email")
const emailError = document.querySelector(".email-error")
const emailSuccess = document.querySelector(".email-success")
const submit = document.querySelector(".submit")



usernameField.addEventListener("keyup", (e)=>{
    const usernameval = e.target.value
    
    usernameError.style.display = "none"
    usernameField.classList.remove("error")

    submit.removeAttribute("disabled")    

    if(usernameval.length > 0){
        usernameSuccess.textContent = "Checking " + usernameval
        usernameSuccess.style.display = "block"
        fetch("/verify-username", {
            body: JSON.stringify({username: usernameval}),
            method: "POST"
        }).then(res=>res.json()).then(data=>{
            usernameSuccess.style.display = "none"
            if (data.username_error){
                usernameField.classList.add("error")
                usernameError.style.display = "block"
                usernameError.textContent = data.username_error
                submit.disabled = disabled
            }
        })
    }
})


emailField.addEventListener("keyup", (e)=>{
    const emailval = e.target.value
    
    emailError.style.display = "none"
    emailField.classList.remove("error")

    if(emailval.length > 0){
        emailSuccess.textContent = "Checking " + emailval
        emailSuccess.style.display = "block"
        fetch("/verify-email", {
            body: JSON.stringify({email: emailval}),
            method: "POST"
        }).then(res=>res.json()).then(data=>{
            emailSuccess.style.display = "none"
            if (data.email_error){
                emailField.classList.add("error")
                emailError.style.display = "block"
                emailError.textContent = data.email_error
            }
        })
    }
})