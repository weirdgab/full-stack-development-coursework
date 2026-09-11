import type { NextApiRequest, NextApiResponse } from 'next';

const produtos = [
	{ id: 1, nome: 'Livro de Matemática', preco: 20.0 },
	{ id: 2, nome: 'Livro de NextJS', preco: 100.0 },
	{ id: 3, nome: 'Computador', preco: 3000.0 },
	{ id: 4, nome: 'Notebook', preco: 5000.0 },
	{ id: 5, nome: 'Caixas de Som', preco: 450.0 },
];

export default function handler(req: NextApiRequest, res: NextApiResponse) {
	res.status(200).json(produtos);
}
