async function registration(){
    var form = document.getElementById("regform");
    var email =  form.elements[0].value;
    var password = form.elements[2].value;
    const params = {
    "inputemail": email,
    "inputpassword": password,
    };
    console.log(email)
    console.log(password)
    /* const options = {
        method: 'POST',
        headers:{'content-type': 'application/json'},
        body: JSON.stringify(params)
    };
    fetch('http://127.0.0.1:5000/register', options)
        .then(response => response.json())
        .then(response =>{
        var regret= (response['answer']);
        if(regret  == 'Registration successful'){
            window.alert("Registration successful");
            myModal.hide();
        }else{
            window.alert(response['answer'])
        }
    }); */
};
