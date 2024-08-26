# Calculadora de Área de Terreno
Este projeto é uma aplicação simples em Python que permite aos usuários calcular a área de um terreno a partir de uma imagem vista de cima, como uma captura de tela do Google Maps. O usuário pode marcar pontos na imagem para definir o perímetro do terreno, e a aplicação calcula a área aproximada em pixels².

## Funcionalidades
* Carregamento de Imagens:  Selecione e carrege uma imagem de seu computador.
    
* Marcação de Pontos: Pode clicar na imagem para marcar os vértices do terreno.
    
* Cálculo de Área: A área do terreno é calculada automaticamente à medida que os pontos são marcados.
    
* Exibição da Área: A área calculada é exibida no console em pixels².

## Tecnologias Utilizadas
* Python 3.x
* Tkinter: Para a interface gráfica.
* Pillow: Para manipulação e exibição de imagens.
* NumPy: Para cálculos matemáticos (cálculo da área).

## Requisitos
Certifique-se de que a seguinte bibliotecas esteja instalada no seu ambiente:

```
pip install pillow numpy
```