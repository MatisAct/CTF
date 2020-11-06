#include

using namespace std;

const int inputSize=10;

string inputString();

void copyStrs(string, char[] );

void subStrs(char[],char[]);

void getStrs(int,int,char[],char[]);

int main()

{

char strs[inputSize];

char sub[inputSize];

string s1 = inputString();

copyStrs(s1,strs);

subStrs(strs,sub);

cout << "sub string: " << sub << endl;

return 0;

}

string inputString()

{

cout << "Type a string: ";

string s;

getline(cin,s);

return s;

}

void copyStrs(string s, char strs[])

{

int i=0;
