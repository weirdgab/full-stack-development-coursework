import { useRouter } from 'next/router';

const produtos = [
  { id: 1, nome: 'Livro de Matematica' },
  { id: 2, nome: 'Livro de NextJS' },
  { id: 3, nome: 'Computador' },
  { id: 4, nome: 'Notebook' },
  { id: 5, nome: 'Caixas de Som' },
];

export default function Produto() {
  const router = useRouter();
  const { id } = router.query;

  const produto = produtos.find((p) => p.id === Number(id));

  return <h1>{produto?.nome}</h1>;
}