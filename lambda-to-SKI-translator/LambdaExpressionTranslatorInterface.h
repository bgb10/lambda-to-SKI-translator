#ifndef LAMBDAEXPRESSIONTRANSLATORINTERFACE_H
#define LAMBDAEXPRESSIONTRANSLATORINTERFACE_H

#include "LambdaExpressionTranslator.h"

using namespace std;

class LambdaExpressionTranslatorInterface
{
private:

public:
	LambdaExpressionTranslatorInterface(LambdaExpressionTranslator&);
	void GetInput();
};

#endif