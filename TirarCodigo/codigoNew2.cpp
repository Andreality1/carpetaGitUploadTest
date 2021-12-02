#include <iostream>
#include <string>   
#include <windows.h>

#include <winbase.h>
using namespace std;

std::string getDir()
{
    char buff[MAX_PATH];
    int n = GetCurrentDirectoryA(MAX_PATH, buff);
    if (n)
        return buff;
    cout << "get directory failed\n";
    return "";
}

int main()
{
    cout << "Curent dir: " <<  getDir() << '\n';   
    
    if (SetCurrentDirectoryA("d:\\code\\"))
        cout << "Directory change ok\n";
    else
        cout << "Directory change failed\n";

    cout << "Curent dir: " <<  getDir() << '\n';   
    cout << system("dir") << std::endl;

    std::string variable = system("git log -n 1" )
       
}