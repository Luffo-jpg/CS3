# Code Quality Assessment Worksheet

**Section:** *9-Arayat* **Score:** *-*

 **C# / Name**: *#16/Veniegas , #17/Yumul, #18/Cabanayan*     **Date:** *August 16, 2026*


## ***Instructions:***
### **The Problem: Finding the highest (Maximum) number from a given list of numbers.**

PseudoCode 1
```
Algorithm FindMax1(numbers)
   max ← numbers[0]
   For i from 1 to length(numbers)-1
      If numbers[i] > max Then
         max ← numbers[i]
      EndIf
   EndFor
   Return max
EndAlgorithm
```

PseudoCode 2
```
Algorithm FindMax2(numbers)
   For i from 0 to length(numbers)-1bigger ← true
      For j from 0 to length(numbers)-1
         If numbers[j] > numbers[i] Then
            bigger ← false
         EndIf
      EndFor
      If bigger = true Then
         Return numbers[i]
      EndIf
   EndFor
EndAlgorithm
```

## Questions with Checklists
### **1. Efficiency**
**Which algorithm is faster when the list of numbers is very large? Why?**

- In terms of the usage of a large list of numbers, the 1st pseudocode is faster as it makes use of a single loop, so it only examines each number once. On the other hand, pseudocode 2 utilizes nested loops which compares each element to every other element, making the steps grow as the list gets longer.


***Checklist (✓)***

PseudoCode 1
- [One Loop] Does the algorithm use one loop or two nested loops?
- [No] Does the algorithm repeat work unnecessarily?
- [Pseudocode 1] Which algorithm finishes in fewer steps?

PseudoCode 2
- [One Loop] Does the algorithm use one loop or two nested loops?
- [No] Does the algorithm repeat work unnecessarily?
- [Pseudocode 1] Which algorithm finishes in fewer steps?

### **2. Readability**
**Which algorithm is easier to understand at first glance? What makes it clearer?**

- Pseudocode 1 is easier to understand as it uses clearer variable names, is more straightforward, and has far less lines of code compared to the 2nd pseudocode.


***Checklist (✓)***

PseudoCode 1
- [✓] Are variable names meaningful (e.g., max vs. bigger)?
- [Simple] Is the logic simple or complicated?
- [✓] Which algorithm finishes in fewer steps?] Are there fewer lines of code?

PseudoCode 2
- [✘] Are variable names meaningful (e.g., max vs. bigger)?
- [Complicated] Is the logic simple or complicated?
- [✘] Are there fewer lines of code?

### **3. Maintainability**
**If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?**

- If we were to add a new feature, pseudocode 1 would be easier to update with its structure, where you can easily track a second variable inside a loop. Meanwhile, updating the other pseudocode would be more prone to errors because you have to modify the nested loops to update it.


***Checklist (✓)***

PseudoCode 1
- [✓] Is the structure straightforward?
- [✘] Would adding new steps break the code easily?
- [✓] Is there less chance of errors when updating?

PseudoCode 2
- [✘] Is the structure straightforward?
- [✓] Would adding new steps break the code easily?
- [✘] Is there less chance of errors when updating?

### **4. Testability**
**Which algorithm is easier to test with different inputs? Why?**

- Pseudocode 1 is easier to test due to its flow being linear and edge cases can be tested and verified more straightforwardly. Debugging is also easier in this pseudocode because of its single-path execution.


***Checklist (✓)***

PseudoCode 1
- [✓] Can you test with small lists easily?
- [✓] Does the algorithm have fewer conditions to check?
- [✓] Is the output predictable and clear?

PseudoCode 2
- [✘] Can you test with small lists easily?
- [✘] Does the algorithm have fewer conditions to check?
- [✘] Is the output predictable and clear?


### **5. Security**
**Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?**

- For the algorithm to avoid errors and misuse, it must validate that the list of inputs is not null or empty. Aside from that, it should also have a type and range validation to ensure that all inputs are valid numbers and not string types or special characters.


***Checklist (✓)***

PseudoCode 1
- [✘] Does the algorithm check if the list is empty?
- [✘] Does it handle invalid inputs (like letters instead of numbers)?
- [✘] Does it avoid crashing when inputs are unusual?

PseudoCode 2
- [✘] Does the algorithm check if the list is empty?
- [✘] Does it handle invalid inputs (like letters instead of numbers)?
- [✘] Does it avoid crashing when inputs are unusual?

### **6. Final Answer**
**Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer**

- Based on our answers, the 1st algorithm is definitely better in solving the problem because of its faster run time, cleaner and simpler structure, efficiency in testing, and it being less prone to errors when being updated/modified.
