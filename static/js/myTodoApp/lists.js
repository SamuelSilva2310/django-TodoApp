const progress_task = document.querySelectorAll(".progress-done");


//ADD FUNCTIONALITY
// EACH CARD (TO DO LIST) PROGRESS BAR DISPAYS THE RIGHT AMMOUNT

//get percentage (tasks done/tasks total)
var progress = [5,60];
progress_task.forEach((item,index)=>{
    item.style.width = progress[index] + "%";
})
