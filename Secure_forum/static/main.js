async function registration(){
    var form = document.getElementById("regform");
    var email = form.elements["InputEmail"].value;
    var password = form.elements[2].value; 
    var crsft = form.elements['csrf_token'].value
    const params = {
    "inputemail": email,
    "inputpassword": password,
    };

    const options = {
        method: 'POST',
        headers:{'content-type': 'application/json', 'X-CSRFToken' : crsft},
        body: JSON.stringify(params),
        referrerPolicy: 'same-origin',
    };
    fetch('http://127.0.0.1:5000/register', options)
        .then({
    });
};