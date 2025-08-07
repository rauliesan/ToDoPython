let user = localStorage.getItem('user');
let message = localStorage.getItem('message');

function toDo() {
    alert(user); /* Quitar en el futuro */

    fetch('http://127.0.0.1:8000/get_toDo_tasks/?user=' + user)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error with to-do tasks')
            }
            return response.json();
        })
        .then(data => {
            let taskContainer = document.getElementById('tasks');
            let tasks = "";
            data.forEach(task => {
                tasks += `
                <div class="card" data-task-id="${task.id}">
                    <div class="card-details">
                        <p class="text-title">${task.name}</p>
                        <p class="text-body">${task.text}</p>
                    </div>
                    <div class="card-actions">
                        <button class="delete" onclick="deleteTask(${task.id})"> 
                            <svg viewBox="0 0 448 512" class="svgIcon">
                                <path
                                    d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z">
                                </path>
                            </svg>
                        </button>
                        <button class="card-button done" onclick="doneTask(${task.id})">Done</button>
                    </div>
                </div>
            `;
            })
            taskContainer.innerHTML = tasks;
        })
}

function done(){
    alert(user);

    fetch('http://127.0.0.1:8000/get_done_tasks/?user='+user)
    .then(response => {
        if(!response.ok){
            throw new Error('Error with done tasks');
        }
        return response.json();
    })

    .then(data => {
        let taskContainer = document.getElementById('tasks');
        let tasks = "";
        data.forEach(task => {
            tasks += `
                <div class="card" data-task-id="${task.id}">
                    <div class="card-details">
                        <p class="text-title">${task.name}</p>
                        <p class="text-body">${task.text}</p>
                    </div>
                    <div class="card-actions">
                        <button class="delete" onclick="deleteTask(${task.id})"> 
                            <svg viewBox="0 0 448 512" class="svgIcon">
                                <path
                                    d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z">
                                </path>
                            </svg>
                        </button>
                        <button class="card-button done" onclick="toDoTask(${task.id})">To Do</button>
                    </div>
                </div>
            `;
        })
        taskContainer.innerHTML = tasks;
    })

}

function doneTask(taskId){
    alert('Done task ' + taskId);
}

function toDoTask(taskId){
    alert('To do task ' + taskId);
}

function deleteTask(taskId){
    alert('Delete task ' + taskId);
}

function logOut() {
    user = undefined;
    window.location.href = "index.html";
}