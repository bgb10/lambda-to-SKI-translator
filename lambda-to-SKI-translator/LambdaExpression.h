#ifndef LAMDAEXPRESSION_H
#define LAMDAEXPRESSION_H

#include <string>

using namespace std;

class LambdaExpression
{
private:
	string name;

public:
	LambdaExpression();
	
	LambdaExpression(string expression);

	void Print();

	void Concatenate();

	string GetName();
};

#endif