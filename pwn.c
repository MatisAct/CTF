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

for (i = 0; i < s.length(); i++)

strs[i] = s.at(i);

strs[i] ='\0';

}

void subStrs(char strs[],char newStrs[])

{

int start;

int end;

cout << "Starting point: ";

cin >> start;

cout << "Ending point: ";

cin >> end;

getStrs(start,end,strs,newStrs);

}

void getStrs(int start,int end,char strs[],char newStrs[])

{

int len = end-start+1;

int i=0;

for (i=0; i < len - 1; i++)

newStrs[i] = strs[start + i];

newStrs[i] = '\0';

}
