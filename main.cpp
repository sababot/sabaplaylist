#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string command;

    while (command != "quit" || command != "q")
    {
        // read command
        getline(cin, command);
        
        // process command into words
        vector <string> words;
        string word;
        
        for (int i = 0; i < command.length(); i++)
        {
            if (i != command.length() - 1)
            {
                if (!isspace(command[i]))
                    word += command[i];

                else if (isspace(command[i]))
                {
                    words.push_back(word);
                    word = "";
                }
            }

            else
            {
                word += command[i];
                words.push_back(word);
                word = "";
            }
        }

        // export command
        if (words[0] == "export")
        {
            cout << words[1] << endl;
            //export_spotify(words[1]);
        }
    }
    
    return 0;
}
