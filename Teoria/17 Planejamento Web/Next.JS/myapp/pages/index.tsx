import Link from 'next/link';

function Home() {
	return (
		<ul>
			<li>
				<Link href="/noticias/xpto">vai para pages/noticias/[id].tsx</Link>
			</li>
			<li>
				<Link href="/noticias?ano=2022&categoria=esportes">
					Vai para pages/noticias/[ano]/[categoria].js
				</Link>
			</li>
			<li>
				<Link href="/noticias/2022/esportes">
					Vai para pages/noticias/[ano]/[categoria].js
				</Link>
			</li>
		</ul>
	);
}

export default Home;
