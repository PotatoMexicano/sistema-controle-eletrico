# Sistema de controle elétrico

O sistema funcionará da seguinte maneira.

Haverá 2 inputs, um para voltagem e outro para Ampere

O sistema principal ficará encarregado de ajustar conforme a necessidade
do usuário a amperagem e a voltagem.

Será aplicado os modelos matemáticos para calcular os resultados das alterações
de amperagem e na voltagem, visto que ambas medidas estão intercaladas.


[ x ] No final do sistema, haverá um motor que gira uma hélice, mostrando o RPM do motor no momento.

A formula matemática escolhida foi
$$N = (60 * P) / (2π * T)$$

* N é a velocidade em RPM
* T é o torque em Newton-metro (Nm)
    * Motores de caminhão geralmente são acima de 1000 Nm
    
* π é a constante matemática Pi (aproximadamente 3,14)
* 60 é o número de segundos em um minuto.
* P é a potência em watts 
    
    $$ V * I * cos(θ)$$

    * V é a tensão elétrica em volts (V);
    * I é a corrente elétrica em amperes (A);
    * cos(θ) é o fator de potência (adimensional), que representa a eficiência do uso da energia elétrica. Em geral, o fator de potência varia de 0 a 1, sendo que valores mais próximos de 1 indicam um uso mais eficiente da energia.