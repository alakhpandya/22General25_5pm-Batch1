let addTaskBtn = document.getElementById('add-task');
let taskInput = document.getElementById('task-input');
let taskContainer = document.querySelector('.task-container');
let taskInputValue, task, cnt = 0, hr, newTask;


addTaskBtn.addEventListener('click', () => {
    taskInputValue = taskInput.value;
    if (taskInputValue != ""){
        cnt++;
        taskInput.value = "";
        task = document.createElement('div');
        task.setAttribute('class', 'task');
        task.innerHTML = `<p class="task-text">${taskInputValue}</p>
        <div class="task-options">
            <i class="fa-solid fa-edit task-icon edit-icon"></i>
            <i class="fa-solid fa-check task-icon check-icon"></i>
            <i class="fa-solid fa-trash task-icon trash-icon"></i>
        </div>`;
        if (cnt > 1){
            hr = document.createElement('hr');
            hr.setAttribute('class', 'task-seperator');
            taskContainer.appendChild(hr);
        }
        taskContainer.appendChild(task);
        if (cnt == 1){
            taskContainer.classList.add('show-task-container');
        }
    }
})

window.addEventListener('click', (e) => {
    target = e.target;
    if (target.classList.contains('trash-icon')){
        if (target.parentElement.parentElement.previousElementSibling != null){
            target.parentElement.parentElement.previousElementSibling.remove();
        }
        else if (target.parentElement.parentElement.nextElementSibling != null){
            target.parentElement.parentElement.nextElementSibling.remove();
        }
        target.parentElement.parentElement.remove();
        cnt--;
        if (cnt == 0){
            taskContainer.classList.remove('show-task-container');
        }
    }

    if (target.classList.contains('check-icon')){
        target.parentElement.previousElementSibling.style.textDecoration = 'line-through';
    }

    if (target.classList.contains('edit-icon')){
        newTask = prompt("Enter new task:");
        if (newTask != ""){
            target.parentElement.previousElementSibling.innerText = newTask;
            target.parentElement.previousElementSibling.style.textDecoration = 'none';
        }
    }
})