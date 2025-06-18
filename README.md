# Ophelia Finanacial Planner
by Xofox(xy)
## What is this?
The main idea is to create a framework to generate your own financial planner to better predict the long term health 
of your finances by breaking everything down into manageable and more predictable chunks.


## What is this not?
This is not financial advice in any way. I am not a registered financial professional. 
Any silly decisions I make are mine and any silly decisions you make are yours.

# How does/will it work?
The idea is simple. 
Every aspect of your life can be either represented by a model or discretized.
Every part of your life that needs individual modelling will be an account.
Accounts can all be combined into "Super Accounts" which aggregate the data from each.
### So what is an account?
Each account can be modeled over time to show how it is projected to change over time. 
An account is initialized with a name, a starting balance, an income function, a cost function, and an appreciation rate.
Any of these can reference other accounts if they must, but in order to do that they need to share at least one super account.


### What is the purpose of super accounts?
Super accounts serve as a way to group your accounts. Say you have an account for your children's food, 
your children's education, and your children's hobbies. You may want to project the total cost of your children.
You can include all 3 of those accounts into a super account and then predict the total cost that they will incur
in the next few years.

### So now I understand what the parts do, what do I use it for?
Now you can install it as a package and use it on its own for some basic financial planning, 
or you can build it into your own data driven financial planning.

## So where is this going?
Right now it's in early early development. While the account system works, super accounts aren't yet functional. 
So, that's the next step. After that's done, I want to add more robust statistics and prediction.
I would like to make every account tree initializable through a formatted plaintext document. 
Once that's done it would be helpful if you could easily query an LLM for some simple feedback on how to make your account tree more robust