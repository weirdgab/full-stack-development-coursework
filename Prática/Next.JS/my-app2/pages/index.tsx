import React, { useEffect, useState } from 'react';

type Produto = {
	id: number;
	nome: string;
	preco: number;
};

const HomePage = () => {
	const [produtos, setProdutos] = useState<Produto[]>([]);
	useEffect(() => {
		const fetchData = async () => {
			const response = await fetch('/api/produtos');
			const data = await response.json();
			setProdutos(data);
		};
		fetchData();
	}, []);
	return (
		<div>
			<h1>Produtos</h1>
			<ul>
				{produtos.map((produto) => (
					<li key={produto.id}>
						{produto.nome} - R${produto.preco}
					</li>
				))}
			</ul>
		</div>
	);
};

export default HomePage;
