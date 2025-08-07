document.getElementById('formRegister').addEventListener('submit', register);
function register(event){
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    event.preventDefault();

    fetch('http://127.0.0.1:8000/create_user/?username='+username+'&password='+password, {
        method: 'POST'
    })
    .then(response => {
        if(response.ok){
            window.location.href="log-in.html";
        } else{
            alert('Error, an user has this username');
        }
    })
}