about AI Control & monitoring:
One stronger model monitored by a smaller to find bad intentions
1st issue:
  the model bypasses the monitor : builds actions that look innocent based on the monitor's scope but are harmful.
2nd issue:
  the model corrupts the monitor : since the monitor reads the model production, it can insert harmful instructions to manipulate the monitor.

Two identical models monitor each other : collusion :
to avoid models helping each other, add a reward for when one of the models catches the mistake of the other : debate.
Limits : a reward works in training but collusion happens when the model's real goal is different from the reward


How to verify, externally, that two models are really competing instead of faking ? 


add a small external model that reads the output of each model and detects if they produce a result ?

Research directions : 
reducing opportunities for actor monitor collusion or jailbreaks, for example by editing, paraphrasing the actor's output before showing it to the monitor
training better monitors, by generating for  bu generating synthetic data that realistcally captures sophisticated, malicious behaviour
Developing monitoring schemes that work even when the actor has access to additional affordances, such as memory of previous episodes or the ability to pass messages between instances.
