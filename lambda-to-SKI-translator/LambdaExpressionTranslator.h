#ifndef LAMDAEXPRESSIONTRANSLATOR_H
#define LAMDAEXPRESSIONTRANSLATOR_H

#include <vector>
#include <string>

using namespace std;

class LambdaExpressionTranslator
{
private:
	vector<LambdaExpression> m_lambda_expression_list;
public:
	LambdaExpressionTranslator();
	string ToSKIExpression(LambdaExpression);
	string ToOriginalLambdaExpression(LambdaExpression);
};

#endif