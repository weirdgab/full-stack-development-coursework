const produtos = [
    { id: 1, nome: 'Livro de Matematica', preco: 20.00 },
    { id: 2, nome: 'Livro de NextJS', preco: 100.00 },
    { id: 3, nome: 'Computador', preco: 3000.00 },
    { id: 4, nome: 'Notebook', preco: 5000.00 },
    { id: 5, nome: 'Caixas de Som', preco: 450.00 },
];

export default function handler(req, res) {
    res.status(200).json(produtos);
}