import Link from 'next/link';

const produtos = [
  { id: 1, nome: 'Livro de Matematica' },
  { id: 2, nome: 'Livro de NextJS' },
  { id: 3, nome: 'Computador' },
  { id: 4, nome: 'Notebook' },
  { id: 5, nome: 'Caixas de Som' },
];

export default function Produtos() {
  return (
    <>
      <h1>Lista de Produtos</h1>
      {produtos.map((produto) => (
        <Link key={produto.id} href={`/produto/${produto.id}`}>
          <h2>{produto.nome}</h2>
        </Link>
      ))}
    </>
  );
}