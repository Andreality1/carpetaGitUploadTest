
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

#include <iostream>

char buf[4096]; // never know how much is needed

int main(int argc , char** argv) {

  if (argc > 1) {
    std::cout  << "CWD: " << cwd(buf, sizeof buf) << std::endl;

    // Change working directory and test for success
    if (0 == cd(argv[1])) {
      std::cout << "CWD changed to: " << cwd(buf, sizeof buf) << std::endl;
    }
  } else {
    std::cout << "No directory provided" << std::endl;
  }

  return 0;
}