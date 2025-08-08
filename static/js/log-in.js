document.getElementById('formLogIn').addEventListener('submit', logIn);
function logIn(event){
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    event.preventDefault();

    fetch('https://todopython-b750.onrender.com/log_in/?username='+username+'&password='+password)
    .then(response => {
        if(!response.ok){
            alert('Error, this password or username is incorrect');
            throw new Error('Error, this password or username is incorrect');
        }
        return response.json();
    })
    .then(user => {
        localStorage.setItem('user', user.id);
        let message = "<p>Welcome another time</p>";
        localStorage.setItem('message', message);
        window.location.href="to-do.html";
    })
}