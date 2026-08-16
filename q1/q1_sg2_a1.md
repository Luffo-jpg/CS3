# **Computational Thinking Exercise: "Smart Vending Machine"**
 **Section:** *9-Arayat*    **Score:** *-*

 **C# / Name**: *#16/Veniegas , #17/Yumul, #18/Cabanayan*     **Date:** *August 13, 2026*


## ***Scenario:***
### Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

- Sometimes the machine does not give the correct change.
- Items run out, but the machine doesn’t notify anyone.
- Students press the wrong buttons and get the wrong item.
- The machine is slow when multiple students use it in succession.

### Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

## **Step 1:** Identify the Big Problem
*Main Problem:* The machine is not able to correctly or efficiently process transaction, leading to errors regarding change, inventory, item selection, and speed.

## Step 2: Identify three to four Sub-Problems
### *Please list possible sub-problems:*

1. Incorrect change calculation and dispensing
2. Lack of monitoring inventory and notifications
3. Incorrect item selection
4. Inefficient/slow when used for multiple transactions over a short period of time

## **Step 3:** Define Computational Thinking Approaches
For each sub-problem, apply CT skills:
1. Incorrect change calculation and dispensing - Algorithm Design (To fix this issue, we can create an accurate and precise algorithm that compares the paid amount and the price of the item, calculate the difference of the two values, and dispense the correct amount of change)
2. Lack of monitoring inventory and notifications - Pattern Recognition (We can fix code to make it so that it can effectively monitor the how much of each item is left and recognize patterns such as the inventory of a certain item hitting a baseline, which will then trigger a notification indicating low stock.)
3. Incorrect item selection - Abstraction (Hide complex details and focus only on necessary information which includes the item name and code, quantity being bought, price of the item.)
4. Inefficient/slow when used for multiple transactions over a short period of time - Decomposition (Break the process into smaller parts. For example, the vending machine's process can be broken down into selection of item, payment, checking of inventory, and dispensing.)

## **Step 4:** Draw a flowchart or write a pseudocode for the identified sub-problem
Print item names and prices

INPUT selectedd item

IF selected item is available THEN
  Print item price
  INPUT amount of money inserted

  IF money inserted >= item price THEN
     Calculate change
     Dispense item
     Dispense change
     Update inventory
  ELSE
     Print "Insufficient payment"
     Return money
  END IF

ELSE 
  Print "Item is out of stock"
END IF

END

!(773866635_1852464615924382_7690824962565685196_n)
