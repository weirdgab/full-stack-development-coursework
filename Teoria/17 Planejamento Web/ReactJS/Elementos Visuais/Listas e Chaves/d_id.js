// Na maioria das vezes, utilizamos um ID do objeto. Caso não tenhamos um ID estável para isso, podemos usar
// o índice gerado na listagem. Mas use-o como último recurso!

const listaElementos = elementos.map((e, index) => <li key={index}>{e}</li>);
