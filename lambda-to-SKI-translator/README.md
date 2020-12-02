# Class LambdaExpressionTranslatorInterface

## Description

Get user Input for the `LambdaExpressionTranslator`.

Show functional-language like interface. 

## member variables

## member functions

- LambdaExpressionTranslatorInterface(LambdaExpressionTranslator&)

- public void GetInput()

# Class LambdaExpressionTranslator

## Description

Manages all the `LambdaExpression` objects, and translates `LambdaExpression` objects to another expression (e.g. original lambda(denoted \) Expression, SKI Expression)

## member variables

- private vector<LambdaExpression> m_lambda_expression_list

## member functions

- LambdaExpressionTranslator()

- public string ToSKIExpression(LambdaExpression)

- public string ToOriginalLambdaExpression(LambdaExpression)

# Class LambdaExpression

## Description

Definition of Lambda Expression.

## member variables

- private string name

## member functions

- LambdaExpression()

- LambdaExpression(string)

- public void Print()

- public void Concatenate()

- public string GetName()

<!--
##  Lambda expression Definition

Regular expression�� �̿��� ����ȭ�� �Ŀ��� ���ڿ��� �̾Ƽ� definition�� �����Ѵ�.

## Currying Lambda expression

���� Lambda expression���� App�� ���� queue�� ��ȣ ���� token���� push�Ѵ�.

���� pop�ϸ鼭 Curried Lambda expression�� �ϳ��� �ۼ��ϴٺ��� currying�� ������ �� �ִ�.

## Lambda Expression To SKI

���ڿ� ������ 6���� rule�� �ش��ϴ� token�� �˻��ؼ� �ش� token�� ��ġ�ϸ� rule�� ���� token�� ����, transition rule�� ����� token�� �����Ѵ�.

�� ����� ��� �����ؼ� token�� �˻����� ���� ������ �ݺ��Ѵ�.

���������� ���� token�� SKI �����̴�.
--!>