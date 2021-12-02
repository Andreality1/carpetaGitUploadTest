

#define _WIN32_WINNT 0x500


#include <iostream>
#include <windows.h>

#ifdef _WIN32
#include <direct.h>
// MSDN recommends against using getcwd & chdir names
#define cwd _getcwd
#define cd _chdir
#else
#include "unistd.h"
#define cwd getcwd
#define cd chdir
#endif

using namespace std;


//vamos a tirar el concepto que nos permite detallar el conocimiento de nuestra realidad.

void print(std::string objeto){
    std::cout << objeto << std::endl;
}

void newLine(){
    std::cout << std::endl;
}

void newLineBy3(){
    for(int i = 0; i < 3; i++){
        std::cout << std::endl;
    }
}

void printSplash ()
{
     std::cout << "\n\n ___________________________\n";
     std::cout << "/                           \\\n";
     std::cout << "|  AUTO CLICKER             |\n";
     std::cout << "|  george wong              |\n";
     std::cout << "|  beta  v0.01              |\n";
     std::cout << "\\___________________________/\n";
}

void getMethod (int& method)
{
     // update (via pointer) what method to use (simple)
     std::cout << "0) Exit\n";
     std::cout << "1) Read cursor position\n";
     std::cout << "2) Right mouse click\n";
     std::cout << "3) Left mouse click\n";
     std::cout << "4) Move mouse to location\n\n";
     std::cout << "Enter the number of your selection: ";
     std::cin >> method;
}


void getMousePosition (int& xPos, int& yPos)
{
     // make a point and read into it, then update vars via pointers
     POINT cursorPos;
     GetCursorPos(&cursorPos);
     xPos = cursorPos.x;
     yPos = cursorPos.y;
}

void mouseRightClick ()
{
     INPUT Input = {0};
     
     // right down
     Input.type = INPUT_MOUSE;
     Input.mi.dwFlags = MOUSEEVENTF_RIGHTDOWN;
     ::SendInput(1,&Input,sizeof(INPUT));
     
     // right up
     ::ZeroMemory(&Input,sizeof(INPUT));
     Input.type = INPUT_MOUSE;
     Input.mi.dwFlags = MOUSEEVENTF_RIGHTUP;
     ::SendInput(1,&Input,sizeof(INPUT));
}

void mouseLeftClick ()
{
     INPUT Input = {0};
     
     // left down
     Input.type = INPUT_MOUSE;
     Input.mi.dwFlags = MOUSEEVENTF_LEFTDOWN;
     ::SendInput(1,&Input,sizeof(INPUT));
     
     // left up
     ::ZeroMemory(&Input,sizeof(INPUT));
     Input.type = INPUT_MOUSE;
     Input.mi.dwFlags = MOUSEEVENTF_LEFTUP;
     ::SendInput(1,&Input,sizeof(INPUT));
}

void mouseMoveTo (int toX, int toY)
{
     // find out info about the screen so that we know how to properly go
     // to pixels
     double screenRes_width = ::GetSystemMetrics( SM_CXSCREEN )-1;
     double screenRes_height = ::GetSystemMetrics( SM_CYSCREEN )-1;
     // modify for the 65535 (as float) way we talk to the screen...
     double dx = toX*(65535.0f / screenRes_width);
     double dy = toY*(65535.0f / screenRes_height);
     
     // movement stuff
     INPUT Input = {0};
     Input.type = INPUT_MOUSE;
     Input.mi.dwFlags = MOUSEEVENTF_MOVE|MOUSEEVENTF_ABSOLUTE;
     Input.mi.dx = LONG(dx);
     Input.mi.dy = LONG(dy);
     ::SendInput(1,&Input,sizeof(INPUT));
}

int main() {



    int mil = 1000;

    int variable = 10;
    int numero [variable];
    for (int i = 0; i < 10; i++){
        numero[i] = i;
        std::cout << numero[i]  << std::endl;
    }

    ///que concepto nosotros vamos a creare como el movimiento de nuestra realidad produce el cambio que yo quiero ver, el comportamiento que yo quiero sintetizar.
    

     
    SetConsoleTitle( "Auto Clicker v0.01" );
    
    // set up variables to be used
    int xPos, yPos; // position of pointer
    int methodNumber = 0; // what method to use
    int numOfClicks = 0; // number of clicks
    int sleepTime = 0; // sleep time in ms


    /* 
    start:
    
    printSplash();
    getMethod(methodNumber);
    
    if (methodNumber == 1)
    {
       std::cout << "Number of reads: ";
       std::cin >> numOfClicks;
       std::cout << "\nAmount of time to wait between reads (ms): ";
       std::cin >> sleepTime;
       std::cout << "Reading position in 3 seconds.\n";
       Sleep(1000);
       std::cout << "2..\n";
       Sleep(1000);
       std::cout << "1..\n\n";
       Sleep(1000);
       for(int x=0; x<numOfClicks; x++)
       {
               getMousePosition(xPos,yPos);
               std::cout << "(x,y)   :   (" << xPos << "," << yPos << ")\n";
               Sleep(sleepTime);
       }       
       goto start;
    }
    
    if (methodNumber == 2)
    {
       std::cout << "Clicking right mouse button.\n\nNumber of clicks: ";
       std::cin >> numOfClicks;
       std::cout << "\nTime to wait between clicks (ms): ";
       std::cin >> sleepTime;
       std::cout << "In 3 seconds...\n";
       Sleep(1000);
       std::cout << "2..\n";
       Sleep(1000);
       std::cout << "1..\n\n";
       Sleep(1000);
       for(int x=0; x<numOfClicks; x++)
       {
               mouseRightClick();
               Sleep(sleepTime);
       }
       goto start;
    }
    
    if (methodNumber == 3)
    {
       std::cout << "Clicking left mouse button.\n\nNumber of clicks: ";
       std::cin >> numOfClicks;
       std::cout << "\nTime to wait between clicks (ms): ";
       std::cin >> sleepTime;
       std::cout << "In 3 seconds...\n";
       Sleep(1000);
       std::cout << "2..\n";
       Sleep(1000);
       std::cout << "1..\n\n";
       Sleep(1000);
       for(int x=0; x<numOfClicks; x++)
       {
               mouseLeftClick();
               Sleep(sleepTime);
       }
       goto start;
    }
    
    if (methodNumber == 4)
    {
       std::cout << "Moving.\n\nX coordinate: ";
       std::cin >> xPos;
       std::cout << "\nY coordinate: ";
       std::cin >> yPos;
       std::cout << "\n\nMoving in 1 second...";
       Sleep(1000);
       mouseMoveTo(xPos,yPos);
       goto start;
    }
    
    
     */



    std::string str="We think in generalities, but we live in details.";
                                           // (quoting Alfred N. Whitehead)

    std::string str2 = str.substr (3,5);     // "think"

    std::size_t pos = str.find("live");      // position of "live" in str

    std::string str3 = str.substr (pos);     // get from "live" to the end

    print(str2);
    print(str3);

    newLine();
    int valor = 10;
    mil = valor;

    print(std::to_string(mil));


    std::cout << mil << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << std::endl;

    system("dir");
    system("d:");
    system("dir");
    ///somos los traductore del pensamiento que se quiere diseñar

    ///Vamos a tirar codigo en donde el concepto que nos permite evolucionar como mentalidad como podemos sintetizar mejores formas a usar en la realidad
    ///que contextos podemos analizar

    return 0;   
}
