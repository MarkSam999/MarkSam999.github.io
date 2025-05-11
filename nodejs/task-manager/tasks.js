class Tasks{
    constructor(task){
        this.task = task;
    };

    addTask(task){
        task.push(list);
        JSON.stringify(list);
        console.log("Task '" + task + "' added!")
    };

    removeTask(){
        task.remove(list);
        JSON.stringify(list);
        console.log("Task '" + task + "' removed!");
    };

    listTasks(){
        for(task in list){
            console.log(task);
        }
    }

    seatch(){
        console.log()
    }
}