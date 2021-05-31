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


function createPost(){
          var form = document.getElementById("createpostform");
          var posttitel =  form.elements[0].value;
          var postcontent = form.elements[1].value;
          const csrfToken = document.getElementsByName('csrf_token')[0].value;
          const params = {
            "posttitel": posttitel,
            "postcontent": postcontent,
             credentials: 'same-orgin'
          }
          const options = {
            method: 'POST',
            headers:{'content-type': 'application/json', 'X-CSRF-TOKEN': csrfToken},
            body: JSON.stringify(params)
            
          };
          fetch('http://127.0.0.1:5000/createpost', options)
            .then(response => response.json())
            .then(response =>{
              
        });       
}


function checkifloggedin(){
    var pathname = window.location.pathname;
      if(pathname == '/register' || pathname == '/login'){
      window.location.href = "http://127.0.0.1:5000/home";
    }  
}

