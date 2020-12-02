#  Class LambdaExpressionTranslator

## Description

Manages all the `LambdaExpression` objects, and translates `LambdaExpression` objects to another expression (e.g. original lambda(denoted \) Expression, SKI Expression)

Also, enters user inputs to perform upper content.

## member variables

### vector<LambdaExpression> m_lambda_expression_list

## member functions

### string ToSKIExpression(LambdaExpression)

### string ToOriginalLambdaExpression(LambdaExpression)

### getUserInput()


# Class LambdaExpression

## Description

Definition of Lambda Expression.

## member variables

### name

## member functions

### LambdaExpression()

### LambdaExpression(string)

### Print()

### Concatenate()

### GetName()

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