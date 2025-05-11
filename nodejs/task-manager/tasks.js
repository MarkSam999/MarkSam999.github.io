class Tasks{
    constructor(task){
        this.task = task;
    };

    addTask(task){
        task.push(list);
        JSON.stringify(list);
    };

    removeTask(){
        task.remove(list);
        console.log("Task '" + task + "' removed!")
        JSON.stringify(list);
    };

    listTasks(){
        for(task in list){
            console.log(task);
        }
    }
}