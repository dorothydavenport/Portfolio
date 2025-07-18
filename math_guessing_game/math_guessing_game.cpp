//Dorothy Davenport
//4/18/2024
//
//
//This program is intended to generate a math problem in the form of "4 + 2"
//And then take input from the user for the solution. The player gets 3 attempts per problem.
//If the player does not guess correctly after three attempts, they lose a token. 
//The player starts with 5 tokens. Once all 5 tokens are lost the game is over.
//The player can also exit the game in between each problem if they choose.  

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	
   //Declare variables

   //tokens variable will be used to assign the starting 5 tokens to each player
   int tokens = 5;
   
   //attempts variable will be used to assign the starting 1 attempts to each player 
   //I intend attempts to start at 1 and then increment with each subsequent attempt up to 3 
   int attempts = 1;
  
   //option_to_continue variable will be used within a loop so that the player can choose
   //when they want to exit the game. This option will be either C for continue or E for exit.
   //If they continue, the game moves on. If they exit, they exit the loop controlling the 
   //game play and go straight to end game. 
   char option_to_continue = 'C';
  
   //seed random number generated to be used in following variables
   srand(time(0)); 

   //first random number to be generated for the program. The variable equals the random number modulo 21
   //because we want the random numbers to be between 0 and 20. 
   int random_number_1;

   //second random number to be generated for the program. The variable equals the random number modulo 21
   //because we want the random numbers to be between 0 and 20. 
   int random_number_2;

   //random operation to be used in the program. The values we want are +, - or *. I plan on getting a 
   //random number between 0, 1 and 2 so I'll use modulo 3. Then I'll use conditionals to replace those numbers with one of the 
   //planned operators.  
   char random_operation;

   //solution that is accurate based on the given problem 
   int actual_solution;

   //solution entered by player
   int entered_solution;

   
   //Greet the user and establish program rules	

   cout << "Welcome to the math skills challenge! The rules of the game are as follows." << endl << endl;
   cout	<< "When you’re ready to continue, you will be presented with a problem that needs "
	<< "solving. You’ll start the game with 5 tokens and you’ll get three attempts at each problem. " << endl << endl;
   cout	<< "After entering in the solution, if you are correct, hurray! You’ll get to "
	<< "continue on to the next problem. If you are incorrect, darn! You’ll get two more "
	<< "tries to guess the correct solution. If you don’t get it after three attempts, then you "
	<< "lose a token and move on to the next problem. The game ends when you run out of tokens." << endl << endl;
   cout << "Here is an example of the type of problem that you'll be presented with: " << endl << endl;
   cout	<< "Solve the problem: 12 * 6" << endl;
   cout	<< "Solution: 72" << endl << endl;
   
   //Transition from startup greeting and example to game play

   cout << "Is your brain warmed up? Would you like to continue or exit the game?" << endl;
   
   // Master do while loop that controls game repeat. The loop will continue as long as the player
   // enters C for continue. 
   
   do 
   {	  
   
      //Do while loop that controls input validation. The loop will repeat if the player does not enter a
      //C or an E. 
   
      do
      {
         cout << "Enter C for continue or E for exit then press Enter." << endl;
         cin >> option_to_continue;
 
         // First conditional for first do/while loop relating to menu option Continue

         if (toupper(option_to_continue) == 'C')
         {
            cout << endl << "You have chosen to continue." << endl; 
	    random_number_1 = rand() % 21;
	    random_number_2 = rand() % 21;
	    random_operation = rand() % 3;
            do
	    {
	       cout << "Here is the problem you'll need to solve: " << endl;
               if (random_operation == 0)
               {
                  cout << random_number_1 << " + " << random_number_2 << endl << endl;
                  actual_solution = random_number_1 + random_number_2;
               }
               else if (random_operation == 1)
               {
                  cout << random_number_1 << " - " << random_number_2 << endl << endl;
                  actual_solution = random_number_1 - random_number_2;
               }
               else
               {
                  cout << random_number_1 << " * " << random_number_2 << endl << endl;
                  actual_solution = random_number_1 * random_number_2;
               }
  
              // Do while loop that controls input validation on the entered solution. The loop will repeat if the 
              // player has a problem that contains addition + or multiplication * and they enter a negative number

	       do
               { 
                  cout << "Enter your solution here as an integer (no decimals): " << endl;
                  cin >> entered_solution;
   
                  // First do/while condition based on solution being accurate 

	          if (entered_solution == actual_solution)
	          {
	             cout << endl << "That's correct! Great job." << endl;
	             cout << "You get a new problem to complete." << endl << endl;
	             attempts == 1;
	          }
            
	          // Second do/while condition based on solution being negative   
	    
	          else if ((random_operation == 0 || random_operation == 2) && entered_solution < 0)
	             cout << "The solution should not be negative, please try again." << endl;
          
	          // Third do/while condition based on solution being inccurate 
	  
	          else 
	          {
	              cout << endl << "Darn! That's not the right answer." << endl;
	              cout << "This was attempt number " << attempts << endl << endl;
	              if (attempts == 1 || attempts == 2)
	              {
	                 cout << "You still have more attempts left! You can try again." << endl << endl;
	                 ++attempts;
	              }
		      else if (attempts == 3  && tokens > 1)
	              {
	                 cout << "Oh no! You don't have any more attempts left." << endl;
	                 cout << "You will lose a token." << endl << endl;
	                 --tokens;
	                 if (tokens > 1)
			    cout << "You have " << tokens << " tokens remaining." << endl;
			 else
			    cout << "You have " << tokens << " token remaining." << endl;
	                 cout << "On to the next problem!" << endl << endl;
		         attempts = 1;
                      }
		      else 
		      {
	                 cout << "Oh no! That was your last attempt and you're out of tokens." << endl;
		         cout << "That's game over I'm afraid." << endl;
	                 ++attempts;
			 option_to_continue = 'E';
		      }
	          }
	       }
	       while ((random_operation == 0 || random_operation == 2) && entered_solution < 0); 
            }
	    while ((attempts == 2 || attempts == 3) && entered_solution != actual_solution); 
       }  //This bracket ends the if(option_to_continue == 'C') conditional 
   
          // Second conditional for first do/while loop relating to menu option Exit
      
          else if (toupper(option_to_continue) == 'E')
          cout << "You have chosen to exit." << endl;
       
          // Third conditional for first do/while loop relating to menu option that is invalid
         
	  else 
          {
            cout << "That is not a valid option. Please re-enter your choice." << endl;
            option_to_continue == 'C';  
          }
      }
      while (toupper(option_to_continue) != 'C' && toupper(option_to_continue) != 'E');
   
   }
   while (toupper(option_to_continue) == 'C');  
   cout << "Thank you for playing! Come back again." << endl; 

   return 0;
   
}
