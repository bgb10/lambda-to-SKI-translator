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

Regular expression을 이용해 정규화된 식에서 문자열을 뽑아서 definition을 저장한다.

## Currying Lambda expression

원래 Lambda expression에서 App에 따라 queue에 괄호 안의 token들을 push한다.

이후 pop하면서 Curried Lambda expression에 하나씩 작성하다보면 currying을 구현할 수 있다.

## Lambda Expression To SKI

문자열 내에서 6가지 rule에 해당하는 token을 검색해서 해당 token과 일치하면 rule에 따라 token을 삭제, transition rule이 적용된 token을 삽입한다.

이 방법을 계속 적용해서 token이 검색되지 않을 때까지 반복한다.

최종적으로 나온 token은 SKI 형태이다.
--!>