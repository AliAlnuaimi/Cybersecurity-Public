using Microsoft.Win32.TaskScheduler;

class Program
{
    static void CreateScheduledTask(string pDescription, int pDaysInterval, string pActionPath, string pActionArguments, string pTaskName)
    {
        // Create a new task service
        using (TaskService taskService = new TaskService())
        {
            // Create a new task definition
            TaskDefinition taskDefinition = taskService.NewTask();

            // Set the task properties
            taskDefinition.RegistrationInfo.Description = pDescription;
            
            // Create a trigger for the task (e.g., daily trigger)
            DailyTrigger dailyTrigger = new DailyTrigger();
            dailyTrigger.DaysInterval = pDaysInterval;
            taskDefinition.Triggers.Add(dailyTrigger);

            // Create an action (e.g., run a program)
            taskDefinition.Actions.Add(new ExecAction(pActionPath, pActionArguments, null));

            // Register the task in the root folder
            taskService.RootFolder.RegisterTaskDefinition(pTaskName, taskDefinition);
        }
    }
}
